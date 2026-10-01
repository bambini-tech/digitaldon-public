# Adding it to a group

Getting the bot into a group and flipping its switches is covered in
[Setting it up](setup.md). This page is what it actually does once it's there.

## Auto-scan: the short card

Someone pastes a contract address in the chat. The bot answers with a **short
card**:

* header — token, chain, price, market cap
* the score
* both trade horizons with their estimated upside
* two buttons — **📊 TA Analysis** and **👥 Holder Scan**

That's it. Deliberately.

Every other scanner bot answers the same trigger with a full-size card, which is
why busy groups end up as walls of bot output with a conversation occasionally
visible between them. The short card fits three in a row without pushing the chat
off screen — and it still shows entry and exit zones, which nobody else posts at
all.

Tap **📊 TA Analysis** and you get the whole card, chart included.

Tap **👥 Holder Scan** and you get the holder and wallet-cluster report on its
own, without opening the full card first — the distribution, the wallet quality
and the funder-based cluster map. That is the question most groups actually have
about a freshly pasted contract ("is the supply bundled?"), and it no longer
costs a full TA card and a chart render to get to it. The short card stays where
it is, so the other button still works afterwards.

The Holder Scan button only appears where the scan can actually run: Solana
always, EVM chains when the cluster engine is enabled for them.

### Three details that matter in practice

**Old cards keep working.** Auto-scan cards sit in the scrollback for hours or
days, and the button on one of them still works long after it was posted. There's
no session to expire and nothing to go stale.

**Expanding an old card shows current numbers.** Tapping a six-hour-old card runs
a fresh analysis at the moment you tap it, rather than replaying the numbers from
when it was posted. That's the honest thing for a card that may have been sitting
there all night.

**Repeats are deduped.** The same token pasted again in the same chat within a
short window (a minute, by default) doesn't get a second card. The check runs
*before* a rate-limit slot is spent, so a repeated mention costs the group
nothing.

## Fresh launches are not auto-scanned

A token that deployed twenty minutes ago has no chart to analyse. Auto-scan
passes it over in silence — no card, and no "skipped, too fresh" reply either,
which would just be the same noise with different words.

There is a mode that answers those tokens as well, with a different card: no
score and no entry/exit zones — those would be invented — but the on-chain read
instead. It is **reserved for the bot owner** and cannot be switched on for a
group. Two reasons, and the second is the one that decides it:

* That card is the thinnest thing the bot posts, and it is still being reworked.
* Every minutes-old contract pasted anywhere costs an upstream lookup, and every
  group draws on the **same** API budget. One busy chat pasting ten deploys an
  hour would spend what the rest of the groups need.

Two things stay unaffected:

* **`/don <address>` always answers**, fresh launch or not. Auto-scan governs
  what the bot says on its own, never what it does when it's asked.
* **A token is still recorded as a call** even when no card is posted, so `/pnl`
  and the [leaderboard](leaderboard.md) know who was first regardless.

And what looks fresh isn't always: an **older** token that has barely traded
since it launched still gets its card, so a dormant contract waking up is never
silently swallowed.

## The other two group features

| Feature | Command | Page |
|---|---|---|
| 🃏 **PNL cards** | `/pnl <contract>` | [PNL cards](pnl-cards.md) |
| 🏆 **Leaderboard** | `/lb` | [Leaderboard](leaderboard.md) |

Both are on by default and both are one admin tap from off.

They share a source: every `/don` in a group registers the **first** scan of a
token in that chat, credited to whoever ran it. PNL cards read one row of that
record; the leaderboard ranks all of it.

## Rate limits in groups

Groups have their own windows on top of the per-user ones — **8 scans per minute
and 120 per hour** by default.

The per-minute one exists because Telegram itself throttles a bot at roughly 20
messages per minute per group, and one full analysis writes several times (status
message, edits, chart). That ceiling bites first, whatever else is going on.

The per-hour one exists because nothing else caps a *group*: thirty active
members each with their own hourly allowance could sustain hundreds of scans an
hour in one chat and crowd every other group out. It deliberately leaves bursts
alone — it bounds the sustained rate, which is the part that actually causes
harm.

DMs are exempt from both, so anyone can always keep scanning privately.

## When auto-scan stays quiet

In order of likelihood:

1. **The bot isn't an admin.** Telegram's privacy mode means a non-admin bot
   never receives ordinary group messages. Use the `🔄 Check admin rights` button
   on the setup card, or `/setup` to reopen it.
2. **Auto-scan is off.** `/setup`, or `/autoscan on`.
3. **The token is too fresh to analyse.** Auto-scan skips tokens with no chart
   history; use `/don`, which always answers.
4. **The group is rate limited.** Wait it out, or scan in a DM.
