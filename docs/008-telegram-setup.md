# Telegram setup

Telegram posting requires a bot token and one or more channel IDs.

## Create a bot

1. Open Telegram.
2. Start a chat with `@BotFather`.
3. Create a new bot.
4. Copy the bot token into your local `.env` file.

## Add the bot to a channel

1. Open the target channel.
2. Add the bot as an administrator.
3. Allow the bot to post messages.

## Channel IDs

Public channels usually use usernames such as:

```txt
@CoinsBlog_eng
```

Private channels may require numeric IDs.

## Safety check

Before sending real posts, run:

```bash
python app.py status
python app.py preview --platform telegram_ru --limit 3
```

Only publish after the preview text looks correct.
