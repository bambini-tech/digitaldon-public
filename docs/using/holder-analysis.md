# Holder analysis

The chart tells you what price did. Holder analysis tells you who's holding the
bag and whether they're all the same person.

Available as the **👥 Holder Analysis** button in Telegram and the **holder
intelligence** panel (with the bubble map) in the Web Analyzer. Both run the same
analysis, so the numbers are identical by construction, not by luck.

## What it reports

### Supply concentration

| Verdict | Roughly |
|---|---|
| 🔴 **High** | The top 10 hold a majority of supply, or one wallet holds an outsized share of it |
| 🟡 **Mid** | Meaningful concentration, but short of that |
| 🟢 **Low** | Neither |

Plus the raw numbers: holder count, top 10 %, top 20 %, and the largest single
wallet.

Note this is **owner-level**, not account-level. On Solana one person can hold a
token across many token accounts; aggregating by owner is the difference between
"800 holders" and "800 accounts belonging to 300 people".

### Wallet clusters (bubbles)

This is the interesting part.

Ten wallets holding 3% each looks like healthy distribution. Ten wallets holding
3% each that were **all funded by the same address twenty minutes before launch**
is one wallet holding 30% wearing a hat.

The analysis traces how each significant holder was funded and when it first
became active, then groups wallets that trace back to the same origin. Each
cluster is reported with its combined percentage, its wallet count, and *why* it
formed.

**Evidence strength matters.** Some links are strong evidence of one operator;
others are circumstantial, because plenty of legitimate infrastructure touches
many wallets. Weak links are held to a higher bar before they form a cluster at
all, and they can't push the risk verdict to High on their own.

Known exchange wallets are excluded outright: everyone who bought on Coinbase
shares a funding source, and that isn't a bubble. Any list of known exchange
wallets is best-effort, so there's a behavioural backstop as well — an address
that has funded thousands of wallets is infrastructure, not a deployer. (A
chain that runs its own exchange is the exception that proves the rule: on
Robinhood Chain, a wallet labelled "Robinhood" is the chain's own plumbing, so
that name is not treated as an exchange signal *there* while still counting
everywhere else.)

**Sharing a funder is worth less on some chains than others.** Where a chain is
fronted by one app, nearly every wallet on it was funded through the same
bridge or on-ramp — so "these ten holders share a funder" describes the chain,
not a bubble. Those groups are dropped rather than shown as weak clusters.

What survives that is *how* the funding landed: wallets paid out of the same
address **in one block**, or for **byte-identical amounts**, are coordinated no
matter how busy the funder is. When a group carries one of those fingerprints,
the cluster is built from exactly the wallets that share it — so you get the
three wallets that were actually batched, not the thirty that used the same
bridge.

Proximity in time is deliberately *not* treated as evidence: a busy on-ramp
funds strangers continuously, so any window wide enough to catch a careful
operator also fires on unrelated wallets.

### Bubble risk

🔴 **High** / 🟡 **Mid** / 🟢 **Low**, derived from how much supply sits inside
those clusters and how strong the evidence behind them is.

The card also shows total connected supply, and separately how much of it rests
on strong evidence — so you can see when a scary-looking number is mostly weak
inference.

**One exception: our own token.** The largest wallet group on `$DON` is the
project treasury — supply held back for scheduled burns and for future partner
and KOL allocations, not a whale cluster positioned to exit. It is drawn on the
map exactly like any other group, at its real size, labelled **project
treasury**, and it is the one group left out of the bubble-risk grade. The card
says so in place: the grade never appears without the line telling you how much
supply was excluded from it.

### Launch signals

Who was around when the pool opened:

| Signal | Meaning |
|---|---|
| 🌱 **Fresh** | Wallets whose first-ever activity is around this token's launch |
| 🎯 **Snipers** | Bought in the earliest transactions after the pool opened |
| 📦 **Bundle** | Buys landing together — coordinated, not coincidental |
| 👤 **Insiders** | Wallets funded by the token's own creator |

Where the size of the launch cohort is known, snipers and bundles are shown as
`launch% → now%`. That arrow is the whole story: `40% → 4%` means they dumped;
`40% → 38%` means they're still sitting on it.

### Wallet quality

The top holders (LP excluded) bucketed by total portfolio value — whales, mids,
and everything below. A holder base made entirely of tiny wallets gets flagged
for paper-hand risk: nothing there is a conviction position.

### Security

Where the data is available, contract security checks are layered on — mint
authority, blacklist functions, rug ratio, and the big one:

> ⛔ **HONEYPOT — sells are blocked. Do not buy.**

If that's on the card, it's the first line, and nothing else on the card matters.

## Chain coverage

| Chain | Coverage |
|---|---|
| **Solana** | Full — owner aggregation, funding traces, clusters, snipers, bundles, insiders |
| **Ethereum / Base** | Full — same output, resolved through a different data path |
| **BSC** | Partial — cluster evidence is thinner than on the chains above |
| **Robinhood Chain** | Partial — clusters, concentration, fresh wallets and insiders all work; snipers and bundles are not available |
| **Arbitrum** | Partial — same shape as Robinhood Chain. Concentration, wallet quality and shared-funder clusters all work; the behavioural tags (snipers, bundles) come from a source with no Arbitrum coverage, so those rows are absent |
| **Mantle** | Partial — same shape as Arbitrum. Concentration, wallet quality and shared-funder clusters all work; the behavioural tags (snipers, bundles) come from a source with no Mantle coverage, so those rows are absent |
| **Arc** | Partial — same shape as Arbitrum and Mantle. Concentration, wallet quality and shared-funder clusters all work; the behavioural tags (snipers, bundles) come from a source with no Arc coverage, so those rows are absent. The transfer graph runs on Circle's primary Arc endpoint out of the box; Arc's private mainnet phase makes that endpoint permissioned, so on a deployment it does not recognise those rows report as unmeasured rather than wrong. Wallet values are in USDC, Arc's native gas token |

Every chain returns the same shape of result, which is why the Telegram card, the
web panel and the bubble map all work unchanged across chains.

**A signal that couldn't be measured is left out, not reported as zero.** Where
a chain has no source for snipers or bundles, those rows are absent from the
card rather than showing `0%` — an absent row means "not checked here", and a
`0%` row means "checked, and there were none". They are not the same claim, and
on a launch the difference matters.

## Why it's behind a button

A full holder scan is expensive — it means walking the entire holder set and then
tracing the history of each significant wallet to find where its funding came
from. That's orders of magnitude more work than reading a chart, and running it
on every `/don` would exhaust the day's capacity by lunchtime.

So: on demand only, and results are cached per token for a while, so tapping the
button twice in five minutes gives you the same answer without paying twice.

It's also **budget-aware end to end**. If a data source is close to its ceiling,
the analysis degrades to a partial result rather than failing — and any hiccup
anywhere in the pipeline degrades to "unknown" rather than crashing. The button
always answers with something.

## What it deliberately doesn't expose

You get the significant holders — address, percentage and role tags — and, for
the full view, what's needed to draw the map. You don't get the complete holder
set or the internals behind the verdicts.

That's enough to render the visualisation and check the work. It isn't enough to
reconstruct the analysis, or to use the panel as a free data pipe.
