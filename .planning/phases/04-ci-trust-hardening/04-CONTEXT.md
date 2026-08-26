# Phase 4: CI & trust hardening - Context

**Gathered:** 2026-08-26 (plan-phase; no discuss-phase — locked from ROADMAP.md, REQUIREMENTS.md, PROJECT.md Ship Bar, Phase 2 freeze, and Phase 3 handoff)
**Status:** Ready for planning

<domain>
## Phase Boundary

Make regression coverage match the **shipped** Crosscheck surface: every protocol whose Python stdout is `RESULT: CONFIRMED` stays gated in `.github/workflows/crosscheck-repro.yml`, and `tests/repo_smoke` covers epidemic plus the new script entry points from Phase 3 (`generate_crosscheck.py`, oncology GCC repro).

This is a **CI + smoke** phase, not a fifth CONFIRMED trophy hunt and not a catalog-status cleanup.

Out of scope: marketing, DNS, arXiv, catalog content waves, Phase 5 hub recommendations, feeding execution results into hypothesis validation, unified percolation toolkit, in-browser JS, retuning epidemic FSS, flipping habitat/cluster/Ising YAML `status` to `confirmed`.
</domain>

<decisions>
## Implementation Decisions

### Locked Decisions

- **D-01 (TRUST-02 gate token):** Gate **stdout** `RESULT: CONFIRMED`, not YAML `status: confirmed`. Today habitat FSS, cluster exponent, and Ising YAML remain `status: executed` while their Python prints `RESULT: CONFIRMED`. Epidemic YAML is `confirmed`. Oncology GCC YAML is `ready` and prints `INCONCLUSIVE`. Do **not** mass-edit YAML status as a unification stunt.
- **D-02 (keep the four greps):** `crosscheck-repro.yml` already tees+greps `RESULT: CONFIRMED` for habitat FSS, cluster exponent, epidemic FSS, and Ising EWI. Keep all four. Do not drop epidemic. Do not replace live CI runs of those four with pytest-only pins.
- **D-03 (no fake fifth CONFIRMED):** `repro/p-b-percolation-oncology-gcc/giant_component_fraction.py` always prints `RESULT: INCONCLUSIVE` and exits 0. **Never** add `grep -q "RESULT: CONFIRMED"` for GCC. If GCC is run in CI or pytest, assert `RESULT: INCONCLUSIVE` and exit code 0.
- **D-04 (unified means inventory, not a trophy):** TRUST-02 “unified CONFIRMED gates” means a **maintainable mapping** so a future CONFIRMED protocol cannot silently skip CI. Researcher/planner pick the mechanism (workflow matrix from a checked-in list, a small Python inventory check in repo_smoke that diffs catalog/repro vs the workflow YAML, or both). The inventory must treat **expected stdout token** as the source of truth, not YAML `status`.
- **D-05 (epidemic freeze):** Do not change `epidemic_percolation_fss.py` constants, freeze `mean_pcs` in `test_epidemic_fss_fit_confirmed_on_reference_pcs`, or `NU_THEORY = 3.0`. No live NetworkX / ER Monte Carlo in pytest. Do not shop a prettier R².
- **D-06 (TRUST-03 epidemic):** Epidemic freeze pytest **already exists** in `tests/repo_smoke/test_crosscheck_repro_regression.py`. Do not duplicate it. TRUST-03 “covers epidemic” is closed by keeping that test and asserting `NU_THEORY == 3.0` still holds.
- **D-07 (TRUST-03 generate_crosscheck):** Add a **fast** repo_smoke for `scripts/generate_crosscheck.py`. Happy path: `--bridge b-percolation-oncology --dry-run` (or another existing bridge). Assert exit 0 and a `p-b-` id on stdout. **No `--write`** (must not dirty the worktree). No networkx. Must stay well under 30s.
- **D-08 (TRUST-03 GCC entry point):** Add repo_smoke for `giant_component_fraction.py`. Prefer actually running the stdlib script (L=32, TRIALS=8 is cheap) and asserting `RESULT: INCONCLUSIVE` plus exit 0. Do not add a fake freeze-fit of CONFIRMED numbers. Do not copy cluster’s live `collect_pooled_sizes()` anti-pattern into new tests.
- **D-09 (where tests run):** New pytest lives in `tests/repo_smoke/` and is picked up automatically by `.github/workflows/validate-schemas.yml` (`python -m pytest tests/repo_smoke -v`). Do **not** duplicate the pytest bundle inside `crosscheck-repro.yml`.
- **D-10 (workflow path filters):** `crosscheck-repro.yml` currently triggers on `repro/**`, `protocols-catalog/**`, and Crosscheck build scripts — **not** `tests/repo_smoke/**`. That is OK for CONFIRMED greps. If 04-01 adds a helper script used by the workflow, include that script in the workflow `paths:` list. Do not add `generate_crosscheck.py` as a fifth CONFIRMED job.
- **D-11 (honesty docs):** Update `docs/CROSSCHECK.md` (parity / CI column) so it states CONFIRMED-only grep policy: four seeds grepped CONFIRMED; GCC is INCONCLUSIVE and must not be grepped CONFIRMED. After any hub HTML change: `python scripts/build_crosscheck.py --apply` then `--check`. Prefer docs-only if the hub already links the manifesto.
- **D-12:** No marketing, DNS, arXiv, catalog waves, JS runners, promote CLI, or Phase 5 recommendations.
- **D-13:** No fabricated `RESULT: CONFIRMED`. GSD artifacts are process metadata, not scientific evidence.
- **D-14:** ROADMAP plan split: **04-01** unified CONFIRMED gates in CI (TRUST-02); **04-02** repo_smoke expansion (TRUST-03). They may run as independent waves if they do not share files; if both edit `docs/CROSSCHECK.md`, serialize that file to one plan or one trailing docs task.

### Claude's Discretion

- Exact TRUST-02 inventory mechanism (matrix job vs pytest that parses `.github/workflows/crosscheck-repro.yml` vs a tiny `scripts/` helper). Prefer the smallest change that fails CI when a CONFIRMED stdout protocol is missing from the workflow.
- Whether GCC also runs as a named step in `crosscheck-repro.yml` (INCONCLUSIVE grep) **in addition to** pytest, or pytest-only.
- Which `--bridge` id the generate dry-run uses.
- Whether 04-01 and 04-02 are parallel Wave 1 or sequential.

### Deferred Ideas

- Feeding execution results YAML back into hypothesis validation (`docs/CROSSCHECK.md` internal “Phase 3”)
- Unified percolation toolkit (`docs/CROSSCHECK.md` internal “Phase 4”)
- HUB-01 smart recommendations (GSD Phase 5)
- In-browser JS for epidemic FSS
- Raising epidemic freeze R² / retuning `SEEDS_PER_N`
- Changing habitat / cluster / Ising YAML `status` from `executed` to `confirmed`
</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### CI & smoke
- `.github/workflows/crosscheck-repro.yml` — four `tee` + `grep -q "RESULT: CONFIRMED"` jobs
- `.github/workflows/validate-schemas.yml` — `python -m pytest tests/repo_smoke -v`
- `tests/repo_smoke/test_crosscheck_repro_regression.py` — frozen-input fits including epidemic `NU_THEORY = 3.0`
- `tests/repo_smoke/test_crosscheck_artifacts.py` — `build_crosscheck.py --check`
- `tests/repo_smoke/test_catalog_regression.py` — subprocess script smokes

### Phase 3 surface that must now be covered
- `scripts/generate_crosscheck.py` — `--dry-run` / `--write` / `--bridge`
- `repro/p-b-percolation-oncology-gcc/giant_component_fraction.py` — always `RESULT: INCONCLUSIVE`, exit 0
- `docs/CROSSCHECK.md` — generate path + Run-mode parity matrix (CI grep column)

### Freeze / honesty
- `.planning/phases/02-epidemic-fss-precision/02-01-SUMMARY.md` — CONFIRMED_FREEZE mean_pcs
- `.planning/phases/03-crosscheck-scale-up/03-01-SUMMARY.md` — no 5th CONFIRMED grep
- `.planning/PROJECT.md` — Ship Bar
- `LEGAL.md` / `docs/METHODOLOGY.md` — no fabricated claims
</canonical_refs>

<specifics>
## Specific Ideas

ROADMAP listed plans (keep unless split needed):
- 04-01: Unified CONFIRMED gates in CI
- 04-02: repo_smoke expansion
</specifics>

<deferred>
## Deferred Ideas

See Decisions → Deferred Ideas. Do not plan them.
</deferred>

---

*Phase: 04-ci-trust-hardening*
*Context gathered: 2026-08-26 via plan-phase (no discuss-phase)*
