# Backlog scout

Generated **2026-09-26 11:59 UTC**. Operations only — not a scientific result.

Findings: **4**. New issues this run (cap 5): 0.

Agents: pick `status:needs-owner` issues first, then this list, then ROADMAP.md.
Do not promote Wave Factory. Do not invent CONFIRMED.

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
- `p-b-ising-social-dynamics-ewi (status=executed)`

Run the canonical Python, then:
`python scripts/apply_crosscheck_result.py --protocol ID --from-stdout run.txt --apply --refresh-hub`
Do not set `status: confirmed` from this bot.

## 2 orphan unknowns in the knowledge graph

`usdr-scout:fingerprint=5756d9b8fa6d` · orphans · normal

Unknowns with no bridge/hypothesis edge. Prime contribution targets, not auto-generated bridges.

- `u-gap-improved-survival-with-ipilimumab-in-pat-f8b52b71`
- `u-gap-lifetime-prevalence-and-age-of-onset-dis-e040267e`

`python scripts/find_orphan_unknowns.py`
