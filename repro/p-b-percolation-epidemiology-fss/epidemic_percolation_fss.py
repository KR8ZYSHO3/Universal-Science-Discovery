#!/usr/bin/env python3
"""Crosscheck repro: bond percolation FSS on Erdős–Rényi graphs.

Tests the volume finite-size scaling exponent nu_bar = 3 (mean-field: upper
critical dimension d_u = 6 times lattice nu = 1/2). The Bethe-lattice
chemical-distance exponent nu = 1 is a different quantity; this script does
not confirm nu = 1 and must not relabel 3 as 1.

Estimator: bisect bond occupancy p until the mean giant-component fraction
S >= N**(-1/3) (mean-field order parameter at p_c: beta/nu_bar = 1/3).
Theoretical p_c(inf) = 1/MEAN_DEGREE for Poisson ER (Newman 2002).
"""
from __future__ import annotations

import random
import sys
from typing import List, Tuple

MEAN_DEGREE = 6
SIZES = [200, 500, 1000, 2000, 5000]
SEEDS_PER_N = 20
NU_THEORY = 3.0
NU_TOLERANCE = 0.25
PC_INF = 1.0 / MEAN_DEGREE


def _require_nx():
    try:
        import networkx as nx
    except ImportError:
        print("ERROR: networkx required — pip install networkx")
        raise SystemExit(2)
    return nx


def order_parameter_threshold(n: int) -> float:
    """Mean-field S(p_c) ~ N**(-1/3)."""
    return n ** (-1.0 / 3.0)


def giant_fraction(g: object, p: float, rng: random.Random) -> float:
    """Bond percolation: keep edge with probability p; return giant component fraction."""
    nx = _require_nx()
    n = g.number_of_nodes()
    if n == 0:
        return 0.0
    kept = nx.Graph()
    kept.add_nodes_from(g.nodes())
    for u, v in g.edges():
        if rng.random() < p:
            kept.add_edge(u, v)
    if kept.number_of_edges() == 0:
        return 0.0
    largest = max(nx.connected_components(kept), key=len)
    return len(largest) / n


def er_graph(n: int, mean_k: int, seed: int) -> object:
    nx = _require_nx()
    p_edge = mean_k / (n - 1) if n > 1 else 0.0
    return nx.fast_gnp_random_graph(n, p_edge, seed=seed)


def estimate_pc(n: int, graphs: List[object], n_seed: int) -> float:
    """Bisect p until mean giant fraction across graphs is S >= N**(-1/3)."""
    lo, hi = 0.0, 1.0
    thresh = order_parameter_threshold(n)
    for t in range(24):
        mid = (lo + hi) / 2.0
        fracs = []
        for s, g in enumerate(graphs):
            rng = random.Random(n_seed + s + 7 + t)
            fracs.append(giant_fraction(g, mid, rng))
        mean_s = sum(fracs) / len(fracs)
        if mean_s >= thresh:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2.0


def fit_nu(sizes: List[int], pcs: List[float]) -> Tuple[float, float, bool]:
    """Fit p_c(N) - p_c(inf) ~ N**(-1/nu) via signed log-log OLS.

    ER pseudocritical points approach from above: deltas = pc - PC_INF.
    """
    import math

    deltas = [pc - PC_INF for pc in pcs]
    sign_ok = all(d > 0 for d in deltas)
    xs = [math.log(N) for N in sizes]
    ys = [math.log(d if sign_ok else abs(d) + 1e-9) for d in deltas]
    n = len(xs)
    x_mean = sum(xs) / n
    y_mean = sum(ys) / n
    num = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    den = sum((x - x_mean) ** 2 for x in xs)
    slope = num / den if den else 0.0
    nu = -1 / slope if slope else float("inf")
    ss_res = sum((y - (y_mean + slope * (x - x_mean))) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - y_mean) ** 2 for y in ys)
    r2 = 1 - ss_res / ss_tot if ss_tot else 0.0
    return nu, r2, sign_ok


def main() -> int:
    _require_nx()
    print("Crosscheck: p-b-percolation-epidemiology-fss")
    print(
        f"Theory: p_c(inf)={PC_INF:.6f} (1/MEAN_DEGREE), volume nu_bar={NU_THEORY} "
        "(not chemical-distance nu=1)"
    )
    print()

    mean_pcs: List[float] = []
    for N in SIZES:
        graphs = [
            er_graph(N, MEAN_DEGREE, seed=N * 100 + s) for s in range(SEEDS_PER_N)
        ]
        mean_pc = estimate_pc(N, graphs, n_seed=N * 100)
        mean_pcs.append(mean_pc)
        print(
            f"  N={N:5d}  p_c_hat={mean_pc:.5f}  "
            f"delta={mean_pc - PC_INF:+.5f}  (seeds={SEEDS_PER_N})"
        )

    nu, r2, sign_ok = fit_nu(SIZES, mean_pcs)
    rel_err = abs(nu - NU_THEORY) / NU_THEORY if NU_THEORY else float("inf")
    passed = sign_ok and rel_err <= NU_TOLERANCE

    print()
    if not sign_ok:
        print("Sign check: p_c estimates crossed p_c(inf) — increase SEEDS_PER_N")
    print(f"Fitted nu = {nu:.4f}  (R² = {r2:.4f})")
    print(
        f"Relative error vs {NU_THEORY} = {100 * rel_err:.1f}%  "
        f"(tolerance {100 * NU_TOLERANCE:.0f}%)"
    )
    print(f"mean_pcs={mean_pcs!r}")
    print(
        f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase SEEDS_PER_N for higher precision)'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
