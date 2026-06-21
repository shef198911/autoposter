# Secret scanning notes

Secret scanning helps catch credentials before they are shared or committed.

## What to scan for

- Telegram bot tokens
- Bluesky app passwords
- Meta app secrets
- Instagram access tokens
- private `.env` values

## Manual review checklist

Before pushing changes, review files for:

```txt
TOKEN=
PASSWORD=
SECRET=
ACCESS_TOKEN=
APP_PASSWORD=
```

## Repository safety

Keep `.env` ignored and publish only `.env.example` templates.

If a real token is committed, rotate it immediately.
