# Token safety rules

Access tokens and app passwords must be treated as secrets.

## Never commit

- real `.env` files
- Telegram bot tokens
- Bluesky app passwords
- Instagram access tokens
- Meta app secrets

## Safe storage

Keep secrets only on the machine where the autoposter runs.

Use `.env.example` for public documentation and `.env` for local private values.

## If a secret is exposed

1. Revoke or rotate the token.
2. Remove the secret from any public place.
3. Check logs and screenshots.
4. Update the local `.env` with the new value.
