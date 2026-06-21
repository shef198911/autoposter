# Bluesky setup

Bluesky posting requires a handle and an app password.

## Create an app password

1. Open Bluesky settings.
2. Go to app passwords.
3. Create a new app password for the autoposter.
4. Store it only in your local `.env` file.

## Required values

Typical values:

```env
BSKY_HANDLE=your-handle.bsky.social
BSKY_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx
```

For Coin Blog, the handle may use a custom domain.

## Safety notes

- Do not use your main account password.
- Do not commit the app password.
- Rotate the app password if it is exposed.

## Test before publishing

```bash
python app.py status
python app.py preview --platform bluesky --limit 3
python app.py send --all --platform bluesky --dry
```
