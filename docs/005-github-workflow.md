# GitHub workflow

This repository should keep changes small, readable, and easy to review.

## Recommended commit style

Use one focused commit per topic.

Good examples:

- `Document environment configuration`
- `Add Telegram setup notes`
- `Add Instagram troubleshooting guide`
- `Add content feed example`

Avoid vague commit messages such as:

- `update`
- `fix`
- `changes`
- `misc`

## Branches

For routine documentation and small safe changes, commits can go directly to `main`.

For risky code changes, create a feature branch first and test before merging.

## Safety checklist

Before pushing, make sure the change does not include:

- real tokens
- passwords
- local database files
- private `.env` values
- generated cache files
