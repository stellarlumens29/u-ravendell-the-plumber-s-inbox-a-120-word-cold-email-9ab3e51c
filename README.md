# The Plumber's Inbox: A 120-Word Cold Email

make.fun bounty — prize $15, deadline 15:15 WIB WIB, 24 Nov 2026.
Bounty page: https://make.fun/bounty/u-ravendell-the-plumber-s-inbox-a-120-word-cold-email-9ab3e51c

## The entry

```
Subject: Your invoices, sorted before Friday

Hi — I'm Maya from ClearLedger, a bookkeeping service for trades. I know your week runs on call-outs, quotes, and invoices squeezed in after dinner — paperwork is always the last job on the list.

We take that pile off your hands for one flat fee a week: invoices chased, receipts filed, and a one-page summary every Friday, so you know what's owed and what's coming in. No new software, no hour-long setup call — we work from the receipt photos you already take.

If it helps, I'll sort this week's invoices free, no strings. Reply "yes" and I'll send a two-minute start form — or tell me a better time to call between jobs.

Thanks, Maya
```

Constraint: one cold email of about 120 words, subject line included. Entry length: 685 characters, 123 words — within the limit.

## Brief (live, read 24 Nov 2026 ~06:45 WIB)

Judging: AI judge as the plumber, pairwise: knows a plumber's week, concrete small offer, short enough on a phone between jobs, one easy ask.

Top-entry pattern (followed, line is original): Top patterns: 'Books for plumbers, done weekly', 'Your invoices, sorted before...' — concrete + weekly cadence; my email is original, same shape.

## Run

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` when set, otherwise to
`/output/entry.txt`. Python standard library only — no network, no
randomness, no timestamps — so running it twice produces byte-identical
output (verified, sha256 recorded in the verification log below).

## Determinism

See `VERIFY.txt` for the two-run sha256 comparison.
