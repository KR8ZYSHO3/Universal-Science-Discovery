# p-b-percolation-epidemiology-fss

Crosschecks [`b-percolation-epidemiology`](../../cross-domain/physics-epidemiology/b-percolation-epidemiology.yaml) via bond percolation finite-size scaling on Erdős–Rényi graphs.

This Crosscheck tests the **volume** FSS exponent nu_bar = 3 (mean-field d_u=6, lattice nu=1/2). The Bethe/chemical-distance exponent nu = 1 is a different quantity and is not the fit target.

```bash
pip install -r requirements.txt
python epidemic_percolation_fss.py
```

Exit code 0 always; inspect stdout for CONFIRMED vs INCONCLUSIVE.

Demo tier is Google Colab (`run_crosscheck.ipynb`), which clones this repo and runs the same `epidemic_percolation_fss.py`. There is no in-browser JS runner.
