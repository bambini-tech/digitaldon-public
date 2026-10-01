# API examples

- [`curl.sh`](curl.sh): read the contract, make the free daily call, see the 402.
- [`python/analyze.py`](python/analyze.py): the full paid round trip over x402
  (USDC on Solana), with its own `requirements.txt`.

Any x402 client library works; the protocol and its clients for other
languages are at [github.com/x402-foundation/x402](https://github.com/x402-foundation/x402).
The response shape is in [`../../api/openapi.json`](../../api/openapi.json),
including three complete worked responses.
