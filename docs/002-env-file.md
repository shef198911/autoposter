# Environment configuration

The app reads settings from a local `.env` file.

The real `.env` file must stay on the machine where the app runs and must not be committed to GitHub.

## Recommended setup

1. Copy `.env.example` to `.env`.
2. Fill only the platforms you want to use.
3. Run a status check before sending anything.

```bash
python app.py status
```

## Safety rules

- Do not commit real access tokens.
- Do not share the `.env` file in chat or screenshots.
- Keep platform credentials separate from code changes.
- Rotate any token that was accidentally exposed.

## Common variables

- Content feed URL
- Telegram bot token and channel IDs
- Bluesky handle and app password
- Instagram access token and user ID
