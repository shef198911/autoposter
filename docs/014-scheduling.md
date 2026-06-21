# Scheduling notes

The local autoposter does not need a hosted cron service by default.

You can run it manually or schedule it on the machine where the `.env` file is stored.

## Manual run

```bash
python app.py status
python app.py preview --limit 3
python app.py send --all --dry
```

## Scheduled run ideas

- Windows Task Scheduler
- cron on Linux
- a manual daily checklist

## Safety recommendation

Start with manual runs. Add scheduling only after the app has posted correctly several times.
