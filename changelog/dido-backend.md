# Changelog — DiDo backend

Tags: `dido-backend/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

## [0.6.0] - 2026-10-29

- DiDo's trading service now names the two networks it trades at launch,
  Solana and Robinhood Chain.

## [0.5.0] - 2026-10-14

- DiDo's trading service now tells the terminal which networks it trades
  and how to add them to your wallet.

## [0.4.0] - 2026-10-14

- Safer trade records in DiDo's backend: a trade can no longer be blocked
  or misrecorded by someone else, and a trade that takes unusually long to
  land is flagged for a person to check. Trading is not open yet.

## [0.3.0] - 2026-10-13

- More groundwork for trading in DiDo: secure, encrypted storage for your
  DiDo trade history, and sign-in with your wallet so only you can see your
  own trade records. Nothing changes for users yet.

## [0.2.0] - 2026-10-08

- More groundwork for trading in DiDo: the supported chains and safe amount
  handling. Nothing changes for users yet.

## [0.1.0] - 2026-10-08

- Groundwork for DiDo's own backend. Nothing changes for users yet.
