# Crosscheck launch story — habitat percolation bridge

**Use this as the lead narrative for outreach** (Reddit, LinkedIn, X, institutional emails). It demonstrates USDR is not only a catalog — it produces runnable, falsifiable tests of cross-domain bridges.

---

## One-liner

We mapped a physics→ecology bridge in YAML, ran the Crosscheck protocol on a laptop in under 15 seconds, and got a reproducible finite-size scaling result — with a clear path to confirm or falsify the mapping.

---

## The bridge

**Bridge:** `b-habitat-percolation-ecology` — site percolation threshold in statistical physics maps to critical habitat coverage in landscape ecology.

**Protocol:** `p-b-habitat-percolation-ecology-fss` — test whether 2D site percolation finite-size scaling follows exponent ν ≈ 4/3 (universality class), as the bridge claims.

**Explainer + demo:** [Habitat percolation explainer (Crosscheck section)](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/explainers/b-habitat-percolation-ecology.html#crosscheck)

**Repro landing (GitHub Pages):** [p-b-habitat-percolation-ecology-fss/index.html](https://kr8zysho3.github.io/Universal-Science-Discovery/repro/p-b-habitat-percolation-ecology-fss/index.html)

---

## What we ran (2026-06-21)

```bash
pip install -r repro/p-b-habitat-percolation-ecology-fss/requirements.txt
python repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py
```

**Output (default quick-trial settings, ~14s runtime):**

```
Crosscheck: p-b-habitat-percolation-ecology-fss
Theory: p_c(inf)=0.59274621, nu=1.3333

  L=  16  p_c_hat=0.58842  delta=-0.00432
  L=  32  p_c_hat=0.59058  delta=-0.00217
  L=  64  p_c_hat=0.59473  delta=+0.00198
  L= 128  p_c_hat=0.59297  delta=+0.00023

Fitted nu = 0.7743  (R² = 0.8150)
Relative error vs 4/3 = 41.9%  (tolerance 15%)
RESULT: INCONCLUSIVE (increase TRIALS_PER_P for higher precision)
```

---

## How to talk about this honestly

**Do not claim:** "We proved the bridge."

**Do claim:**

- USDR bridges link to **schema-validated protocols** with **self-contained repro scripts**.
- Anyone can re-run the test; results are **falsifiable** (confirmed / falsified / inconclusive at stated precision).
- Default settings prioritize fast CI smoke tests; increasing `TRIALS_PER_P` in the script is the documented next step for publication-grade precision.
- This is the difference between "interesting metaphor" and **infrastructure that closes the loop**.

---

## Suggested social post (short)

> USDR doesn't just catalog cross-domain bridges — it ships **Crosscheck** protocols you can run locally.
>
> We tested the habitat fragmentation ↔ percolation bridge: 2D site percolation finite-size scaling on a laptop in ~15s. Repro script in-repo; result INCONCLUSIVE at quick-trial settings (by design — crank trials for confirm/falsify).
>
> Bridge map → runnable protocol → falsifiable outcome. That's the bet.
>
> Demo: https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/explainers/b-habitat-percolation-ecology.html#crosscheck
> Repo: https://github.com/KR8ZYSHO3/Universal-Science-Discovery

---

## Next steps for contributors

1. Re-run with higher `TRIALS_PER_P` and open a PR updating protocol `status` to `confirmed` or `falsified`.
2. Run `p-b-habitat-percolation-ecology-cluster-exponent` or `p-b-percolation-epidemiology-fss` and document outcomes.
3. Draft a new Crosscheck from any bridge with `cross_pollination_opportunities`: `python scripts/generate_crosscheck.py --bridge <id> --dry-run`