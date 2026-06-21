# Logging notes

Logs are important when the autoposter runs without a visible terminal.

## What to log

- command start time
- selected platform
- selected slug, if any
- dry-run mode
- feed loading errors
- platform API errors
- successful publish IDs

## Local log file idea

```bash
python app.py send --all --dry >> logs/autoposter.log 2>&1
```

## Safety

Logs should not include full access tokens, app passwords, or private `.env` values.

If a log accidentally contains secrets, rotate those credentials before sharing the log.
