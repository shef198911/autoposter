# Dry-run guide

Dry-run mode is the safest way to check what the autoposter would do without publishing anything.

Use it before any real send command.

## Check all pending items

```bash
python app.py send --all --dry
```

## Check one platform

```bash
python app.py send --all --platform telegram_ru --dry
```

## Check one item

```bash
python app.py send --slug sample-market-update --dry
```

## What dry-run should confirm

- The content feed loads correctly.
- The item is recognized as pending.
- The target platform is configured.
- The formatted message looks correct.
- No real platform API publish action is executed.

If dry-run output is unexpected, fix configuration before publishing.
