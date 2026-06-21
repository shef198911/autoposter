# Pre-publish checklist

Use this checklist before sending real posts.

## Confirm configuration

- `.env` exists locally.
- Only intended platforms are configured.
- Content feed URL loads successfully.
- Platform credentials are current.

## Confirm output

```bash
python app.py status
python app.py preview --limit 3
python app.py send --all --dry
```

## Confirm scope

- Use one slug first when testing.
- Use one platform first after changing credentials.
- Avoid bulk publishing until output is reviewed.
