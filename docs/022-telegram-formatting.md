# Telegram formatting rules

Telegram posts should be concise, readable, and safe for HTML parse mode.

## Rules

- Escape user-facing text before sending it as HTML.
- Keep article links clickable.
- Preserve paragraph breaks between title, summary, and footer.
- Use language-specific read-more labels.
- Keep messages within Telegram length limits.

## Article shape

```txt
Emoji + linked title

Summary

Linked read-more footer
```

## Shorts shape

```txt
Linked short title

Short body

Linked open-short footer
```
