# Local Autoposter

Clean public scaffold for a local autoposter.

This repository intentionally contains no real tokens, no `.env`, no posting database, and no real project URLs except `example.com` placeholders.

## Setup

1. Copy `.env.example` to `.env`.
2. Fill `SITE_URL` and `CONTENT_URL`.
3. Add credentials only for the platforms you want to use.
4. Run:

```bash
python app.py self-test
python app.py status
python app.py preview --limit 5
python app.py send --all --dry
```

Real posting:

```bash
python app.py send --all
```

## Do not commit

- `.env`
- `autopost.db`
- logs
- Python cache files

These are ignored by `.gitignore`.
