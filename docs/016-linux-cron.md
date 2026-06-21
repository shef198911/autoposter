# Linux cron notes

A Linux machine can run the autoposter with cron after manual testing is stable.

## Example dry-run cron

```cron
0 9 * * * cd /path/to/autoposter && /usr/bin/python3 app.py send --all --dry >> logs/autoposter.log 2>&1
```

Use dry-run first to confirm the environment, working directory, and logs.

## Real run

Only remove `--dry` after repeated successful dry-runs.

## Checklist

- Use an absolute project path.
- Use the correct Python executable.
- Keep `.env` in the project directory.
- Redirect logs for later review.
- Avoid very frequent schedules until publishing is proven stable.
