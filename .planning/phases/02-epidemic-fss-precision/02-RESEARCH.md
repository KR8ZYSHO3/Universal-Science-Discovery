# Phase 2: Epidemic FSS precision — Research

**Researched:** 2026-06-23
**Domain:** Bond percolation FSS on Erdős–Rényi graphs (networkx)
**Confidence:** HIGH

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- Fourth seed protocol must reach `RESULT: CONFIRMED` at documented tolerance (ν ≈ 1, 25% relative error)
- Python canonical; Colab is demo tier (verify after Python CONFIRMED)
- `networkx` required — CI already installs in `crosscheck-repro.yml`
- Runtime budget: largest N=5000; sweep before committing heavy defaults
- Must tie to WORK-01 (outcome reflected in CI/tests), not isolated tuning

### Claude's Discretion
- Exact `SEEDS_PER_N`, `TRIALS_PER_BISECTION`, bisection depth
- Whether to use fixed `PC_INF = 1/MEAN_DEGREE` vs joint fit (protocol allows nonlinear fit)
- Whether to add monotonicity gate on p_c(N) vs N

### Deferred Ideas (OUT OF SCOPE)
- Browser runner for epidemic (no repro JS today)
- Hub outcome badges (Phase 5 / WORK-01 UI slice)
- Marketing / outreach copy updates
</user_constraints>

<research_summary>
## Summary

Baseline `epidemic_percolation_fss.py` prints `RESULT: INCONCLUSIVE` (ν≈0.24, 76% off theory). Root cause is **estimator noise**, not missing seeds alone: `estimate_pc()` uses a **single bond-percolation realization per bisection step**, while habitat FSS (`simulate_percolation_fss.py`) averages `TRIALS_PER_P` crossing trials at each bisection midpoint. With flat noisy p_c(N)≈0.23, the log-log fit on `abs(pc - pcs[-1])` yields meaningless ν.

**Primary recommendation:** Port habitat's averaged-bisection pattern to epidemic, use theoretical `PC_INF = 1.0 / MEAN_DEGREE`, add signed `fit_nu()` with `sign_ok`, increase `SEEDS_PER_N` to ≥10 per protocol statistical plan, sweep parameters locally, lock defaults that print `RESULT: CONFIRMED`, then add fixed-input regression + CI grep (mirror Phase 1 #298).
</research_summary>

<standard_stack>
## Standard Stack

| Component | Role |
|-----------|------|
| `networkx` | ER graph + connected components |
| `epidemic_percolation_fss.py` | Canonical repro |
| `simulate_percolation_fss.py` | Reference FSS pattern (TRIALS_PER_P, signed fit) |
| `test_crosscheck_repro_regression.py` | Fixed-input fit regression |
| `crosscheck-repro.yml` | CI CONFIRMED grep gates |
| `build_crosscheck.py` | Regenerate hub/repro/explainers after protocol change |
</standard_stack>

<findings>
## Key Findings

### Baseline run (2026-06-23)
```
SEEDS_PER_N=5, SIZES=[200,500,1000,2000,5000], MEAN_DEGREE=6
p_c_hat ≈ 0.227–0.236 (flat across N)
Fitted nu = 0.239, R² = 0.62, error vs 1.0 = 76.1%
RESULT: INCONCLUSIVE
```

### Defects in current implementation
1. **`estimate_pc` stochastic bisection** — one `giant_fraction` call per step; habitat uses trial averaging.
2. **`fit_nu` uses `pc_inf = pcs[-1]`** — protocol specifies `p_c(N) = p_c(∞) + c·N^(-1/ν)`; infinite-limit for ER bond percolation is `p_c(∞) = 1/⟨k⟩ = 1/6`.
3. **No `sign_ok` gate** — habitat rejects fits when p_c estimates cross `PC_INF`.
4. **`SEEDS_PER_N=5`** — protocol `statistical_analysis_plan` mentions 10 seeds per N.

### Phase 1 pattern to replicate
From `simulate_percolation_fss.py`:
- `TRIALS_PER_P` at each bisection midpoint
- `PC_INF` constant (theoretical)
- `fit_nu()` returns `(nu, r2, sign_ok)`; pass requires `sign_ok and rel_err <= NU_TOLERANCE`

### CI gap
`crosscheck-repro.yml` runs epidemic repro but **does not grep** `RESULT: CONFIRMED` (unlike habitat, cluster, Ising).

### Colab path
`run_crosscheck.ipynb` clones repo + runs `epidemic_percolation_fss.py` — verify after Python CONFIRMED.
</findings>

<validation_architecture>
## Validation Architecture

| Layer | Check |
|-------|-------|
| Local | `python epidemic_percolation_fss.py` → `RESULT: CONFIRMED` |
| Regression | `pytest tests/repo_smoke/test_crosscheck_repro_regression.py -k epidemic` |
| CI | `crosscheck-repro.yml` grep CONFIRMED for epidemic step |
| Drift | `python scripts/build_crosscheck.py --check` |
</validation_architecture>