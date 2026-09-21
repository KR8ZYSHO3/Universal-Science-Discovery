# Backlog scout

Generated **2026-09-21 19:07 UTC**. Operations only — not a scientific result.

Findings: **4**. New issues this run (cap 5): 4.

Agents: pick `status:needs-owner` issues first, then this list, then ROADMAP.md.
Do not promote Wave Factory. Do not invent CONFIRMED.

## WORK-01 still open — Crosscheck RESULT writes through

`usdr-scout:fingerprint=d0a51a74ffe4` · roadmap · normal

v1.3 item **WORK-01** is on ROADMAP.md and has no shipped hint file (`scripts/apply_crosscheck_result.py`).

Crosscheck RESULT writes through

Open a PR that satisfies the success criteria in `.planning/ROADMAP.md`. Do not market. Do not auto-confirm science.

## UI-01 still open — Hub first-visit audit (counts, links, no broken loads)

`usdr-scout:fingerprint=44030059a091` · roadmap · normal

v1.3 item **UI-01** is on ROADMAP.md and has no shipped hint file (`none`).

Hub first-visit audit (counts, links, no broken loads)

Open a PR that satisfies the success criteria in `.planning/ROADMAP.md`. Do not market. Do not auto-confirm science.

## ROBUST-01 still open — One ordered maintainer command list

`usdr-scout:fingerprint=9ac0b612793c` · roadmap · normal

v1.3 item **ROBUST-01** is on ROADMAP.md and has no shipped hint file (`none`).

One ordered maintainer command list

Open a PR that satisfies the success criteria in `.planning/ROADMAP.md`. Do not market. Do not auto-confirm science.

## Protocols have no last_run_result (hub will not show last run)

`usdr-scout:fingerprint=1efc82621bd2` · last-run · normal

WORK-01 write-through is missing on:

- `p-b-habitat-percolation-ecology-cluster-exponent (status=executed)`
- `p-b-habitat-percolation-ecology-fss (status=executed)`
- `p-b-percolation-epidemiology-fss (status=confirmed)`
- `p-b-percolation-oncology-gcc (status=ready)`
- `p-b-ising-social-dynamics-ewi (status=executed)`

Run the canonical Python, then:
`python scripts/apply_crosscheck_result.py --protocol ID --from-stdout run.txt --apply --refresh-hub`
Do not set `status: confirmed` from this bot.

## Opened this run

- https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues/326
- https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues/327
- https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues/328
- https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues/329
