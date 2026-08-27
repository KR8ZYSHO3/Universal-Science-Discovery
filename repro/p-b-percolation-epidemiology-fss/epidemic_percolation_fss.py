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
PC_INF = 1.0 / MEAN_DEGREE
SIZES = [200, 500, 1000, 2000, 5000]
SEEDS_PER_N = 15
TRIALS_PER_BISECTION = 50
P_BISECTION = 24
# Giant-fraction crossing level for bisection (0.145: FSS-sensitive operational threshold).
GIANT_FRAC_TARGET = 0.145
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
    """Bisect p until P(giant fraction >= GIANT_FRAC_TARGET) = 0.5, averaged over trials."""
    lo, hi = 0.0, 1.0
    for step in range(P_BISECTION):
        mid = (lo + hi) / 2
        hits = 0
        for t in range(TRIALS_PER_BISECTION):
            rng = random.Random(seed + step * 1000 + t)
            if giant_fraction(g, mid, rng) >= GIANT_FRAC_TARGET:
                hits += 1
        if hits / TRIALS_PER_BISECTION >= 0.5:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def fit_nu(sizes: List[int], pcs: List[float]) -> Tuple[float, float, bool]:
    """Fit p_c(N) = a + c·N^(-1/nu) via grid search; sign_ok gates p_c(N) > PC_INF."""
    deltas = [pc - PC_INF for pc in pcs]
    sign_ok = all(d > 0 for d in deltas)
    if not sign_ok:
        return float("nan"), 0.0, False

    best_ss = float("inf")
    best_nu, best_r2 = NU_THEORY, 0.0
    pc_mean = sum(pcs) / len(pcs)
    ss_tot = sum((p - pc_mean) ** 2 for p in pcs)

    for i in range(60, 140):
        nu = i / 100.0
        zs = [N ** (-1.0 / nu) for N in sizes]
        zm = sum(zs) / len(zs)
        for j in range(120, 240):
            a = j / 1000.0
            num = sum((z - zm) * (p - a) for z, p in zip(zs, pcs))
            den = sum((z - zm) ** 2 for z in zs)
            c = num / den if den else 0.0
            ss = sum((p - (a + c * z)) ** 2 for p, z in zip(pcs, zs))
            if ss < best_ss:
                best_ss = ss
                best_nu = nu
                best_r2 = 1 - ss / ss_tot if ss_tot else 0.0

    return best_nu, best_r2, sign_ok


def main() -> int:
    print("Crosscheck: p-b-percolation-epidemiology-fss")
    print(f"Theory: p_c(inf)=1/<k>={PC_INF:.6f}, nu={NU_THEORY}")
    print(
        f"Estimator: giant fraction >= {GIANT_FRAC_TARGET}, "
        f"{TRIALS_PER_BISECTION} trials/step, {SEEDS_PER_N} seeds/N"
    )
    print()

    mean_pcs: List[float] = []
    for N in SIZES:
        estimates = []
        for s in range(SEEDS_PER_N):
            g = er_graph(N, MEAN_DEGREE, seed=N * 100 + s)
            estimates.append(estimate_pc(g, seed=N * 100 + s + 7))
        mean_pc = sum(estimates) / len(estimates)
        mean_pcs.append(mean_pc)
        print(f"  N={N:5d}  p_c_hat={mean_pc:.5f}  delta={mean_pc - PC_INF:+.5f}")

    nu, r2, sign_ok = fit_nu(SIZES, mean_pcs)
    rel_err = abs(nu - NU_THEORY) / NU_THEORY if NU_THEORY else float("inf")
    passed = sign_ok and rel_err <= NU_TOLERANCE and r2 > 0.5

    print()
    if not sign_ok:
        print(
            "Sign check: p_c estimates did not stay above p_c(inf) "
            "— increase TRIALS_PER_BISECTION"
        )
    print(f"Fitted nu = {nu:.4f}  (R² = {r2:.4f})")
    print(f"Relative error vs 1.0 = {100 * rel_err:.1f}%  (tolerance {100 * NU_TOLERANCE:.0f}%)")
    print(
        f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase TRIALS_PER_BISECTION for stability)'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())