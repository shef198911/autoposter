# Supported platforms

The autoposter is designed around independent platform senders.

If one platform is not configured or returns an error, the others should continue to work.

## Telegram

Telegram posting uses a bot token and one or more channel IDs.

Typical channels:

- Russian channel
- English channel

## Bluesky

Bluesky posting uses a handle and an app password.

The app can create short text posts and attach external links when supported by the sender logic.

## Instagram

Instagram posting uses the official Instagram Graph API.

It requires:

- Instagram Business or Creator account
- connected Facebook Page
- Meta app permissions
- long-lived access token
- numeric Instagram user ID

## Disabled platforms

A platform with missing credentials should be skipped instead of breaking the whole run.
