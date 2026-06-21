# Status checks

Use status checks before previewing or publishing content.

```bash
python app.py status
```

## What to verify

- The content feed URL is configured.
- Telegram channels are detected when Telegram is enabled.
- Bluesky credentials are present when Bluesky is enabled.
- Instagram credentials are present only when Instagram publishing is intended.

## Recommended workflow

Run status checks after every `.env` change.

Do not publish until the status output matches the platforms you actually want to use.
