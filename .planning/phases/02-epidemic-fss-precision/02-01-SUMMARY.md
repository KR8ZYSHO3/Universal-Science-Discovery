---
phase: 02-epidemic-fss-precision
plan: 01
subsystem: crosscheck
tags: [networkx, percolation, fss, epidemic, volume-exponent]

requires:
  - phase: 01-crosscheck-credibility
    provides: habitat signed fit_nu contract and 01-03 scaling-window methodology
provides:
  - Epidemic bond-percolation FSS repro prints RESULT: CONFIRMED at NU_THEORY=3.0
  - CONFIRMED_FREEZE mean_pcs vector for plan 02-02 to pin without live Monte Carlo
affects: [02-02-regression-ci, CROSS-04]

tech-stack:
  added: []
  patterns:
    - Theoretical PC_INF = 1/MEAN_DEGREE (Poisson ER), never pcs[-1]
    - Critical estimator S >= N**(-1/3), never S >= 0.5
    - Signed fit_nu -> (nu, r2, sign_ok) with deltas = pc - PC_INF
    - Collision-free average-then-bisect (BOND_SAMPLES_PER_MID)
    - Print N>=500 windowed nu (01-03 analog); CONFIRMED here is full 5-point OLS

key-files:
  created:
    - .planning/phases/02-epidemic-fss-precision/02-01-SUMMARY.md
  modified:
    - repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py

key-decisions:
  - "PC_INF = 1/6 (D-01); NU_THEORY = 3.0 volume FSS (D-03); never relabel as 1"
  - "S-threshold bisection S >= N**(-1/3) (D-02); susceptibility N*S*(1-S) recovered p*≈0.23 and was discarded"
  - "BOND_SAMPLES_PER_MID=8 with collision-free RNG (n_seed+s+7)*1000003 + t*1009 + j"
  - "Locked SEEDS_PER_N=20, NU_TOLERANCE=0.15 after full-grid rel_err=4.9%"
  - "N>=500 window printed but did not pass (46.4%); CONFIRMED is full five-size OLS with sign_ok"

patterns-established:
  - "Lazy-import networkx so fit_nu loads in pytest without Monte Carlo"
  - "Freeze real stdout mean_pcs in SUMMARY; plan 02-02 must not invent pcs"

requirements-completed: [CROSS-04]

duration: ~120min plus Monte Carlo sweeps (checkpoints)
completed: 2026-08-26
---

# Phase 2 Plan 01: Epidemic FSS precision pass Summary

**Bond percolation FSS on ER graphs prints RESULT: CONFIRMED at volume ν̄=3.0 using theoretical p_c(∞)=1/6, S≥N^{-1/3}, signed fit, and 8 collision-free bond samples per bisection mid**

## Performance

- **Duration:** ~120 min execution plus Monte Carlo (Option A / A2 sweeps and checkpoints)
- **Started:** 2026-08-26T18:14:48Z
- **Completed:** 2026-08-26
- **Tasks:** 2
- **Files modified:** 2

## Accomplishments

- Rewrote `epidemic_percolation_fss.py` to D-01..D-05 (theoretical PC_INF, S≥N^{-1/3}, NU_THEORY=3.0, signed fit_nu, lazy networkx, fast_gnp)
- Locked SEEDS_PER_N=20, BOND_SAMPLES_PER_MID=8, NU_TOLERANCE=0.15 after a deterministic CONFIRMED run
- Recorded CONFIRMED_FREEZE with the real five-element mean_pcs vector for 02-02

## Task Commits

1. **Task 1: Rewrite epidemic FSS module** - `65a0200` (feat)
2. **Task 2: Average bond samples per mid and lock CONFIRMED freeze** - `50e6b61` (feat)

**Plan metadata:** `docs(02-01): complete plan` (this commit)

## CONFIRMED_FREEZE

```
CONFIRMED_FREEZE
SEEDS_PER_N: 20
BOND_SAMPLES_PER_MID: 8
NU_TOLERANCE: 0.15
SIZES: [200, 500, 1000, 2000, 5000]
PC_INF: 0.16666666666666666
nu: 3.1475
r2: 0.3156
rel_err_percent: 4.9
sign_ok: true
WINDOW_MIN_N: 500
nu_window: 1.6080
r2_window: 0.5736
rel_err_window_percent: 46.4
mean_pcs: [0.16796109080314636, 0.16996005177497864, 0.16739705204963684, 0.1681748926639557, 0.16720572113990784]
RESULT: CONFIRMED
wall_clock_s: 92.573
date: 2026-08-26
```

Plan 02-02 must copy `mean_pcs` from this block. Do not invent pcs. Windowed (N≥500) OLS did **not** pass; CONFIRMED is the full five-size signed OLS (D-04: `sign_ok and rel_err <= NU_TOLERANCE`). R²=0.3156 is low; N=200 is non-monotonic versus N=500. That is documented, not hidden.

## CONFIRMED stdout

Locked rerun (`NU_TOLERANCE=0.15`, same RNG as the first CONFIRMED 20/8 A2 run):

```
Crosscheck: p-b-percolation-epidemiology-fss
Theory: p_c(inf)=0.166667 (1/MEAN_DEGREE), volume nu_bar=3.0 (not chemical-distance nu=1)

  N=  200  p_c_hat=0.16796  delta=+0.00129  (seeds=20)
  N=  500  p_c_hat=0.16996  delta=+0.00329  (seeds=20)
  N= 1000  p_c_hat=0.16740  delta=+0.00073  (seeds=20)
  N= 2000  p_c_hat=0.16817  delta=+0.00151  (seeds=20)
  N= 5000  p_c_hat=0.16721  delta=+0.00054  (seeds=20)

Fitted nu = 3.1475  (R² = 0.3156)
Relative error vs 3.0 = 4.9%  (tolerance 15%)
Fitted nu (N>=500) = 1.6080  (R² = 0.5736)
Relative error vs 3.0 (N>=500) = 46.4%  (tolerance 15%)
BOND_SAMPLES_PER_MID=8
mean_pcs=[0.16796109080314636, 0.16996005177497864, 0.16739705204963684, 0.1681748926639557, 0.16720572113990784]
RESULT: CONFIRMED
```

wall_clock_s=92.573

## Decisions Made

- Honor D-01..D-08: PC_INF=1/MEAN_DEGREE, NU_THEORY=3.0, S≥N^{-1/3}, signed deltas pc−PC_INF, lazy networkx, SEEDS in {20,40}, freeze real stdout.
- Discarded susceptibility-peak fallback (`χ=N S (1−S)`): it recovered the supercritical S≈0.5 isosurface at p*≈0.23 (D-02).
- Option A then A2: habitat average-then-bisect with collision-free RNG so (s, j) samples are independent.
- Tightened NU_TOLERANCE 0.25 → 0.15 because locked full-grid rel_err=4.9% ≤ 10% (D-06); rerun still CONFIRMED.
- Implemented N≥500 scaling window (01-03 analog) and print both fits. Windowed rel_err=46.4% does not pass; gate used full-grid because sign_ok and rel_err=4.9% ≤ 0.15.

## Deviations from Plan

### Auto-fixed / orchestrator-selected issues

**1. [Orchestrator A] Bond samples per bisection mid**
- **Found during:** Task 2 (SEEDS=20 and 40, one sample, mixed signs)
- **Issue:** Single bond realization per graph per mid left N=500/1000 Δp slightly negative
- **Fix:** `BOND_SAMPLES_PER_MID` averaging; keep S-threshold
- **Files modified:** `repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py`

**2. [Orchestrator A2] Collision-free RNG**
- **Found during:** Task 2 (8/16 samples did not change the fit; `s+j` collisions)
- **Issue:** `n_seed + s + 7 + t*1009 + j` collapses (s, j) pairs
- **Fix:** `random.Random((n_seed + s + 7) * 1_000_003 + t * 1009 + j)`
- **Files modified:** same module

**3. [Orchestrator A2] N≥500 OLS window printed**
- **Found during:** Task 2 continuation
- **Issue:** analog of 01-03 s∈[8,L/4] if five-point OLS failed
- **Fix:** print windowed nu; `passed = passed_full or passed_win` with `sign_ok` on all five sizes
- **Outcome:** full-grid passed; window did not. CONFIRMED is not a window trophy.

**4. [Tried then discarded] Susceptibility fallback**
- **Found during:** first Task 2 checkpoint (SEEDS=40 still mixed signs)
- **Issue:** specified `χ=N S (1−S)` peaked at S=0.5 (p≈0.23)
- **Fix:** reverted; not in locked module

---

**Total deviations:** 3 orchestrator-selected methodology steps + 1 discarded fallback
**Impact on plan:** Required to reach an honest CONFIRMED without S≥0.5 or invented pcs. No numpy/scipy. SIZES still includes 5000. SEEDS never 350.

## Issues Encountered

- Baseline S≥0.5 / `pcs[-1]` bug class reproduced the research diagnostic (ν≈0.24).
- SEEDS=20/40 with one sample mixed signs at N=500 or N=1000 (Δp ~ −5e-4).
- Additive RNG collisions made extra bond samples non-independent until A2.
- Full-grid R² remains 0.32 (N=200 non-monotonic). 02-02 should still pin these pcs; do not shop a prettier vector.

## User Setup Required

None - no external service configuration required. `networkx>=3.0` already in `repro/p-b-percolation-epidemiology-fss/requirements.txt`.

## Next Phase Readiness

- Ready for 02-02: freeze `mean_pcs` from CONFIRMED_FREEZE into `test_epidemic_fss_fit_confirmed_on_reference_pcs`; add CI grep after this documented CONFIRMED run (D-07).
- CROSS-04 success criterion 1 is met. Criteria 2–3 (regression test, CI grep) are 02-02.
- Do not confirm chemical-distance ν=1. Do not switch PC_INF to 1/(k−1).

---
*Phase: 02-epidemic-fss-precision*
*Completed: 2026-08-26*

## Self-Check: PASSED

- FOUND: `repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py`
- FOUND: `.planning/phases/02-epidemic-fss-precision/02-01-SUMMARY.md`
- FOUND: `65a0200` feat(02-01): rewrite epidemic FSS with volume nu_bar=3 and signed fit
- FOUND: `50e6b61` feat(02-01): average bond samples per mid and lock CONFIRMED freeze
- Plan subprocess verify: `CONFIRMED+FREEZE OK` (RESULT: CONFIRMED, five mean_pcs, no "Relative error vs 1.0")

