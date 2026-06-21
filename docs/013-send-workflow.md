# Send workflow

Use the send command only after status and preview checks pass.

## Safe sequence

```bash
python app.py status
python app.py preview --limit 3
python app.py send --all --dry
```

Then publish one item or one platform first.

## Send one slug

```bash
python app.py send --slug sample-market-update
```

## Send one platform

```bash
python app.py send --all --platform telegram_ru
```

## Avoid accidental bulk posting

Do not run `--all` for every platform until you confirm the pending list and message formatting.
