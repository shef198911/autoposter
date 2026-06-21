#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import sqlite3
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

APP_NAME = "Local Autoposter"
VERSION = "0.1.0"
SITE_URL_DEFAULT = "https://example.com"
CONTENT_URL_DEFAULT = "https://example.com/content/insights.json"
DB_FILE_DEFAULT = "autopost.db"
ENV_FILE_DEFAULT = ".env"
GRAPH_API_VERSION = "v20.0"
USER_AGENT = f"{APP_NAME}/{VERSION}"
PLATFORMS = ["telegram", "telegram_en", "bsky", "instagram"]
TELEGRAM_LIMIT = 4096
BLUESKY_LIMIT = 300
INSTAGRAM_CAPTION_LIMIT = 2200
BLUESKY_PDS = "https://bsky.social"


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_env(path: str = ENV_FILE_DEFAULT) -> Dict[str, str]:
    env = dict(os.environ)
    p = Path(path)
    if not p.exists():
        return env
    for raw in p.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


@dataclass
class Config:
    env_file: str
    site_url: str
    content_url: str
    db_file: str
    env: Dict[str, str]

    @classmethod
    def from_env(cls, env_file: str = ENV_FILE_DEFAULT) -> "Config":
        env = load_env(env_file)
        return cls(
            env_file=env_file,
            site_url=env.get("SITE_URL", SITE_URL_DEFAULT).rstrip("/"),
            content_url=env.get("CONTENT_URL", CONTENT_URL_DEFAULT),
            db_file=env.get("DB_FILE", DB_FILE_DEFAULT),
            env=env,
        )


class Store:
    def __init__(self, db_file: str):
        self.conn = sqlite3.connect(db_file)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS posted (slug TEXT NOT NULL, platform TEXT NOT NULL, posted_at TEXT NOT NULL, PRIMARY KEY(slug, platform))"
        )
        self.conn.commit()

    def is_posted(self, slug: str, platform: str) -> bool:
        return self.conn.execute("SELECT 1 FROM posted WHERE slug=? AND platform=?", (slug, platform)).fetchone() is not None

    def mark(self, slug: str, platform: str) -> None:
        self.conn.execute("INSERT OR REPLACE INTO posted VALUES(?,?,?)", (slug, platform, now_iso()))
        self.conn.commit()

    def reset(self, slug: str, platform: str) -> None:
        self.conn.execute("DELETE FROM posted WHERE slug=? AND platform=?", (slug, platform))
        self.conn.commit()


def http_json(url: str, method: str = "GET", headers: Optional[Dict[str, str]] = None, data: Any = None, timeout: int = 30) -> Any:
    headers = {"User-Agent": USER_AGENT, **(headers or {})}
    body = None
    if data is not None:
        if isinstance(data, bytes):
            body = data
        else:
            body = json.dumps(data, ensure_ascii=False).encode("utf-8")
            headers.setdefault("Content-Type", "application/json")
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = resp.read().decode("utf-8")
            return json.loads(payload) if payload else {}
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')}") from e


def form_post(url: str, data: Dict[str, str], timeout: int = 60) -> Any:
    body = urllib.parse.urlencode(data).encode("utf-8")
    return http_json(url, "POST", {"Content-Type": "application/x-www-form-urlencoded"}, body, timeout)


def text_value(value: Any, locale: str = "en") -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, dict):
        return str(value.get(locale) or value.get("en") or value.get("ru") or next(iter(value.values()), "")).strip()
    return str(value).strip()


def slug_of(item: Dict[str, Any]) -> str:
    return text_value(item.get("slug") or item.get("id") or item.get("path"))


def title_of(item: Dict[str, Any], locale: str = "en") -> str:
    return text_value(item.get("title") or item.get("name") or item.get("headline"), locale)


def summary_of(item: Dict[str, Any], locale: str = "en") -> str:
    return text_value(item.get("summary") or item.get("description") or item.get("excerpt"), locale)


def absolute_url(value: Any, cfg: Config) -> str:
    value = text_value(value)
    if not value:
        return ""
    if value.startswith(("http://", "https://")):
        return value
    return cfg.site_url + (value if value.startswith("/") else "/" + value)


def article_url(item: Dict[str, Any], cfg: Config) -> str:
    direct = text_value(item.get("url") or item.get("href"))
    if direct:
        return absolute_url(direct, cfg)
    return cfg.site_url + "/insights/" + urllib.parse.quote(slug_of(item))


def trim_plain(value: str, limit: int) -> str:
    value = re.sub(r"\s+", " ", text_value(value)).strip()
    return value if len(value) <= limit else value[: max(0, limit - 3)].rstrip() + "..."


def image_candidates(item: Dict[str, Any], cfg: Config) -> List[str]:
    fields = [item.get("instagramImage"), item.get("socialImage"), item.get("social_image"), item.get("ogImage"), item.get("og_image"), item.get("cover"), item.get("image")]
    out: List[str] = []
    for field in fields:
        url = absolute_url(field, cfg)
        if url and url not in out:
            out.append(url)
    return out


def instagram_image_candidates(item: Dict[str, Any], cfg: Config) -> List[str]:
    return [u for u in image_candidates(item, cfg) if re.search(r"\.(jpe?g|png)(?:[?#].*)?$", u, re.I)]


def telegram_text(item: Dict[str, Any], cfg: Config, locale: str = "en") -> str:
    title = html.escape(title_of(item, locale) or "Open article", quote=False)
    summary = html.escape(summary_of(item, locale), quote=False)
    url = html.escape(article_url(item, cfg), quote=True)
    footer = "🔗 Читать полностью" if locale == "ru" else "🔗 Read more"
    parts = [f'<a href="{url}">🔗 {title}</a>']
    if summary:
        parts.append(summary)
    parts.append(f'<a href="{url}">{html.escape(footer, quote=False)}</a>')
    return "\n\n".join(parts)[:TELEGRAM_LIMIT]


def bluesky_text(item: Dict[str, Any], cfg: Config) -> str:
    title = title_of(item, "en") or title_of(item, "ru") or "New post"
    summary = summary_of(item, "en") or summary_of(item, "ru")
    url = article_url(item, cfg)
    return trim_plain(f"{title}\n\n{summary}\n\n{url}" if summary else f"{title}\n\n{url}", BLUESKY_LIMIT)


def instagram_caption(item: Dict[str, Any], cfg: Config) -> str:
    title = title_of(item, "en") or title_of(item, "ru") or "New post"
    summary = summary_of(item, "en") or summary_of(item, "ru")
    url = article_url(item, cfg)
    return trim_plain(f"{title}\n\n{summary}\n\nRead more: {url}" if summary else f"{title}\n\nRead more: {url}", INSTAGRAM_CAPTION_LIMIT)


def load_content(cfg: Config) -> List[Dict[str, Any]]:
    data = http_json(cfg.content_url, timeout=30)
    if isinstance(data, list):
        return [x for x in data if isinstance(x, dict)]
    if isinstance(data, dict):
        items: List[Dict[str, Any]] = []
        for key in ("items", "posts", "articles", "data", "shorts"):
            if isinstance(data.get(key), list):
                items.extend([x for x in data[key] if isinstance(x, dict)])
        return items
    return []


class Sender:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.env = cfg.env

    def send_telegram(self, item: Dict[str, Any], platform: str) -> Dict[str, Any]:
        token = self.env.get("TELEGRAM_BOT_TOKEN")
        chat_id = self.env.get("TELEGRAM_CHANNEL_ID_EN" if platform == "telegram_en" else "TELEGRAM_CHANNEL_ID")
        if not token or not chat_id:
            raise RuntimeError("Telegram is not configured")
        body = {"chat_id": chat_id, "text": telegram_text(item, self.cfg, "en" if platform == "telegram_en" else "ru"), "parse_mode": "HTML"}
        return form_post("https:" + f"//api.telegram.org/bot{token}/sendMessage", body)

    def send_bsky(self, item: Dict[str, Any]) -> Dict[str, Any]:
        handle = self.env.get("BSKY_HANDLE")
        password = self.env.get("BSKY_APP_PASSWORD")
        if not handle or not password:
            raise RuntimeError("Bluesky is not configured")
        session = http_json(f"{BLUESKY_PDS}/xrpc/com.atproto.server.createSession", "POST", data={"identifier": handle, "password": password}, timeout=30)
        token = session["accessJwt"]
        did = session["did"]
        record = {"$type": "app.bsky.feed.post", "text": bluesky_text(item, self.cfg), "createdAt": now_iso()}
        return http_json(f"{BLUESKY_PDS}/xrpc/com.atproto.repo.createRecord", "POST", {"Authorization": f"Bearer {token}"}, {"repo": did, "collection": "app.bsky.feed.post", "record": record}, 60)

    def send_instagram(self, item: Dict[str, Any]) -> Dict[str, Any]:
        token = self.env.get("INSTAGRAM_ACCESS_TOKEN")
        user_id = self.env.get("INSTAGRAM_USER_ID")
        if not token or not user_id:
            raise RuntimeError("Instagram is not configured")
        images = instagram_image_candidates(item, self.cfg)
        if not images:
            raise RuntimeError("No JPG/PNG image for Instagram")
        base = "https:" + f"//graph.facebook.com/{GRAPH_API_VERSION}/{user_id}"
        errors = []
        for image_url in images:
            try:
                create = form_post(f"{base}/media", {"image_url": image_url, "caption": instagram_caption(item, self.cfg), "access_token": token})
                creation_id = create.get("id")
                if not creation_id:
                    raise RuntimeError(f"No creation id: {create}")
                publish = form_post(f"{base}/media_publish", {"creation_id": creation_id, "access_token": token})
                return {"image": image_url, "id": publish.get("id"), "creation_id": creation_id, "imageErrors": errors}
            except Exception as e:
                errors.append({"image": image_url, "error": str(e)})
        raise RuntimeError("Instagram rejected all images: " + json.dumps(errors, ensure_ascii=False))

    def send(self, item: Dict[str, Any], platform: str) -> Dict[str, Any]:
        if platform in ("telegram", "telegram_en"):
            return self.send_telegram(item, platform)
        if platform == "bsky":
            return self.send_bsky(item)
        if platform == "instagram":
            return self.send_instagram(item)
        raise RuntimeError(f"Unsupported platform: {platform}")


class Engine:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.store = Store(cfg.db_file)
        self.sender = Sender(cfg)

    def items(self) -> List[Dict[str, Any]]:
        return load_content(self.cfg)

    def status(self) -> Dict[str, Any]:
        env = self.cfg.env
        return {"app": f"{APP_NAME} v{VERSION}", "siteUrl": self.cfg.site_url, "contentUrl": self.cfg.content_url, "dbFile": self.cfg.db_file, "platforms": {"telegram": bool(env.get("TELEGRAM_BOT_TOKEN") and env.get("TELEGRAM_CHANNEL_ID")), "telegram_en": bool(env.get("TELEGRAM_BOT_TOKEN") and env.get("TELEGRAM_CHANNEL_ID_EN")), "bsky": bool(env.get("BSKY_HANDLE") and env.get("BSKY_APP_PASSWORD")), "instagram": bool(env.get("INSTAGRAM_ACCESS_TOKEN") and env.get("INSTAGRAM_USER_ID"))}}

    def preview_text(self, item: Dict[str, Any], platform: str) -> str:
        if platform == "telegram":
            return telegram_text(item, self.cfg, "ru")
        if platform == "telegram_en":
            return telegram_text(item, self.cfg, "en")
        if platform == "bsky":
            return bluesky_text(item, self.cfg)
        if platform == "instagram":
            return instagram_caption(item, self.cfg)
        return ""

    def send_items(self, platforms: List[str], slug: Optional[str], all_items: bool, dry: bool) -> List[Dict[str, Any]]:
        results = []
        for item in self.items():
            item_slug = slug_of(item)
            if slug and item_slug != slug:
                continue
            if not slug and not all_items:
                continue
            row = {"slug": item_slug, "title": title_of(item, "en") or title_of(item, "ru"), "results": {}}
            for platform in platforms:
                try:
                    if self.store.is_posted(item_slug, platform) and not dry:
                        row["results"][platform] = {"status": "skip", "reason": "already posted"}
                    elif dry:
                        row["results"][platform] = {"status": "dry", "text": self.preview_text(item, platform)}
                    else:
                        sent = self.sender.send(item, platform)
                        self.store.mark(item_slug, platform)
                        row["results"][platform] = {"status": "ok", "response": sent}
                except Exception as e:
                    row["results"][platform] = {"status": "error", "error": str(e)}
            results.append(row)
        return results


def parse_platforms(value: str) -> List[str]:
    platforms = [x.strip() for x in value.split(",") if x.strip()]
    bad = [p for p in platforms if p not in PLATFORMS]
    if bad:
        raise SystemExit("Unknown platform: " + ", ".join(bad))
    return platforms or PLATFORMS


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="app.py")
    parser.add_argument("--env", default=ENV_FILE_DEFAULT)
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("self-test")
    sub.add_parser("status")
    p_preview = sub.add_parser("preview")
    p_preview.add_argument("--limit", type=int, default=5)
    p_preview.add_argument("--platform", default="telegram")
    p_send = sub.add_parser("send")
    p_send.add_argument("--slug")
    p_send.add_argument("--all", action="store_true")
    p_send.add_argument("--platform", default="telegram")
    p_send.add_argument("--dry", action="store_true")
    p_mark = sub.add_parser("mark")
    p_mark.add_argument("--slug", required=True)
    p_mark.add_argument("--platform", required=True)
    p_reset = sub.add_parser("reset")
    p_reset.add_argument("--slug", required=True)
    p_reset.add_argument("--platform", required=True)
    args = parser.parse_args(argv)
    cfg = Config.from_env(args.env)
    engine = Engine(cfg)
    if args.cmd in (None, "status"):
        print(json.dumps(engine.status(), ensure_ascii=False, indent=2))
        return 0
    if args.cmd == "self-test":
        print(f"{APP_NAME} v{VERSION} self-test")
        print(json.dumps(engine.status(), ensure_ascii=False, indent=2))
        print("Self-test OK")
        return 0
    if args.cmd == "preview":
        for item in engine.items()[: args.limit]:
            print("=" * 60)
            print(slug_of(item), "—", title_of(item, "en") or title_of(item, "ru"))
            for platform in parse_platforms(args.platform):
                print(f"\n[{platform}]\n{engine.preview_text(item, platform)}")
        return 0
    if args.cmd == "send":
        print(json.dumps(engine.send_items(parse_platforms(args.platform), args.slug, args.all, args.dry), ensure_ascii=False, indent=2))
        return 0
    if args.cmd == "mark":
        engine.store.mark(args.slug, args.platform)
        print("marked")
        return 0
    if args.cmd == "reset":
        engine.store.reset(args.slug, args.platform)
        print("reset")
        return 0
    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
