# Glossary

Terms that show up on the cards, in plain language.

## Chart & score

**Score (0–100)** — the composite verdict of every signal the analysis checks,
weighted by the token's age profile. Not a probability, not a price target. See
[How the score works](../engine/score.md).

**Profile** — 🆕 Fresh, 🌱 Early or 🏛 Established, decided purely by token age.
Changes what the score leans on. See [Token profiles](../engine/profiles.md).

**Support / resistance** — price levels the chart has repeatedly bounced off
(support) or been rejected at (resistance). Everything in the trade plan hangs
off these two.

**Range position** — where the current price sits between the chart's low and
high, as a fraction. `0.1` is near the low, `0.9` is near the high.

**RSI** — momentum oscillator, 0–100. Low readings are usually called oversold,
high ones overbought. Reality is messier, which is why it's one of many signals
here and not the whole answer.

**Stoch RSI** — RSI's own oscillator. Faster and noisier than RSI, useful for
timing rather than direction.

**MACD** — trend/momentum crossover indicator. Its histogram flipping sign is the
part worth watching, especially when volume backs the flip.

**Bollinger Bands** — a volatility envelope around a moving average. Price at the
lower band is a stretched-down reading, at the upper band a stretched-up one.

**EMA 20 / 50 / 200** — exponential moving averages. The stack (which sits above
which) is the cheapest read on trend there is.

**Golden cross / death cross** — the 50 EMA crossing above (golden) or below
(death) the 200. "Confirmed" means volume backed it up.

**RSI divergence** — price makes a lower low but RSI makes a higher low
(bullish), or price makes a higher high while RSI makes a lower high (bearish).
Classic exhaustion signal.

**Launch candles** — the first hours of a token's life, where price does
something absurd and then never revisits it. Excluded before analysing young
tokens, otherwise every level derived from the chart is garbage. See
[Token profiles](../engine/profiles.md#stripping-launch-candles).

**Launch-spike ATH** — an all-time high that was set in those first hours and
never approached again. When the card flags it, ignore every "% below ATH" number
on that card.

## On-chain

**MCap (market cap)** — circulating supply × price.

**FDV (fully diluted valuation)** — *total* supply × price. FDV much larger than
MCap means a lot of tokens haven't hit the market yet.

**Liquidity** — how much is actually in the pool. Low liquidity relative to
market cap means your exit moves the price.

**Buy/sell pressure** — the 24h split of buy vs sell transactions. Crude, but
it's a real number from real trades.

## Holders

**Concentration** — how much of supply the top 10 / top 20 wallets hold.

**Cluster (bubble)** — a group of wallets that are demonstrably connected — same
funding origin. Ten wallets holding 3% each is fine; ten wallets funded by the
same address holding 3% each is one wallet holding 30%.

**Bubble risk** — Low / Mid / High verdict derived from how much supply sits
inside those clusters, weighted by how strong the evidence is.

**Fresh wallet** — a wallet whose first activity is around the token's launch. It
exists to hold this token.

**Sniper** — bought in the earliest blocks after the pool opened.

**Bundle** — a group of buys landing together. Coordinated, not coincidental.

**Insider** — a wallet funded by the token's own creator.

**Honeypot** — you can buy, you cannot sell. If detected, the card leads with it
in red and nothing else on that card matters.

## Groups

**Call** — the first `/don` scan of a token in a group, credited to whoever ran
it. Feeds both [PNL cards](../using/pnl-cards.md) and the
[leaderboard](../using/leaderboard.md).

**Peak multiple** — how far a token got after it was called, measured from the
market cap at the first scan to its highest point since. The number on both the
PNL card and the leaderboard.

**Hit / flop** — a call that reached at least 2x is a hit; one that never got
above where it was called is a flop. Everything between is neither.
