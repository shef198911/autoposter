# Duplicate protection

The autoposter should avoid sending the same content item more than once to the same platform.

## How it works

Each published item should be recorded with enough information to identify:

- content type
- slug
- platform
- publish result
- time of publication

## Why it matters

Without duplicate protection, scheduled runs can repost the same article or short repeatedly.

## Safe behavior

If an item was already posted, the app should skip it unless a user explicitly targets that slug for a controlled repost.

## Manual checks

Use preview and dry-run before changing posting history.
