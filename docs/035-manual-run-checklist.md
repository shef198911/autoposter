# Manual run checklist

Use this checklist when running the autoposter by hand.

## Before running

- Confirm the latest code is downloaded.
- Confirm dependencies are installed.
- Confirm `.env` exists locally.
- Confirm the content feed opens in a browser.

## Command sequence

```bash
python app.py status
python app.py preview --limit 3
python app.py send --all --dry
```

## Before real sending

Review the preview output and confirm the target platforms are correct.

If anything looks wrong, stop and fix the configuration before publishing.
