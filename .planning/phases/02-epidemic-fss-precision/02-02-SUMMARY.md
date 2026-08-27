# 02-02 Summary: Epidemic regression + CI gate

**Completed:** 2026-06-23

## One-liner

Fixed-input epidemic FSS regression test and CI `RESULT: CONFIRMED` grep gate mirror habitat/cluster/ising.

## Shipped

- `test_epidemic_fss_fit_confirmed_on_reference_pcs()` in `test_crosscheck_repro_regression.py`
- Reference pcs from 2026-06-23 CONFIRMED run (GIANT_FRAC_TARGET=0.145, SEEDS=15, TRIALS=50)
- `crosscheck-repro.yml`: epidemic step uses `tee` + `grep -q "RESULT: CONFIRMED"`

## Verification

- `pytest -k epidemic` passes
- `build_crosscheck.py --apply` + `--check` green (artifact sync for 02-03)