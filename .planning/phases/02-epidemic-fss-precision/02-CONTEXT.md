# Phase 2 Context: Epidemic FSS precision

**Gathered:** 2026-06-23

## Goal

Fourth seed Crosscheck protocol CONFIRMED — bond percolation FSS on Erdős–Rényi graphs (ν ≈ 1 mean-field).

## Baseline (default settings)

```
SEEDS_PER_N=5, SIZES=[200,500,1000,2000,5000], MEAN_DEGREE=6
Fitted nu = 0.239, R² = 0.62, error vs 1.0 = 76.1%
RESULT: INCONCLUSIVE
```

## Prior art in repo

Habitat FSS pass (#298): `TRIALS_PER_P=350`, signed `fit_nu()` when all p_c < p_c(∞). Same pattern likely applies:
- Increase `SEEDS_PER_N` and/or graph instances per N
- Signed log-log fit on p_c(∞) − p_c(N) ~ N^(−1/ν)
- Fixed-input regression test once stable

## Files

- `repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py`
- `protocols-catalog/.../p-b-percolation-epidemiology-fss.yaml`
- Colab path (networkx) — verify after Python CONFIRMED

## Constraints

- `networkx` required — CI already installs it in crosscheck-repro.yml
- Runtime budget: largest N=5000; sweep before committing heavy defaults
- Browser demo may not exist — Colab is demo tier

## Success

- `RESULT: CONFIRMED` at documented tolerance
- Regression test in `test_crosscheck_repro_regression.py`
- CI grep in `crosscheck-repro.yml`