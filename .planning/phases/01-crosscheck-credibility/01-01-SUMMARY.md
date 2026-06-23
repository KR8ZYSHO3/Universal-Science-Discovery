# 01-01 Summary: FSS + Ising precision passes

**Completed:** 2026-06-22 (PRs #297, #298)

## One-liner

Habitat percolation FSS and Ising EWI repros reach CONFIRMED via increased trials and signed/monotonic fit gates.

## Shipped

- `simulate_percolation_fss.py`: TRIALS_PER_P=350, signed ν fit
- `ising_critical_slowing.py` + JS: γ fit in scaling regime
- Protocol YAML + hub artifacts regenerated

## Verification

- CI greps `RESULT: CONFIRMED` for FSS and Ising
- Regression tests in `test_crosscheck_repro_regression.py`