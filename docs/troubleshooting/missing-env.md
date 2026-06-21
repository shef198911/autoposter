# Troubleshooting: missing `.env`

If the app reports missing credentials, first check that the `.env` file exists in the project folder.

## Symptoms

You may see a platform status such as:

```txt
SKIP — missing token or channel ID
```

or:

```txt
Instagram: SKIP — missing INSTAGRAM_ACCESS_TOKEN or INSTAGRAM_USER_ID
```

## Checks

1. Confirm `.env` is in the same folder as `app.py`.
2. Confirm the file is named `.env`, not `.env.txt`.
3. Confirm each variable uses `KEY=value` format.
4. Restart the app after editing `.env`.

## Safety

Do not commit the real `.env` file.

Use `.env.example` only as a public template.
