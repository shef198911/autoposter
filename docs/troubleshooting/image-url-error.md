# Troubleshooting: image URL error

Some platforms need a public image URL before they can publish a post.

Instagram is especially strict because Meta downloads the image from the URL during media container creation.

## Symptoms

- The platform returns an image fetch error.
- The post is skipped because no image candidate was found.
- Instagram creates a media container error.

## Checks

1. Open the image URL in a browser.
2. Confirm the image uses HTTPS.
3. Confirm the image is public and does not require login.
4. Prefer JPG or PNG for social posting.
5. Avoid SVG for Instagram publishing.

## Recommended image pattern

```txt
/uploads/insights/social/{slug}-1200x630.jpg
```

## Recovery

Fix the image URL or add a social JPG before retrying the post.
