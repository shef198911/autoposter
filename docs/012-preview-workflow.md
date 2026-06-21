# Preview workflow

Preview mode helps check formatted output before any real publish action.

```bash
python app.py preview --limit 3
```

## Platform-specific preview

```bash
python app.py preview --platform telegram_ru --limit 3
python app.py preview --platform bluesky --limit 3
python app.py preview --platform instagram --limit 3
```

## What to review

- title text
- summary text
- links
- language selection
- image candidate, when shown
- platform-specific footer

If the preview looks wrong, fix the feed or configuration before sending.
