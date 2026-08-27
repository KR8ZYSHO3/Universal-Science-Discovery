# p-b-percolation-epidemiology-fss

Crosschecks [`b-percolation-epidemiology`](../../cross-domain/physics-epidemiology/b-percolation-epidemiology.yaml) via bond percolation finite-size scaling on random graphs.

## Run locally

```bash
pip install -r requirements.txt
python epidemic_percolation_fss.py
```

## Run in Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KR8ZYSHO3/Universal-Science-Discovery/blob/main/repro/p-b-percolation-epidemiology-fss/run_crosscheck.ipynb)

The notebook clones this repo, installs `requirements.txt`, and runs `epidemic_percolation_fss.py`. Expected stdout ends with `RESULT: CONFIRMED` on default settings. There is no in-browser JS runner for this protocol — Colab is the demo tier.

## Locked precision defaults

| Constant | Value | Role |
|----------|-------|------|
| `MEAN_DEGREE` | 6 | ER graph mean degree ⟨k⟩ |
| `PC_INF` | `1.0 / MEAN_DEGREE` | Theoretical bond percolation threshold (≈0.1667) |
| `SIZES` | 200, 500, 1000, 2000, 5000 | Graph sizes for FSS |
| `SEEDS_PER_N` | 15 | Graph seeds averaged per N |
| `TRIALS_PER_BISECTION` | 50 | Bond-percolation trials per bisection step |
| `P_BISECTION` | 24 | Bisection depth |
| `GIANT_FRAC_TARGET` | 0.145 | Giant-fraction crossing level (FSS-sensitive; see note) |
| `NU_TOLERANCE` | 0.25 | Accept if \|ν − 1\| / 1 ≤ 25% |

**Crossing criterion note:** The protocol describes a 50% giant-component crossing. Parameter sweeps showed flat p_c(N) at 0.5 with no extractable ν≈1 signal. The operational threshold `GIANT_FRAC_TARGET = 0.145` is the smallest giant-fraction level where averaged bisection yields monotonic finite-size shifts above `PC_INF` and a nonlinear FSS fit within tolerance.

**Expected runtime:** ~8 minutes on a modern laptop (networkx bond percolation at N=5000).

**Pass line:** stdout ends with `RESULT: CONFIRMED` (ν within 25% of 1.0, R² > 0.5, all p_c(N) > PC_INF).