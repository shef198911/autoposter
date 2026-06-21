# Troubleshooting: content URL error

The autoposter needs to download a public JSON feed before it can find items to publish.

## Symptoms

The app may fail during `check`, `preview`, or `send` if the feed cannot be loaded.

Common causes:

- The content URL is wrong.
- The site is temporarily unavailable.
- DNS or internet access is not working on the local machine.
- The endpoint returns HTML instead of JSON.

## Checks

1. Open the content URL in a browser.
2. Confirm the response is JSON.
3. Check that the URL uses HTTPS.
4. Retry after a few minutes if the site is being deployed.

## Safe recovery

Do not publish while the feed is unavailable. Run `preview` again after the feed loads correctly.
