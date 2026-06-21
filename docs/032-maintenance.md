# Maintenance notes

Regular maintenance keeps the autoposter safe and predictable.

## Weekly checks

- Review recent logs.
- Confirm the content feed still loads.
- Run preview before the next publish.
- Check whether platform tokens are close to expiration.
- Confirm that `.env` is still local-only.

## After code changes

Run a syntax check and at least one dry-run before sending real posts.

## After platform errors

Fix only the affected platform first, then retry that platform with a specific slug or a dry-run.
