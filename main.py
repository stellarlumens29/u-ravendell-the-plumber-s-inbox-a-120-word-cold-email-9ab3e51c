#!/usr/bin/env python3
"""make.fun entry: The Plumber's Inbox: A 120-Word Cold Email.

Writes the entry text deterministically to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt). Python standard library only — no network, no
randomness, no timestamps. Running twice produces byte-identical output.

Bounty: https://make.fun/bounty/u-ravendell-the-plumber-s-inbox-a-120-word-cold-email-9ab3e51c
Constraint: one cold email of about 120 words, subject line included
"""

import hashlib
import os
import sys

ENTRY = 'Subject: Your invoices, sorted before Friday\n\nHi — I\'m Maya from ClearLedger, a bookkeeping service for trades. I know your week runs on call-outs, quotes, and invoices squeezed in after dinner — paperwork is always the last job on the list.\n\nWe take that pile off your hands for one flat fee a week: invoices chased, receipts filed, and a one-page summary every Friday, so you know what\'s owed and what\'s coming in. No new software, no hour-long setup call — we work from the receipt photos you already take.\n\nIf it helps, I\'ll sort this week\'s invoices free, no strings. Reply "yes" and I\'ll send a two-minute start form — or tell me a better time to call between jobs.\n\nThanks, Maya'

LIMIT_CHARS = None


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = (ENTRY + "\n").encode("utf-8")
    if LIMIT_CHARS is not None and len(ENTRY) > LIMIT_CHARS:
        print(f"FAIL: entry is {len(ENTRY)} chars, limit is {LIMIT_CHARS}",
              file=sys.stderr)
        return 1
    with open(out_path, "wb") as f:
        f.write(data)
    print(out_path)
    print("chars:", len(ENTRY))
    print("sha256:", hashlib.sha256(data).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
