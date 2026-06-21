# Bluesky formatting rules

Bluesky posts should be short, clear, and link-friendly.

## Rules

- Keep text within the Bluesky character limit.
- Preserve one blank line between title and summary when possible.
- Prefer an external link embed for articles and shorts.
- Use the English title and summary for the default Bluesky post.

## Recommended shape

```txt
Title

Summary
```

The external embed can carry the article URL, link title, description, and image.

## Checks

Before publishing, preview the Bluesky output:

```bash
python app.py preview --platform bluesky --limit 3
```
