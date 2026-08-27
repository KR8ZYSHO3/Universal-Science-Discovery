# p-b-habitat-percolation-ecology-fss

Crosschecks [`b-habitat-percolation-ecology`](../../cross-domain/physics-ecology/b-habitat-percolation-ecology.yaml) via finite-size scaling of an effective 2D site-percolation threshold \(p_c(L)\).

```bash
python simulate_percolation_fss.py
```

Canonical defaults: Newman–Ziff union-find, periodic \(L\times L\) square, 4-neighbor, \(p_c(L)\) = mean occupation at first wrapping in either direction, \(L\in\{32,64,128,256\}\) in the exponent fit (400 samples per \(L\)). Exit code 0 always; inspect stdout for `RESULT: CONFIRMED` / `INCONCLUSIVE` / `FALSIFIED`.

The in-browser page is a **smoke test** (smaller \(L\), 48 samples). It must print `INCONCLUSIVE`. That means the demo is underpowered, not that percolation is wrong.

## What this means for habitat maps

A habitat map of finite area is not the infinite lattice of textbooks. The occupancy at which a connected path first wraps the map — the coverage where patches join into one spanning landscape — shifts with map size as \(L^{-3/4}\) in two dimensions. Smaller reserves therefore have a different connectivity threshold than a continental grid of the same habitat fraction. This test checks that shift, not whether percolation “exists.”

## Why the old 120-trial demo was INCONCLUSIVE

It estimated \(p_c(L)\) by noisy bisection of open-boundary top–bottom spanning probability through \(1/2\). On a square, that crossing tends to \(1/2\) at \(p_c(\infty)\) (Cardy), so the leading \(L^{-1/\nu}\) amplitude is ~0. Combined with a four-point \(\log|\Delta p|\) fit and 120 independent Bernoulli trials per probe, the run was underpowered. The physics formula was never the problem.
