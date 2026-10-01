# Supported chains

## Always on

| Chain | Search | Chart & score | Holder analysis |
|---|---|---|---|
| **Solana** | ✅ | ✅ | ✅ full (owner-level) |
| **Ethereum** | ✅ | ✅ | ✅ full |
| **Base** | ✅ | ✅ | ✅ full |

## Also available

| Chain | Notes |
|---|---|
| **BSC** | On by default. Chart and score are full-strength; holder analysis has thinner evidence to work with than the three above. |
| **Robinhood Chain** | On by default. Newer chain — clustering, concentration, fresh wallets and insiders all work; sniper and bundle signals aren't available, and are omitted from the card rather than shown as zero. |
| **Arbitrum** | On by default. Chart and score are full-strength — Arbitrum has been indexed for years and the candle history is as good as Ethereum's. Holder analysis behaves like Robinhood Chain: clustering, concentration, wallet quality and insiders work, sniper and bundle signals aren't available and are omitted rather than shown as zero. |
| **Mantle** | On by default. Chart and score are full-strength — Mantle is indexed by both DexScreener and GeckoTerminal, so the candle history the score runs on is the same quality as Base's. Holder analysis behaves like Arbitrum: clustering, concentration, wallet quality and insiders work, sniper and bundle signals aren't available and are omitted rather than shown as zero. |
| **Arc** | On by default from day one — the chain's mainnet opened 2026-09-16 and this build was wired two days ahead of it. Chart and score are full-strength wherever a pair resolves: GeckoTerminal indexed Arc before launch, so the candle history the score runs on is the same quality as Base's. The caveat is discovery rather than analysis — a token has to be listed by DexScreener to be *found*, and DexScreener had not indexed Arc when this shipped, so an Arc search that comes back empty is far more likely to mean "not indexed yet" than "not covered". Holder analysis behaves like Arbitrum and Mantle: clustering, concentration, wallet quality and insiders work, while sniper and bundle signals aren't available and are omitted rather than shown as zero. Arc's gas token is USDC rather than ETH, which the wallet-value maths already accounts for. |

Which chains are live is an instance-level setting. Out of the box all eight are
on — Solana, Ethereum and Base always, plus BSC, Robinhood Chain, Arbitrum,
Mantle and Arc — and an operator can narrow that list per deployment.

## When a ticker exists on several chains

Searching `PEPE` will match tokens on more than one chain. Rather than picking
for you, the bot shows a disambiguation picker with the chain, price and
liquidity of each match, and you tap the one you meant. The Web Analyzer does the
same thing with a list of cards.

Contract addresses skip this entirely — a Solana mint or an `0x` address resolves
directly. (An `0x` address *can* exist on more than one EVM chain, so the chain
is taken from whichever pair actually resolves, and results are kept separate per
chain so Base and Ethereum never bleed into each other.)

## What "supported" actually needs

For a token to be analysable at all, three things have to line up:

1. **The pair is discoverable** — that's where price, liquidity, FDV, market cap
   and the 24h buy/sell split come from.
2. **Chart history exists for the pool** — no candles, no technical analysis.
   Very new or very thin pools often have none.
3. **There's enough of it** — below a small floor of usable candles there's
   nothing honest to compute.

If (2) or (3) fail on a token that's only a few days old, you don't get an
error — you get a
[fresh-launch card](../engine/onchain.md#fresh-launch-cards) built from chain
data instead. If the token is older than that, missing chart data means the
source failed, and the card says so rather than pretending the token is new.
