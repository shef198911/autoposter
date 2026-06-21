# Troubleshooting: item already posted

The autoposter tracks sent items to avoid duplicate publications.

## Symptoms

An item exists in the feed but does not appear in the pending list.

The most likely reason is that it was already recorded as posted for the selected platform.

## Checks

1. Confirm the item `slug` is correct.
2. Check whether the local database already contains the item.
3. Confirm you are checking the right platform.
4. Run preview with a small limit to inspect pending items.

```bash
python app.py preview --limit 5
```

## Safe recovery

Do not delete posting history unless you intentionally want to republish old items.

If you need a one-time repost, prefer sending a specific slug after confirming the output.
