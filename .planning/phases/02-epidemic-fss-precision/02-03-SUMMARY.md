---
phase: 02-epidemic-fss-precision
plan: 03
subsystem: crosscheck
tags: [networkx, percolation, fss, epidemic, volume-exponent, colab, catalog]

requires:
  - phase: 02-epidemic-fss-precision
    provides: Epidemic bond-percolation FSS repro prints RESULT: CONFIRMED at NU_THEORY=3.0
provides:
  - Epidemic protocol YAML status confirmed with volume nu_bar=3 matching the CONFIRMED script
  - Colab notebook still runs python epidemic_percolation_fss.py
  - Generated hub/index/explainer aligned via build_crosscheck.py --apply
affects: [CROSS-04, CROSS-05, 03-02-parity]

tech-stack:
  added: []
  patterns:
    - Catalog YAML experimental_design/stats/runtime match the canonical Python script
    - Colab notebook is clone-and-run of epidemic_percolation_fss.py, not a JS runner
    - Generated repro/index.html and hub/explainer come only from build_crosscheck.py --apply

key-files:
  created:
    - .planning/phases/02-epidemic-fss-precision/02-03-SUMMARY.md
  modified:
    - protocols-catalog/physics-epidemiology/p-b-percolation-epidemiology-fss.yaml
    - repro/p-b-percolation-epidemiology-fss/README.md
    - repro/p-b-percolation-epidemiology-fss/run_crosscheck.ipynb
    - repro/p-b-percolation-epidemiology-fss/index.html
    - dashboard/explainers/b-percolation-epidemiology.html
    - dashboard/index.html

key-decisions:
  - "Copied locked SEEDS_PER_N=20, NU_TOLERANCE=0.15, BOND_SAMPLES_PER_MID=8 from 02-01-SUMMARY CONFIRMED_FREEZE"
  - "Epidemic YAML status confirmed because 02-01 printed RESULT: CONFIRMED; habitat/cluster/Ising left executed (D-08)"
  - "Catalog fit target is volume nu_bar=3 with S >= N^(-1/3) and p_c(inf)=1/6; never relabeled as nu=1 (D-03)"
  - "Colab still invokes !python epidemic_percolation_fss.py; no BROWSER_RUNNERS entry"

patterns-established:
  - "Protocol YAML signed log-linear OLS, not NLS or 10-seed bootstrap"
  - "README Exit code 0 always; inspect stdout for CONFIRMED vs INCONCLUSIVE"

requirements-completed: [CROSS-04]

duration: 3min
completed: 2026-08-26
---

# Phase 2 Plan 03: Epidemic catalog + Colab honesty Summary

**Epidemic protocol YAML, README, Colab notebook, and generated hub landing now describe signed volume-FSS (nu_bar=3, p_c(inf)=1/6, S≥N^{-1/3}) with status confirmed; Colab still runs `epidemic_percolation_fss.py`**

## Performance

- **Duration:** 3 min
- **Started:** 2026-08-26T18:54:40Z
- **Completed:** 2026-08-26T18:57:26Z
- **Tasks:** 3
- **Files modified:** 6 (plus this SUMMARY and planning metadata)

## Accomplishments

- Rewrote `p-b-percolation-epidemiology-fss.yaml` to signed log-linear volume FSS with `status: confirmed`, `nu_bar = 3`, `p_c(inf)=1/6`, `S >= N^(-1/3)`, locked `SEEDS_PER_N=20` / `NU_TOLERANCE=15%` / `BOND_SAMPLES_PER_MID=8`
- Documented Colab as the demo tier: README `Exit code 0 always`; notebook markdown no longer claims mean-field ν ≈ 1; code cells still `!python epidemic_percolation_fss.py`
- Regenerated `repro/p-b-percolation-epidemiology-fss/index.html`, hub grid, and explainer via `python scripts/build_crosscheck.py --apply`; `--check` green

## Task Commits

1. **Task 1: Rewrite epidemic protocol YAML to match the signed volume-FSS script** - `48bfdbe` (docs)
2. **Task 2: Document Colab path and honest README; fix notebook exponent claim** - `1f1ed9d` (docs)
3. **Task 3: Regenerate Crosscheck artifacts from YAML** - `52789dc` (chore)

**Plan metadata:** `docs(02-03): complete plan` (this commit)

## Locked freeze copied from 02-01-SUMMARY

```
SEEDS_PER_N: 20
BOND_SAMPLES_PER_MID: 8
NU_TOLERANCE: 0.15
RESULT: CONFIRMED
wall_clock_s: 92.573
```

YAML `status: confirmed` because plan 01 already printed `RESULT: CONFIRMED`. Colab cells still call the canonical script (`!pip install -q -r requirements.txt` then `!python epidemic_percolation_fss.py`).

## Files Created/Modified

- `protocols-catalog/physics-epidemiology/p-b-percolation-epidemiology-fss.yaml` — catalog matches script (volume nu_bar=3, signed OLS)
- `repro/p-b-percolation-epidemiology-fss/README.md` — run command, exit-code honesty, Colab demo tier
- `repro/p-b-percolation-epidemiology-fss/run_crosscheck.ipynb` — markdown exponent claim only
- `repro/p-b-percolation-epidemiology-fss/index.html` — generated from YAML (not hand-edited)
- `dashboard/explainers/b-percolation-epidemiology.html` — generated explainer title
- `dashboard/index.html` — hub grid title

## Decisions Made

- Copied freeze integers from 02-01 CONFIRMED_FREEZE; did not invent seeds or tolerance
- Epidemic status may be confirmed; did not batch-upgrade habitat/cluster/Ising (still `executed`)
- No JS browser runner; networkx is not stdlib and epidemic stays out of `BROWSER_RUNNERS`
- `estimated_runtime` uses measured ~90 s (freeze wall_clock_s=92.573) rather than the plan template "under 1 minute"

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing Critical] Honest estimated_runtime from freeze wall clock**
- **Found during:** Task 1 (YAML rewrite)
- **Issue:** Plan template said `under 1 minute` for SEEDS_PER_N=20, but 02-01 freeze recorded wall_clock_s=92.573
- **Fix:** Set `estimated_runtime: about 90 seconds on a modern laptop (SEEDS_PER_N=20 by default)`. Did not restore `3–8 minutes`
- **Files modified:** `protocols-catalog/physics-epidemiology/p-b-percolation-epidemiology-fss.yaml`
- **Verification:** YAML python -c checks + `validate_schemas.py`
- **Committed in:** `48bfdbe` (Task 1)

**2. [Rule 2 - Missing Critical] Document BOND_SAMPLES_PER_MID=8 in experimental_design**
- **Found during:** Task 1 (D-08 match the script)
- **Issue:** Plan YAML template averaged S across graphs only; locked script averages 8 collision-free bond samples per mid
- **Fix:** Experimental-design bullet names 20 graphs and 8 independent bond samples per graph
- **Files modified:** same YAML
- **Verification:** freeze values appear as concrete numbers (`20`, `15%`, `8`)
- **Committed in:** `48bfdbe` (Task 1)

**3. [.cursor/rules documentation-and-dashboard] CHANGELOG Unreleased + consultant handoff**
- **Found during:** Plan metadata
- **Issue:** Merge-worthy catalog/hub change requires CHANGELOG Unreleased and optional handoff
- **Fix:** Added Unreleased epidemic FSS catalog note; refreshed `.planning/handoffs/GROK_CONSULTANT_LATEST.md`
- **Files modified:** `CHANGELOG.md`, `.planning/handoffs/GROK_CONSULTANT_LATEST.md`
- **Verification:** Unreleased section names nu_bar=3 and status confirmed
- **Committed in:** plan metadata commit

---

**Total deviations:** 3 auto-fixed (2 missing critical honesty, 1 documentation-hub rule)
**Impact on plan:** Catalog matches the locked CONFIRMED script. CHANGELOG/handoff required by always-apply hub rules.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required. Optional hosted Colab click is manual; automated substitute is the notebook cell grep.

## Next Phase Readiness

- Phase 2 plans 01–03 complete. CROSS-04 catalog/hub now match stdout CONFIRMED
- Habitat/cluster/Ising YAML remain `executed` (D-08); not a 02-03 job
- Ready for Phase 3 (Crosscheck scale-up) or `/gsd-verify-work 2`
- Generated `index.html` may still mention shared generator "exit code 1" sentence; do not edit `generate_repro_index_pages.py` in this phase

---
*Phase: 02-epidemic-fss-precision*
*Completed: 2026-08-26*

## Self-Check: PASSED

- FOUND: `protocols-catalog/physics-epidemiology/p-b-percolation-epidemiology-fss.yaml`
- FOUND: `repro/p-b-percolation-epidemiology-fss/README.md`
- FOUND: `repro/p-b-percolation-epidemiology-fss/run_crosscheck.ipynb`
- FOUND: `repro/p-b-percolation-epidemiology-fss/index.html`
- FOUND: `.planning/phases/02-epidemic-fss-precision/02-03-SUMMARY.md`
- FOUND: `48bfdbe` docs(02-03): rewrite epidemic protocol YAML for volume nu_bar=3
- FOUND: `1f1ed9d` docs(02-03): document Colab path and nu_bar=3 in README and notebook
- FOUND: `52789dc` chore(02-03): regenerate Crosscheck artifacts from epidemic YAML
- Plan verifies: yaml strings OK; readme+notebook OK; `python scripts/build_crosscheck.py --check` OK; `python scripts/validate_schemas.py` OK; `pytest tests/repo_smoke/test_crosscheck_artifacts.py` 1 passed
