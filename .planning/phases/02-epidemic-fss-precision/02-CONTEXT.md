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

## Decisions (research-locked 2026-08-26)

These lock research findings so Phase 2 is a methodology pass (precedent: cluster-exponent 01-03), not a trophy hunt for ν = 1 with a supercritical estimator.

- **D-01** Theoretical `PC_INF = 1.0 / MEAN_DEGREE` (Poisson ER / Newman T_c). Do not use `pcs[-1]`. Do not use 1/(k−1) unless the generator is switched to k-regular (it is not).
- **D-02** Critical estimator: bisect until mean giant fraction `S ≥ N^(-1/3)`. Do not keep `S ≥ 0.5` (that is a supercritical isosurface at p* ≈ 0.231 with no FSS).
- **D-03** `NU_THEORY = 3.0` (volume FSS ν̄ = d_u ν = 6 × 1/2). Rewrite protocol YAML so the catalog does not claim |Δp| ~ N^{-1/ν} with ν = 1. Document chemical-distance ν = 1 vs volume ν̄ = 3. Do not relabel 3 as 1.
- **D-04** Signed habitat-style `fit_nu(sizes, pcs) -> (nu, r2, sign_ok)`. For ER, approach is from above: `deltas = [pc - PC_INF]`, `sign_ok = all(d > 0)`. `passed = sign_ok and rel_err <= NU_TOLERANCE`.
- **D-05** Average giant fraction across `SEEDS_PER_N` graphs at each bisection mid (habitat average-then-bisect). Use `nx.fast_gnp_random_graph`. Lazy-import networkx so `fit_nu` loads in pytest without networkx installed.
- **D-06** Sweep `SEEDS_PER_N` starting at 20 (try 40 if signs mix). Do not start at 350. Keep `SIZES` including N=5000. Keep `NU_TOLERANCE = 0.25` unless the sweep is stable enough to tighten to 0.15.
- **D-07** Add CI grep only after a documented local run prints `RESULT: CONFIRMED`. Freeze that run's mean p_c vector into `test_epidemic_fss_fit_confirmed_on_reference_pcs`. Do not re-simulate ER graphs in pytest.
- **D-08** After YAML experimental_design / statistical_analysis_plan / runtime / exponent edits: `python scripts/build_crosscheck.py --apply`. Leave other seeds' YAML `status: executed`. Epidemic may flip to `confirmed` in the same PR if Python CONFIRMED.

### Claude's Discretion
- Exact `SEEDS_PER_N` after the timed sweep
- Susceptibility-peak fallback only if N=5000 sign-check fails
- Whether to pin `networkx>=3.0` in the CI pip line

### Deferred Ideas
- Marketing, DNS, arXiv, catalog waves
- Browser/JS runner for epidemic
- Phase 4 unified CONFIRMED gates for all protocols