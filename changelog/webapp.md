# Changelog — Web Analyzer

Tags: `webapp/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

## [1.1.0] - 2026-07-05

- **X Intelligence:** when a token lists an X account, a "run x intel" button
  analyses it with the same scoring as the Telegram bot's Social Sentiment
  feature.
- The result shows a four-part radar (content, activity, engagement, trust), a
  0 to 100 score with a verdict, a rating for each part, key profile stats
  (followers, following, account age, posts per week, median views and likes)
  and any red flags. It works in light and dark mode.
- Every failure case (profile not found, no posts, busy, timed out,
  unavailable) has a clear message.
- The footer now shows the analyzer's own version.

## [1.0.0] - 2026-07-05

- **First release of the Web Analyzer:** the `/don` analysis from the Telegram
  bot, running in your browser. Paste a contract address or ticker to get the
  same score as the bot, with no sign-up and no API key.
- Supports Solana, Ethereum and Base. The analysis covers momentum, trend,
  structure and volume, chart patterns and support and resistance, with short-
  and long-term targets adjusted to the token's age.
- The result shows a signal-score gauge with a verdict, the thesis breakdown,
  an hourly candle chart with the entry zone and exit lines, trade-plan cards
  with upside from the current price, on-chain risk flags and links to the
  token's market page and X.
- Light and dark themes shared with the website, and links of the form
  ?q=<address or ticker> that open an analysis directly.
