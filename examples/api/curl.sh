#!/usr/bin/env sh
# DigitalDon Analysis API from the shell. Full reference: docs/using/api.md
set -eu
API=https://api.digitaldon.net

# The contract: free to read. Chains, depths and prices are in here.
curl -s "$API/v1/openapi.json" | head -c 400; echo

# The first basic call per IP per UTC day is free: see a real response.
curl -s -X POST "$API/v1/analyze" \
  -H 'Content-Type: application/json' \
  -d '{"token": "BONK", "chain": "sol", "depth": "basic"}'
echo

# After that, the same call answers 402 with the payment requirements in the
# PAYMENT-REQUIRED header (base64). Paying needs a signature, so use an x402
# client library: see python/ next to this file.
curl -s -i "$API/v1/analyze?token=BONK" | head -n 20
