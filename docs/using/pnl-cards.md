# PNL cards

```
/pnl <contract>
```

Groups only. Renders a shareable image showing **the group's first scan of that
token versus its peak since**.

## What it's for

Someone drops a contract in the group at $180K market cap. Four days later it's
at $2.1M and everyone remembers it differently. `/pnl` settles it: the bot
recorded the first scan, so the card is receipts, not vibes.

The card shows:

* the token
* market cap at first scan → all-time high since that moment
* the multiple, large and unmissable
* who scanned it first
* the contract address

## How the record works

When `/don` runs inside a group, the bot stores the **first** scan of each token
per chat — market cap and price at that moment, plus who ran it.

Only the first. Later scans of the same token in the same group never overwrite
it, so the credit always belongs to whoever actually called it, not whoever
scanned it most recently. Each group has its own record for a token; your group's
first call is your group's.

The same record feeds the [leaderboard](leaderboard.md), which ranks every caller
in the group by what their calls did.

## Turning it off

The 🃏 **PNL cards** switch in the group setup card. Admins only, on by default.
See [Setting it up](setup.md).

With it off, `/pnl` stays silent in that group.
