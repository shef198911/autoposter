# Content feed format

The autoposter reads content from a public JSON feed.

By default, the app is expected to work with the Coin Blog feed:

```txt
https://www.primus-stat.xyz/content/insights.json
```

## Expected content types

The feed can include two main item groups:

- articles or posts
- shorts

## Common article fields

- `slug`
- `title`
- `ru_title`
- `description`
- `ru_description`
- `seoDescription`
- `ru_seoDescription`
- `socialImage`
- `cover`

## Common short fields

- `slug`
- `title`
- `ru_title`
- `body`
- `ru_body`
- `image`
- `socialImage`

## Notes

The app should tolerate missing optional fields and use fallbacks where possible.
