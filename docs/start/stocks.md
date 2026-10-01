# Tokenized stocks

The bot and the Web Analyzer also cover **tokenized stocks** — official on-chain
versions of listed equities — and run them through exactly the same engine as
every other token. Same score, same entry and exit zones, same card.

## What is covered

| Issuer | Chain | How the tokens are named | Listed |
|---|---|---|---|
| **xStocks** (Backed Finance) | Solana | `TSLAx`, "Tesla xStock" | 46 |
| **Robinhood** stock tokens | Robinhood Chain | `TSLA`, "Tesla • Robinhood Token" | 42 |

That is 67 underlyings in total — stocks, a handful of ETFs (SPY, QQQ, VTI,
TQQQ), commodity funds (GLD, SLV, USO) and SpaceX exposure — and 21 of them are
listed by both issuers. Counts are as of the registry's last verification and
grow as the issuers list more.

## Why there is a list at all

Typing a stock ticker into a DEX search does not find the stock. It finds the
deepest pool for that ticker, and for stock tickers that is usually a copycat
with faked liquidity. On the day this was built, `NVDA` resolved to a two-day-old
"nvda nvda" showing $11.6M of liquidity and $1.7K of daily volume, ahead of the
official token doing $29M a day.

So DigitalDon keeps a **curated registry of the official contracts**, verified
against the live index every week, and every stock lookup resolves against it
first. The ordinary search still runs behind it — a memecoin that happens to
share a ticker stays reachable — it just never outranks the real thing.

## In Telegram

- **`/stocks`** opens the catalogue: counts per issuer and a paged keyboard.
  Tap a stock to analyse it.
- **`/don TSLA`** works too. If the stock is listed by both issuers you get a
  picker that names them — `TSLA · xStocks [SOL]`, `TSLA · Robinhood [RH]` —
  followed by any plain tokens that share the ticker.
- Pasting a stock token's contract address in a group behaves as for any token.
  The card knows it is a stock either way.

## In the Web Analyzer

The switch under the logo — **tokens | stocks** — flips the page into the stocks
section: a board of every listed stock, filterable by kind and issuer, that
narrows as you type. One click runs the deepest listing and opens the chart. A
stock listed with both issuers gets a `SOL · RH` switch in the card header.

Deep links: `?view=stocks` opens the board, `?view=stocks&q=TSLA` runs Tesla.

## What is different on a stock card

- A **`tokenized stock · xStocks`** tag next to the pair, and the **US market
  state** — `market open · closes 16:00 ET` or `market closed · opens Mon 09:30
  ET`. The on-chain token is quoted and scored around the clock, but the equity
  underneath only moves during the regular session. Weekend hourly volume on
  `TSLAx` is about six times thinner than on weekdays, so a Monday-morning chart
  can carry two days of near-empty candles; the line is there so you know.
- **No holder analysis.** A tokenized stock's supply sits with the issuer and
  the exchanges that custody it. A cluster map would read a custody wallet as a
  whale and its funder as an insider, so the button is not offered.
- **It is scored as an equity, not as a young token.** The engine has a
  dedicated profile for tokenized stocks, chosen by what the token is rather
  than by how old its pool is. Three things follow:

  - **No launch candles are stripped.** A stock token's first on-chain candles
    are an ordinary trading day for a company already priced by an exchange.
    Trimming them would delete real history and invent a spike.
  - **On-chain swap counts barely move the score.** A few hundred swaps a day
    against the billions the same share turns over on its home exchange is not
    sentiment. The weight goes to trend and the moving-average stack instead,
    which is what equity traders actually read.
  - **The short horizon is a swing, not a scalp.** It is quoted from about 1%
    of upside rather than 3%, and named *swing (days)* and *position (weeks)*.
    Apple moving 3% is a news event; on the old bar the answer was "no tradable
    range" on almost every stock, almost every day.

- **The on-chain block answers stock questions.** Instead of unlock overhang
  and a rug verdict — both computed from a supply figure that is custody
  inventory, not a cap table — it reports the listing's depth as an execution
  fact (how much size it absorbs before you pay slippage), the on-chain volume,
  which way on-chain flow leaned, and a plain note that the supply is custodial.
  That last line is also why no market capitalisation is quoted: the number
  would describe the wrapper, not the company.

## Thin listings

Liquidity across the catalogue is uneven — `SPYx` holds millions, some
listings hold a few hundred dollars. The board sorts by liquidity and marks the
thin end (`thin` = under $5k everywhere) rather than hiding official tokens. A
chart drawn on a $200 pool is still a chart; treat its score accordingly.

{% hint style="info" %}
Not financial advice. Tokenized stocks are issued by third parties under their
own terms; DigitalDon reads the on-chain market for them and nothing more.
{% endhint %}
