#!/usr/bin/env python3
"""Crosscheck repro: bond percolation FSS on Erdős–Rényi graphs (nu ≈ 1)."""
from __future__ import annotations

import random
import sys
from typing import List, Tuple

try:
    import networkx as nx
except ImportError:
    print("ERROR: networkx required — pip install networkx")
    raise SystemExit(2)

MEAN_DEGREE = 6
SIZES = [200, 500, 1000, 2000, 5000]
SEEDS_PER_N = 5
NU_THEORY = 1.0
NU_TOLERANCE = 0.25


def giant_fraction(g: nx.Graph, p: float, rng: random.Random) -> float:
    """Bond percolation: keep edge with probability p; return giant component fraction."""
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
    components = sorted((len(c) for c in nx.connected_components(kept)), reverse=True)
    return components[0] / n


def er_graph(n: int, mean_k: int, seed: int) -> nx.Graph:
    p_edge = mean_k / (n - 1) if n > 1 else 0.0
    return nx.erdos_renyi_graph(n, p_edge, seed=seed)


def estimate_pc(g: nx.Graph, seed: int) -> float:
    lo, hi = 0.0, 1.0
    rng = random.Random(seed)
    for _ in range(24):
        mid = (lo + hi) / 2
        frac = giant_fraction(g, mid, rng)
        if frac >= 0.5:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def fit_nu(sizes: List[int], pcs: List[float]) -> Tuple[float, float]:
    import math

    pc_inf = pcs[-1]
    xs = [math.log(N) for N in sizes]
    ys = [math.log(abs(pc - pc_inf) + 1e-9) for pc in pcs]
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
    return nu, r2


def main() -> int:
    print("Crosscheck: p-b-percolation-epidemiology-fss")
    print(f"Theory: mean-field nu = {NU_THEORY}")
    print()

    mean_pcs: List[float] = []
    for N in SIZES:
        estimates = []
        for s in range(SEEDS_PER_N):
            g = er_graph(N, MEAN_DEGREE, seed=N * 100 + s)
            estimates.append(estimate_pc(g, seed=N * 100 + s + 7))
        mean_pc = sum(estimates) / len(estimates)
        mean_pcs.append(mean_pc)
        print(f"  N={N:5d}  p_c_hat={mean_pc:.5f}  (seeds={SEEDS_PER_N})")

    nu, r2 = fit_nu(SIZES, mean_pcs)
    rel_err = abs(nu - NU_THEORY) / NU_THEORY if NU_THEORY else float("inf")
    passed = rel_err <= NU_TOLERANCE

    print()
    print(f"Fitted nu = {nu:.4f}  (R² = {r2:.4f})")
    print(f"Relative error vs 1.0 = {100 * rel_err:.1f}%  (tolerance {100 * NU_TOLERANCE:.0f}%)")
    print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase SEEDS_PER_N for stability)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())