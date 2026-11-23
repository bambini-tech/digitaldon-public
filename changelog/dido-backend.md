# Changelog — DiDo backend

Tags: `dido-backend/vX.Y.Z`. Versioned independently of the other components; see `versions.json` for the current set.
Each release lists what changed for users and integrators.

## [0.31.0] - 2026-11-23

- Internal changes only.

## [0.30.0] - 2026-11-22

- Buy a token on Robinhood Chain, Base, Ethereum or Arc with SOL or USDC
  from your Solana wallet, delivered to your EVM wallet, in one
  transaction.

## [0.29.0] - 2026-11-22

- Internal changes only.

## [0.28.0] - 2026-11-22

- Buy a Solana token with ETH or USDC from Robinhood Chain, Base, Ethereum or
  Arc, delivered to your Solana wallet, in one transaction.

## [0.27.1] - 2026-11-20

- Internal changes only.

## [0.27.0] - 2026-11-19

- DiDo's holder beta: hold 10,000,000 $DON in up to three wallets, prove it
  with one free signature, and trade from any wallet. Holdings are checked
  again every few hours, with two days of grace if they dip below the line.

## [0.26.0] - 2026-11-18

- Your DiDo trade history is now available to your wallet: every buy and
  sell with what paid for it, where, its value, fee and transaction.

## [0.25.1] - 2026-11-17

- More headroom for trading when many people trade at once.

## [0.25.0] - 2026-11-17

- Where trading is offered is kept up to date automatically.

## [0.24.0] - 2026-11-17

- Trading is not offered in sanctioned and excluded regions. DiDo's analysis
  stays open everywhere; the trade sheet says so before a wallet is
  connected.

## [0.23.1] - 2026-11-16

- Buying a token on another network with USDC on Arc works.

## [0.23.0] - 2026-11-16

- When many people trade at once, a routing service at its limit is skipped
  for a moment and the other one quotes, instead of the quote failing.
- Buying with USDC on Arc works again, on Arc and into other networks.

## [0.22.0] - 2026-11-16

- A trade no longer stops with "Trading is paused" when one routing service
  is busy: the other one is checked and used.
- Fewer calls to the routing services per quote, so quotes stay available
  when many people trade at once.

## [0.21.0] - 2026-11-16

- The trade sheet's details now show which routing services were compared
  for your trade, and why the other one was not used.

## [0.20.1] - 2026-11-16

- The second routing service is cleared for use on six networks; it starts
  comparing prices on your trades once switched on.

## [0.20.0] - 2026-11-16

- Every trade on the same network now compares two routing services and
  takes the one that gives you more, about 0.15 % more on most trades
  recorded. If one service is down, the other still trades.

## [0.19.0] - 2026-11-15

- Tokens you bought in DiDo now show their profit and loss on the home's
  wallet card, once you sign in with your wallet.
- The gas top-up on a cross-chain buy now says when it is a standard amount
  because today's gas price could not be read.

## [0.18.0] - 2026-11-15

- Buying on Arc from another network can now include a little USDC for
  network fees, so you can sell later without topping up first.
- When no trade route can be found, the trade sheet now says why.

## [0.17.0] - 2026-11-15

- Sell a token and be paid out in USDC on another network, in one
  transaction. If the payout fails, the proceeds come back on the token's
  network.

## [0.16.0] - 2026-11-15

- A cross-chain buy can now be paid with a token you hold on another
  network, swapped and sent in one transaction.

## [0.15.0] - 2026-11-15

- A cross-chain buy can now be paid with the stablecoin you hold on another
  network, not only its own coin.
- Gas for later: a cross-chain buy into a network where you hold too little
  of its coin to sell can bring some along, sized from that network's
  current gas price.

## [0.14.1] - 2026-11-14

- Listing your tokens never slows down wallet scans.

## [0.14.0] - 2026-11-13

- DiDo can list the tokens you hold on a network, so you pick the one to pay
  with or be paid in rather than pasting its address.

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
