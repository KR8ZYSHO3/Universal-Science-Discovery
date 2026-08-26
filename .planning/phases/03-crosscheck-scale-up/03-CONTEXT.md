# Phase 3 Context: Crosscheck scale-up

**Gathered:** 2026-08-26 (plan-phase; no discuss-phase — locked from ROADMAP.md, REQUIREMENTS.md, PROJECT.md Ship Bar, and Phase 2 handoff)
**Status:** Ready for planning

<domain>
## Phase Boundary

Make the path **bridge YAML → `generate_crosscheck.py` → `drafts/crosscheck/` → human-promoted `protocols-catalog/` → `repro/` bundle** repeatable for a bridge that is not one of the four seed protocols. Document Python vs browser vs Colab outcome tiers for every existing seed.

This is a **pipeline + honesty** phase, not a fifth CONFIRMED trophy hunt.

Out of scope: marketing, DNS, arXiv, catalog content waves, Phase 4 unified CI greps for every protocol, Phase 5 hub recommendations, feeding execution results into hypothesis validation (that numbering in `docs/CROSSCHECK.md` is a different roadmap).
</domain>

<decisions>
## Implementation Decisions

### Locked Decisions

- **D-01 (CROSS-06 generate):** Run `python scripts/generate_crosscheck.py --bridge <id> --write` for **≥1 bridge that currently has zero files in `protocols-catalog/`**. Document the exact command and output paths in `docs/CROSSCHECK.md`. Do not use `--all` as the documented happy path (too noisy). Habitat already has two seed protocols — it does not count as the "new bridge."
- **D-02 (CROSS-06 promote):** Promote **≥1** generated draft into `protocols-catalog/` after filling every TODO (`null_hypothesis`, `statistical_analysis_plan`, honest `experimental_design`). Human review remains the merge gate — do not auto-promote. Status may be `draft` or `ready`. **Do not set `status: confirmed` unless a real local run printed `RESULT: CONFIRMED`.** Prefer `ready` or `executed`.
- **D-03 (repro path):** The phase goal requires the path through a **repro bundle**. Add `repro/<protocol-id>/` with README + runnable script (stdlib preferred). Script must print a `RESULT:` line and **exit 0 always** (Phase 2 contract). If the science is not yet a precision pass, print `INCONCLUSIVE` honestly. Do **not** add a fifth `grep RESULT: CONFIRMED` job — that is Phase 4 TRUST-02.
- **D-04 (no trophy hunt):** Do not start another FSS / exponent precision campaign. Do not copy epidemic's 90-minute Monte Carlo sweep. If the new protocol cannot be a small stdlib demo, ship promoted YAML + a documented local runner, still without claiming CONFIRMED.
- **D-05 (CROSS-07 parity):** Add a parity matrix covering **all four seed protocols** (habitat FSS, cluster exponent, Ising EWI, epidemic FSS). Columns at minimum: protocol id, Python canonical script, browser JS (yes/no + filename), Colab notebook (yes/no), CI grep CONFIRMED (yes/no), RESULT contract (`exit 0`, stdout token). Epidemic is Colab-only (no JS). Habitat/cluster/Ising have JS with lighter demo budgets than Python. State explicitly that **Python is canonical**; browser/Colab are demo tier.
- **D-06 (hub):** Surface the parity matrix from the existing Crosscheck hub section and/or `docs/CROSSCHECK.md` (linked from the hub). Do not redesign the dashboard (Phase 5). After protocol YAML / hub HTML changes: `python scripts/build_crosscheck.py --apply` then `--check`.
- **D-07 (epidemic freeze):** Do not change `epidemic_percolation_fss.py` constants, freeze vector, or `NU_THEORY = 3.0`. Do not shop a prettier R².
- **D-08 (schemas):** New/moved protocol YAML must pass `python scripts/validate_schemas.py`. Generator drafts that stay in `drafts/crosscheck/` are gitignored or committed only if `.gitignore` allows — check before planning; do not fight Wave Factory gitignore patterns.
- **D-09:** No marketing, DNS, arXiv, or new catalog waves. No JS runner for networkx protocols.
- **D-10:** New bridge is `b-percolation-oncology`. Promote **opportunity 1** (giant-component / GCC) as protocol id `p-b-percolation-oncology-gcc` (rename on promote; keep `pollination_index: 1`). Do not use habitat or polymer as the D-01 bridge.
- **D-11:** Parity matrix lives as a section in `docs/CROSSCHECK.md` (not a new file). Hub already links that manifesto.
- **D-12:** Add `drafts/crosscheck/` to `.gitignore`. Do not commit generator TODO YAML.
- **D-13:** Promoted YAML `status: ready` (runnable + documented). Never `confirmed`. `executed` only if the executor actually ran the local script in 03-01.
- **D-14:** Thin **stdlib** lattice demo that prints `RESULT: INCONCLUSIVE` and exits 0. Small L. No JS. No 5th CI grep.
- **D-15:** One-line honesty fix in `generate_repro_index_pages.py` (and habitat FSS README if it still claims exit 1): exit 0 always; inspect stdout. Not a dashboard redesign.
- **D-16:** No new `repo_smoke` for `generate_crosscheck.py` this phase (TRUST-03 is Phase 4).
- **D-17:** No Crosscheck promote CLI — manual copy + fill TODOs + PR is the path. Document it.

### Claude's Discretion

- Which new bridge to generate from (must satisfy D-01). Prefer a desktop-tier opportunity that can share percolation/Ising patterns already in `repro/`.
- Whether the promoted protocol is `draft` vs `ready`.
- Whether the new repro is a thin stdlib demo or README-only plus a `python -c` smoke that the generator output validates.
- Exact filename/location of the parity matrix (`docs/CROSSCHECK.md` section vs `docs/CROSSCHECK_PARITY.md`).
- Whether to add `generate_crosscheck.py` to `tests/repo_smoke` (nice-to-have; TRUST-03 is Phase 4 — only add a **fast** dry-run smoke if it stays <30s and needs no networkx).

### Deferred Ideas

- Feeding execution results YAML back into hypothesis validation (`docs/CROSSCHECK.md` internal "Phase 3")
- Unified percolation toolkit across ecology/epidemiology/oncology (`docs/CROSSCHECK.md` internal "Phase 4")
- TRUST-02 / TRUST-03 CI expansion
- HUB-01 smart recommendations
- In-browser JS for epidemic FSS
- Raising epidemic freeze R²
</decisions>

<canonical_refs>
## Canonical References

### Pipeline
- `scripts/generate_crosscheck.py` — drafts from `cross_pollination_opportunities`
- `docs/CROSSCHECK.md` — manifesto + generate/promote/run loop
- `protocols-catalog/README.md` — status enum
- `schemas/protocol.yaml` — required fields
- `scripts/build_crosscheck.py` — hub/index/explainer regen + `--check`
- `scripts/crosscheck_browser.py` — `BROWSER_RUNNERS` vs Colab

### Seed analogs (Phase 1–2)
- `repro/p-b-habitat-percolation-ecology-fss/` — stdlib + JS
- `repro/p-b-percolation-epidemiology-fss/` — networkx + Colab only
- `.planning/phases/02-epidemic-fss-precision/02-03-SUMMARY.md` — YAML honesty + `--apply`

### Constraints
- `.planning/PROJECT.md` Ship Bar
- `LEGAL.md` / `docs/METHODOLOGY.md` — no fabricated claims
</canonical_refs>

<specifics>
## Specific Ideas

ROADMAP listed plans (keep unless split needed):
- 03-01: Generate + promote protocols for a second bridge
- 03-02: Browser/Colab parity matrix + hub updates
</specifics>

<deferred>
## Deferred Ideas

See Decisions → Deferred Ideas. Do not plan them.
</deferred>

---

*Phase: 03-crosscheck-scale-up*
*Context gathered: 2026-08-26 via plan-phase (no discuss-phase)*
