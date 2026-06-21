# Instagram setup

Instagram publishing uses the official Instagram Graph API.

## Requirements

- Instagram Business or Creator account
- Facebook Page connected to the Instagram account
- Meta app with publishing permissions
- Long-lived access token
- Numeric Instagram user ID

## Required `.env` values

```env
INSTAGRAM_ACCESS_TOKEN=your-long-lived-token
INSTAGRAM_USER_ID=17841400000000000
```

`INSTAGRAM_USER_ID` is not the Instagram username. It is the numeric ID returned by the Graph API as `instagram_business_account.id`.

## Recommended checks

```bash
python app.py status
python app.py preview --platform instagram --limit 3
python app.py send --all --platform instagram --dry
```

Publish one post first before using `--all`.
