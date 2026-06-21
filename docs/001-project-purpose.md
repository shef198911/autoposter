# Project purpose

Coin Blog Autoposter is a local publishing helper for Coin Blog content.

The app reads a public content feed, detects items that have not been posted yet, and sends them to configured social platforms.

## Goals

- Keep posting logic local and easy to inspect.
- Avoid storing secrets in the repository.
- Support safe dry-run checks before publishing.
- Keep platform failures isolated, so one failed platform does not block the others.

## Current platforms

- Telegram RU
- Telegram EN
- Bluesky
- Instagram, when Graph API credentials are configured

## Non-goals

- It is not a hosted SaaS service.
- It is not intended to bypass platform rules.
- It does not publish to platforms that are not explicitly configured.
