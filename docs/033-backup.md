# Backup notes

Backups are useful before changing local runtime state.

## What to back up

- local `.env` file
- local posting database
- logs that may help debug failures
- exported app archives shared between machines

## What not to publish

Backups can contain private tokens or posting history, so they should not be committed to GitHub.

## Before cleanup

Before deleting local history or resetting a database, copy the file to a safe private location.

## After restore

Run status and preview checks before sending real posts again.
