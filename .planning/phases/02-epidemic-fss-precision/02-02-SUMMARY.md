---
phase: 02-epidemic-fss-precision
plan: 02
subsystem: crosscheck
tags: [networkx, percolation, fss, epidemic, pytest, ci]

requires:
  - phase: 02-epidemic-fss-precision
    provides: CONFIRMED_FREEZE mean_pcs vector and RESULT: CONFIRMED stdout from plan 01
provides:
  - test_epidemic_fss_fit_confirmed_on_reference_pcs pins freeze mean_pcs without live Monte Carlo
  - crosscheck-repro.yml epidemic step tees stdout and greps RESULT: CONFIRMED
affects: [02-03-colab, CROSS-04, TRUST-03]

tech-stack:
  added: []
  patterns:
    - Frozen-input fit_nu regression (habitat analog); no estimate_pc / er_graph in pytest
    - CI tee+/tmp/*.out then grep -q RESULT: CONFIRMED (habitat/cluster/Ising contract)
    - NU_THEORY asserted as 3.0 in pytest, never 1.0

key-files:
  created:
    - .planning/phases/02-epidemic-fss-precision/02-02-SUMMARY.md
  modified:
    - tests/repo_smoke/test_crosscheck_repro_regression.py
    - .github/workflows/crosscheck-repro.yml

key-decisions:
  - "Copied mean_pcs verbatim from 02-01-SUMMARY CONFIRMED_FREEZE; did not invent or shop a prettier vector"
  - "Assert NU_THEORY == 3.0 (D-03); grep RESULT: CONFIRMED only because 02-01 already documented it (D-07)"
  - "Single existing pip install networkx; no second pip install; no timeout-minutes; pytest stays in validate-schemas.yml"

patterns-established:
  - "Epidemic pytest loads epidemic_percolation_fss via _load_module and calls only fit_nu"
  - "Epidemic CI step name Epidemic percolation FSS (expect CONFIRMED)"

requirements-completed: [CROSS-04]

duration: 2min
completed: 2026-08-26
---

# Phase 2 Plan 02: Epidemic FSS regression + CI gate Summary

**Frozen-input epidemic ν regression pins 02-01 CONFIRMED_FREEZE mean_pcs (SEEDS_PER_N=20, 2026-08-26) and CI greps RESULT: CONFIRMED; no live NetworkX in pytest**

## Performance

- **Duration:** 2 min
- **Started:** 2026-08-26T18:50:23Z
- **Completed:** 2026-08-26T18:52:00Z
- **Tasks:** 2
- **Files modified:** 2 (plus this SUMMARY and planning metadata)

## Accomplishments

- Added `test_epidemic_fss_fit_confirmed_on_reference_pcs` that calls `fit_nu` on the freeze vector and asserts `NU_THEORY == 3.0`, `sign_ok`, and `rel_err <= NU_TOLERANCE`
- Gated `crosscheck-repro.yml` epidemic step with `tee /tmp/epidemic.out` + `grep -q "RESULT: CONFIRMED"` after documented local CONFIRMED (D-07)
- Pytest passed in 0.02s without importing networkx or running Monte Carlo

## Task Commits

1. **Task 1: Add frozen-pcs epidemic fit regression test** - `48ee4a2` (test)
2. **Task 2: Gate epidemic CI step on RESULT: CONFIRMED** - `295d85f` (feat)

**Plan metadata:** `docs(02-02): complete plan` (this commit)

## Frozen pin (must match 02-01-SUMMARY CONFIRMED_FREEZE)

Comment in `tests/repo_smoke/test_crosscheck_repro_regression.py`:

```
# Reference mean p_c(N) at SEEDS_PER_N=20, SIZES including 5000
# (2026-08-26 CONFIRMED run; see 02-01-SUMMARY.md CONFIRMED_FREEZE).
```

Copied `mean_pcs` (verbatim, five floats):

```
pcs = [
    0.16796109080314636,
    0.16996005177497864,
    0.16739705204963684,
    0.1681748926639557,
    0.16720572113990784,
]
```

Freeze metadata from 02-01: `SEEDS_PER_N: 20`, `date: 2026-08-26`, `RESULT: CONFIRMED`, `nu: 3.1475`, `rel_err_percent: 4.9`, `NU_TOLERANCE: 0.15`. R²=0.3156 remains low; N=200 is non-monotonic versus N=500. This plan did not shop a prettier vector.

## Files Created/Modified

- `tests/repo_smoke/test_crosscheck_repro_regression.py` — frozen-input epidemic `fit_nu` regression; reuses `_load_module`; no `estimate_pc` / `er_graph` / `giant_fraction` / `networkx`
- `.github/workflows/crosscheck-repro.yml` — epidemic step renamed `Epidemic percolation FSS (expect CONFIRMED)`; tee + grep; still exactly one `pip install` mentioning networkx

## Decisions Made

- Copy freeze `mean_pcs` character-for-character from 02-01-SUMMARY; zero placeholders forbidden (D-07).
- `assert mod.NU_THEORY == 3.0` (volume FSS); asserting 1.0 would be D-03.
- Add CI grep only because 02-01-SUMMARY already contains `RESULT: CONFIRMED`.
- Do not add a second `pip install`; leave `pip install networkx` as the existing Install dependencies step.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Ready for 02-03: Colab/notebook path verified or documented; YAML honesty.
- CROSS-04 success criteria 1–3 are met (CONFIRMED stdout, frozen pytest, CI grep).
- Do not confirm chemical-distance ν=1. Do not replace freeze pcs with a live Monte Carlo in pytest.

## Verification

- `python -m pytest tests/repo_smoke/test_crosscheck_repro_regression.py::test_epidemic_fss_fit_confirmed_on_reference_pcs -q` → `1 passed in 0.02s`
- Workflow YAML python-c asserts → `ci epidemic grep OK`

---
*Phase: 02-epidemic-fss-precision*
*Completed: 2026-08-26*

## Self-Check: PASSED

- FOUND: `tests/repo_smoke/test_crosscheck_repro_regression.py`
- FOUND: `.github/workflows/crosscheck-repro.yml`
- FOUND: `.planning/phases/02-epidemic-fss-precision/02-02-SUMMARY.md`
- FOUND: `48ee4a2` test(02-02): pin epidemic FSS fit_nu on CONFIRMED freeze pcs
- FOUND: `295d85f` feat(02-02): gate epidemic CI step on RESULT: CONFIRMED
- Plan subprocess verify: pytest 1 passed in 0.02s; `ci epidemic grep OK`

