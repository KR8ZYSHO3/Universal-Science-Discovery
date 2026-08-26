# p-b-percolation-oncology-gcc

Crosschecks [`b-percolation-oncology`](../../cross-domain/physics-oncology/b-percolation-oncology.yaml) via a thin stdlib site-percolation occupancy sweep (giant-component fraction + spanning). Synthetic lattice only — no clinical data.

```bash
python giant_component_fraction.py
```

Exit code 0 always; inspect stdout for CONFIRMED vs INCONCLUSIVE.

This demo always prints INCONCLUSIVE (small L, few trials, not a precision or clinical test). There is no in-browser JS runner.
