#!/usr/bin/env python3
"""
Call the DigitalDon Analysis API and pay for it over x402, in USDC on Solana.

    python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
    export SOLANA_PRIVATE_KEY=...   # base58, the format Phantom exports
    .venv/bin/python analyze.py BONK holders

How a payment works: call the URL and get a 402 listing what we accept. Sign
an authorization for one of those with your wallet, then call the SAME URL
again with it in the PAYMENT-SIGNATURE header. We verify it, run the analysis,
and only then settle. A failed or incomplete scan is never charged.

Use a throwaway wallet holding a little USDC on Solana. The key is read from
the environment and never printed. To pay on Base instead, register x402's
EVM client scheme for "eip155:8453" in build_client(); the rest is identical.
"""

from __future__ import annotations

import os
import sys
from urllib.parse import urlencode

import requests
from solders.keypair import Keypair
from x402 import x402ClientSync
from x402.http import x402HTTPClientSync
from x402.mechanisms.svm.exact import ExactSvmClientScheme
from x402.mechanisms.svm.signers import KeypairSigner

API = os.getenv("DIGITALDON_API", "https://api.digitaldon.net")
SOLANA_RPC = os.getenv("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")
SOLANA_MAINNET = "solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp"


def build_client() -> x402HTTPClientSync:
    secret = os.getenv("SOLANA_PRIVATE_KEY", "").strip()
    if not secret:
        sys.exit("Set SOLANA_PRIVATE_KEY (base58, as Phantom exports it).")
    signer = KeypairSigner(Keypair.from_base58_string(secret))
    client = x402ClientSync()
    client.register(SOLANA_MAINNET, ExactSvmClientScheme(signer, rpc_url=SOLANA_RPC))
    return x402HTTPClientSync(client)


def analyze(token: str, depth: str = "basic", chain: str = "auto") -> dict:
    url = f"{API}/v1/analyze?" + urlencode({"token": token, "depth": depth, "chain": chain})

    resp = requests.get(url, timeout=60)
    if resp.status_code == 402:
        http = build_client()
        headers, _ = http.handle_402_response(dict(resp.headers), resp.content, url)
        resp = requests.get(url, headers=headers, timeout=120)
        if resp.ok:
            receipt = http.get_payment_settle_response(resp.headers.get)
            print(f"paid: tx {receipt.transaction} on {receipt.network}", file=sys.stderr)
    # 200 without a 402 first is the daily free call.

    body = resp.json()
    if not body.get("ok"):
        sys.exit(f"[{resp.status_code}] {body.get('error')}: {body.get('detail')}")
    return body["data"]


def main() -> None:
    token = sys.argv[1] if len(sys.argv) > 1 else "BONK"
    depth = sys.argv[2] if len(sys.argv) > 2 else "basic"
    data = analyze(token, depth)

    a = data["analysis"]
    print(f"{data['token']['symbol']} on {data['token']['chain']}  "
          f"(schema {data['schema_version']}, engine {data['engine_version']})")
    if a.get("available"):
        print(f"score {a['score']}/100: {a['score_label']}")
    else:
        print(f"no chart read yet ({a.get('state')}); on-chain: {data['onchain']}")
    for w in data.get("warnings", []):
        print(f"warning: {w}")
    if data.get("holders"):
        print("holders block present")


if __name__ == "__main__":
    main()
