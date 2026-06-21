# Platform failure handling

Each publishing platform should be treated as an independent destination.

A failure on one platform should not block all other configured platforms.

## Expected behavior

- Telegram failure should not block Bluesky.
- Bluesky failure should not block Telegram.
- Instagram failure should not block Telegram or Bluesky.
- Missing credentials should skip that platform safely.

## What to inspect

When a platform fails, check:

- credentials
- platform API status
- formatted message length
- image URL availability
- rate limits

## Recovery

Fix the platform-specific issue and retry only the affected platform when possible.
