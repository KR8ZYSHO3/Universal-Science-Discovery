# p-b-habitat-percolation-ecology-fss

Crosschecks [`b-habitat-percolation-ecology`](../../cross-domain/physics-ecology/b-habitat-percolation-ecology.yaml) via finite-size scaling of an effective 2D site-percolation threshold \(p_c(L)\).

```bash
python simulate_percolation_fss.py
```

Frozen observable: **2D site percolation, periodic 4-neighbor square lattice, Newman–Ziff; \(p_c(L)\) is the mean occupation fraction at first wrapping in either direction.** Estimator id `mean-first-either-wrap`. SE is the sample standard error of that first-wrap occupation across Newman–Ziff sequences, not a binomial SE on an open-boundary spanning probability. Switching to horizontal-only wrap changes \(c\) and needs a new fit.

Canonical defaults: \(L\in\{32,64,128,256\}\) in the exponent fit (400 samples per \(L\); \(L=16\) diagnostic). \(L=32\) is kept; tighter than ~10% on \(\nu\) needs a second correction term or dropping \(L=32\). Do not loosen the 15% gate. Exit code 0 always; inspect stdout for `RESULT: CONFIRMED` / `INCONCLUSIVE` / `FALSIFIED`.

The in-browser page is a **smoke test** (smaller \(L\), 48 samples). It must print `INCONCLUSIVE`. That means the demo is underpowered, not that percolation is wrong. The browser must not emit `CONFIRMED` and does not recover \(\nu\).

| | Browser smoke | Canonical Python |
|--|--|--|
| \(L\) | 16, 32, 48, 64 | 16 diagnostic + **32, 64, 128, 256** fit |
| Samples | 48 | 400 Newman–Ziff sequences/\(L\) |
| Can emit CONFIRMED? | **No** | Yes, if the weighted fit recovers \(\nu\) within 15% of \(4/3\) |

## What this means for habitat maps

Finite landscapes have a shifted, blurred connectivity threshold; the shift scales as \(L^{-1/\nu}\) for this class of models. Periodic first-wrap is the physics check, not a park-design constant (do not take torus \(c\) as a reserve-sizing number). Real landscapes have open edges. This test checks the finite-size shift, not whether percolation “exists.”

## Why the old 120-trial demo was INCONCLUSIVE

It estimated \(p_c(L)\) by noisy bisection of open-boundary top–bottom spanning probability through \(1/2\). On a square, that crossing tends to \(1/2\) at \(p_c(\infty)\) (Cardy), so the leading \(L^{-1/\nu}\) amplitude is ~0. Combined with a four-point \(\log|\Delta p|\) fit and 120 independent Bernoulli trials per probe, the run was underpowered. The physics formula was never the problem.
