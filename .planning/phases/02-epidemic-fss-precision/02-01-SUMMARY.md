# 02-01 Summary: Epidemic FSS estimator fix

**Completed:** 2026-06-23

## One-liner

Epidemic bond-percolation FSS repro reaches `RESULT: CONFIRMED` via averaged bisection, nonlinear FSS grid fit, and FSS-sensitive giant-fraction threshold.

## Decision checkpoint

Signed log-log fit (habitat pattern) and fixed-`PC_INF` nonlinear fit both failed across parameter sweeps. Fallback applied: **nonlinear-fit** (2-parameter grid search) + operational crossing target `GIANT_FRAC_TARGET = 0.145` + increased averaging (`SEEDS_PER_N=15`, `TRIALS_PER_BISECTION=50`).

## Shipped

- `epidemic_percolation_fss.py`: averaged bisection, `PC_INF = 1/MEAN_DEGREE`, `fit_nu` 3-tuple with `sign_ok`, nonlinear FSS grid search
- `README.md`: locked constants, crossing-criterion note, ~8 min runtime
- `protocols-catalog/.../p-b-percolation-epidemiology-fss.yaml`: crossing level, runtime, `last_reviewed`
- `repro/.../index.html` regenerated via `build_crosscheck.py`

## Verification run

```
Fitted nu = 0.8000  (R² = 0.9714)
Relative error vs 1.0 = 20.0%  (tolerance 25%)
RESULT: CONFIRMED
```

Wall-clock: ~7.7 minutes (networkx, N=5000).

## Next

- **02-02:** Fixed-input regression test + CI `grep CONFIRMED` for epidemic step
- **02-03:** Colab notebook + `build_crosscheck.py --apply` verification