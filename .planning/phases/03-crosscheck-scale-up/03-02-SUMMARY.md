---
phase: 03-crosscheck-scale-up
plan: 02
subsystem: crosscheck
tags: [parity-matrix, generate_crosscheck, hub, exit-code, mkdocs]

requires:
  - phase: 03-crosscheck-scale-up
    provides: Promoted p-b-percolation-oncology-gcc (status ready) and INCONCLUSIVE stdlib repro
provides:
  - Run-mode parity section in docs/CROSSCHECK.md (four seeds plus GCC)
  - Documented generate command --bridge b-percolation-oncology --write
  - Honest exit-0 landings via generate_repro_index_pages.py + habitat FSS README
  - Hub #run-mode-parity link, oncology explainer, fifth hub card
affects: [CROSS-07, Phase 4 TRUST-02]

tech-stack:
  added: []
  patterns:
    - Parity matrix lives in docs/CROSSCHECK.md ## Run-mode parity (not CROSSCHECK_PARITY.md)
    - Python is canonical; browser and Colab are demo tier
    - Generated landings: Exit code is always 0; inspect stdout for CONFIRMED vs INCONCLUSIVE
    - Static hub section-desc is outside @hub-crosscheck-grid markers; --apply preserves it

key-files:
  created:
    - repro/p-b-percolation-oncology-gcc/index.html
    - dashboard/explainers/b-percolation-oncology.html
  modified:
    - docs/CROSSCHECK.md
    - scripts/generate_repro_index_pages.py
    - repro/p-b-habitat-percolation-ecology-fss/README.md
    - dashboard/index.html
    - CHANGELOG.md
    - README.md
    - mkdocs.yml

key-decisions:
  - "D-11: parity is a section in docs/CROSSCHECK.md, not a new file"
  - "D-05: columns protocol id | Python canonical | browser JS | Colab | CI grep CONFIRMED | RESULT contract"
  - "D-15: generator + habitat FSS README match return 0 always (inspect stdout)"
  - "D-06: hub links #run-mode-parity; no new widget"
  - "D-01: happy-path write is --bridge b-percolation-oncology --write, not --all"

patterns-established:
  - "build_crosscheck.py --apply then --check after YAML or generator changes; never hand-edit generated HTML"
  - "Oncology GCC is local-only INCONCLUSIVE — not a fifth CI CONFIRMED grep"

requirements-completed: [CROSS-06, CROSS-07]

duration: 4min
completed: 2026-08-26
---

# Phase 3 Plan 02: Run-mode parity and exit-code honesty Summary

**CROSSCHECK manifesto documents `--bridge b-percolation-oncology --write`, a five-row D-05 parity matrix (Python canonical; browser/Colab demo), honest exit-0 landings, and a hub link to `#run-mode-parity`**

## Performance

- **Duration:** 4 min
- **Started:** 2026-08-26T19:37:32Z
- **Completed:** 2026-08-26T19:41:37Z
- **Tasks:** 2
- **Files modified:** 16 (plus 2 generated creates)

## Accomplishments

- Documented the generate/promote happy path: `python scripts/generate_crosscheck.py --bridge b-percolation-oncology --write` → `drafts/crosscheck/physics-oncology/`; manual copy + PR (no promote CLI)
- Authored `## Run-mode parity` covering all four seed ids plus `p-b-percolation-oncology-gcc` with D-05 columns
- Fixed generator + habitat FSS README exit-code lie; `--apply` stamped `Exit code is always 0` on all five repro landings
- Hub static Crosscheck blurb links `#run-mode-parity`; fifth card is **Run repro** for oncology GCC; `b-percolation-oncology.html` explainer generated
- `build_crosscheck.py --check`, `validate_schemas.py`, and `mkdocs build --strict` pass; four CI CONFIRMED greps and `NU_THEORY = 3.0` unchanged

## Task Commits

Each task was committed atomically:

1. **Task 1: Document generate/promote happy path and D-05 parity matrix in CROSSCHECK.md** - `aaeff9f` (docs)
2. **Task 2: Fix exit-code honesty, hub parity link, --apply/--check, changelog** - `528a1e0` (fix)

**Plan metadata:** `docs(03-02): complete run-mode parity plan` (this commit)

## Files Created/Modified

- `docs/CROSSCHECK.md` - generate command, drafts path, catalog table, Run-mode parity, manual promote, GSD vs manifesto Phase 3 note
- `scripts/generate_repro_index_pages.py` - landing sentence `Exit code is always 0`
- `repro/p-b-habitat-percolation-ecology-fss/README.md` - Ising-style exit-0 honesty
- `dashboard/index.html` - `#run-mode-parity` link + regenerated fifth hub card
- `repro/p-b-percolation-oncology-gcc/index.html` - generated Pages landing
- `dashboard/explainers/b-percolation-oncology.html` - generated explainer
- `repro/*/index.html` (four seeds) - honest exit sentence from `--apply`
- `CHANGELOG.md` / `README.md` - four CI-gated seeds plus INCONCLUSIVE GCC demo
- `mkdocs.yml` - omitted steward/outreach pages added to nav (strict-mode unblock)

## Decisions Made

- Parity is a section in `docs/CROSSCHECK.md` (D-11); file `docs/CROSSCHECK_PARITY.md` does not exist
- Python is canonical; browser and Colab are demo tier (stated as the first sentence of Run-mode parity)
- Oncology GCC is not in `BROWSER_RUNNERS`, has no Colab, and has no CI CONFIRMED grep
- Manifesto roadmap Phase 3/4 (results YAML / unified toolkit) are not GSD Phase 3

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] mkdocs --strict omitted-file warning**
- **Found during:** Task 2 (`mkdocs build --strict`)
- **Issue:** Four tracked docs pages were not in `mkdocs.yml` nav (`STEWARDS_CHARTER.md`, `outreach/CROSSCHECK_LAUNCH_STORY.md`, `outreach/LAUNCH_DAY_ACTIONS.md`, `outreach/READY_TO_POST.md`). Pre-existing; blocked the required verify.
- **Fix:** Added those pages to nav (same pattern as earlier strict-mode nav commits).
- **Files modified:** `mkdocs.yml`, `CHANGELOG.md`
- **Verification:** `mkdocs build --strict` exit 0
- **Committed in:** `528a1e0` (Task 2 commit)

---

**Total deviations:** 1 auto-fixed (1 blocking)
**Impact on plan:** Required for `--strict`. No Crosscheck scope creep. Did not add a 5th CI grep, promote CLI, or epidemic freeze change.

## Issues Encountered

- `gsd-sdk` is not on PATH and not in `node_modules`; STATE/ROADMAP/REQUIREMENTS updated by hand to match executor handlers.
- `scripts/sync-dashboard-from-state.py --dry-run` emits an empty canvas snapshot because `.planning/STATE.md` does not use the canvas section headers; did not apply (would wipe `canvases/Progress.canvas.tsx`).

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- CROSS-07 parity matrix is public; CROSS-06 generate command is documented
- Phase 4 can add TRUST-02 CONFIRMED gates without treating oncology GCC as a fifth trophy
- Do not add epidemic JS; do not change `NU_THEORY = 3.0`

## Verification snippets

Task 1 asserts: generate command, `drafts/crosscheck/physics-oncology/`, `Run-mode parity`, five protocol ids, `CI grep CONFIRMED`, no `--all --write`, no `docs/CROSSCHECK_PARITY.md`.

`--check`: `OK: Crosscheck artifacts match protocols-catalog/` (5 protocols)

`validate_schemas.py`: 5 crosscheck protocols

`mkdocs build --strict`: Documentation built

CI: exactly four `grep -q "RESULT: CONFIRMED"`; `percolation-oncology` not in workflow; `NU_THEORY = 3.0` in `epidemic_percolation_fss.py`.

---

**Total deviations:** 1 auto-fixed
**Impact on plan:** MkDocs nav only

## Self-Check: PASSED

- FOUND: `docs/CROSSCHECK.md`, `scripts/generate_repro_index_pages.py`, habitat FSS README, `dashboard/index.html`, oncology `index.html` + explainer, `03-02-SUMMARY.md`
- FOUND: commits `aaeff9f`, `528a1e0`
- `docs/CROSSCHECK_PARITY.md` absent; `git ls-files drafts/crosscheck` empty; no `scripts/promote_crosscheck.py`
- CROSS-07 marked complete in REQUIREMENTS.md

---
*Phase: 03-crosscheck-scale-up*
*Completed: 2026-08-26*
