# Release checklist

Use this checklist before publishing a new app version or sharing a build.

## Code checks

- Run syntax checks.
- Run available tests.
- Verify dry-run output.
- Confirm platform formatting still looks correct.

## Repository checks

- Make sure `.env` is not committed.
- Make sure local database files are ignored.
- Review changed files for secrets.
- Update documentation when behavior changes.

## Manual publishing checks

- Test one platform first.
- Test one slug first.
- Review logs after the first real send.
