# Local database

The autoposter uses local state to avoid publishing the same item repeatedly.

## Purpose

The local database records which content items have already been sent to each platform.

This helps prevent duplicates when the same feed item appears in multiple runs.

## Safety notes

- Do not commit a real local database file.
- Treat the database as runtime state.
- Back it up before manual cleanup.
- Avoid deleting history unless you intentionally want to republish items.

## Typical checks

If an item is not pending, confirm whether it was already posted for that platform.
