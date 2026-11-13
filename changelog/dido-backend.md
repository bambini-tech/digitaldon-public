# Changelog — DiDo backend

Tags: `dido-backend/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

## [0.13.1] - 2026-11-13

- Arc is switched on for trading in DiDo.

## [0.13.0] - 2026-11-13

- Arc joins the networks DiDo trades on: buy Arc tokens with USDC on Arc, or
  with the ETH you hold on Robinhood Chain.

## [0.12.0] - 2026-11-13

- Buy a token on Base or Ethereum with the ETH you hold on Robinhood Chain,
  in one signature. If the purchase cannot complete, your
  deposit is refunded on the network that paid.
- The token is checked for a way back out on its own network before you
  sign, as for any buy.

## [0.11.0] - 2026-11-13

- Trade one token for another in a single transaction: pay for a token with
  another token you hold, or take a sale's proceeds in a token, from $5.
- The same 1 % fee, charged once, and the token you receive is checked for a
  way back out before you sign.

## [0.10.0] - 2026-11-13

- Quotes now state the route's own fee alongside DiDo's, so the full cost of
  a trade can be shown before it is confirmed.

## [0.9.0] - 2026-11-12

- Trades can use automatic slippage (tighter on networks with a public
  mempool) or your own setting from 0.1 % to 20 %.
- A buy's quote now says how much selling right back would return, so a
  token that keeps a lot on every trade (a tax or a thin pool) is visible
  before you buy.

## [0.8.3] - 2026-11-12

- Trading in DiDo works again on Robinhood Chain, Ethereum and Base after
  a change at our swap provider.

## [0.8.2] - 2026-11-12

- No visible change yet: groundwork for trading through Relay's current
  contracts.

## [0.8.1] - 2026-11-10

- No visible change: groundwork for trading on Ethereum and Base in DiDo.

## [0.8.0] - 2026-11-10

- DiDo's trading service is ready for Ethereum and Base next to Robinhood
  Chain.

## [0.7.2] - 2026-11-10

- No visible change for DiDo's users.

## [0.7.1] - 2026-11-10

- Security updates to DiDo's trading service.

## [0.7.0] - 2026-11-10

- No visible change for DiDo's users.

## [0.6.2] - 2026-11-09

- Fewer "no way to trade this" answers on fresh Solana tokens.

## [0.6.1] - 2026-11-09

- No visible change: groundwork for DiDo's first test trades.

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
