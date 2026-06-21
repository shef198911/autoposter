# Restore notes

Restore steps are useful when moving the autoposter to another machine or recovering from a local problem.

## Restore order

1. Clone or download the repository.
2. Install dependencies.
3. Restore the private `.env` file from a safe backup.
4. Restore the local database only if you want to preserve posting history.
5. Run status and preview checks.

## Verification

```bash
python app.py status
python app.py preview --limit 3
```

Do not run real sends until the restored environment is verified.
