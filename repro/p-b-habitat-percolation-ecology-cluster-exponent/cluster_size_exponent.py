#!/usr/bin/env python3
"""Crosscheck repro: cluster size distribution exponent below p_c."""
from __future__ import annotations

import random
import sys
from collections import Counter
from typing import Dict, List, Tuple

P = 0.55
L = 128
SEEDS = 20
TAU_THEORY = 187 / 91
TAU_TOLERANCE = 0.10


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]


def cluster_sizes(grid: List[List[bool]]) -> List[int]:
    n = len(grid)
    uf = UnionFind(n * n)
    for r in range(n):
        for c in range(n):
            if not grid[r][c]:
                continue
            idx = r * n + c
            if r + 1 < n and grid[r + 1][c]:
                uf.union(idx, (r + 1) * n + c)
            if c + 1 < n and grid[r][c + 1]:
                uf.union(idx, r * n + c + 1)
    roots: Dict[int, int] = {}
    for r in range(n):
        for c in range(n):
            if grid[r][c]:
                root = uf.find(r * n + c)
                roots[root] = roots.get(root, 0) + 1
    return [s for s in roots.values() if s >= 2]


def fit_tau(sizes: List[int]) -> Tuple[float, float]:
    import math

    hist: Counter[int] = Counter(sizes)
    lo, hi = 4, L // 4
    xs, ys = [], []
    for s, count in sorted(hist.items()):
        if lo <= s <= hi:
            xs.append(math.log(s))
            ys.append(math.log(count))
    if len(xs) < 3:
        return float("nan"), 0.0
    n = len(xs)
    x_mean = sum(xs) / n
    y_mean = sum(ys) / n
    num = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    den = sum((x - x_mean) ** 2 for x in xs)
    slope = num / den if den else 0.0
    tau = -slope
    ss_res = sum((y - (y_mean + slope * (x - x_mean))) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - y_mean) ** 2 for y in ys)
    r2 = 1 - ss_res / ss_tot if ss_tot else 0.0
    return tau, r2


def main() -> int:
    print("Crosscheck: p-b-habitat-percolation-ecology-cluster-exponent")
    print(f"Theory: tau = 187/91 = {TAU_THEORY:.4f} at p = {P}")
    print()

    taus: List[float] = []
    for seed in range(SEEDS):
        rng = random.Random(seed)
        grid = [[rng.random() < P for _ in range(L)] for _ in range(L)]
        sizes = cluster_sizes(grid)
        tau, r2 = fit_tau(sizes)
        if tau == tau:
            taus.append(tau)
            print(f"  seed={seed:2d}  tau_hat={tau:.4f}  R²={r2:.3f}  clusters={len(sizes)}")

    if not taus:
        print("ERROR: insufficient clusters for fit")
        return 1

    mean_tau = sum(taus) / len(taus)
    rel_err = abs(mean_tau - TAU_THEORY) / TAU_THEORY
    passed = rel_err <= TAU_TOLERANCE

    print()
    print(f"Mean tau = {mean_tau:.4f} over {len(taus)} seeds")
    print(f"Relative error vs 187/91 = {100 * rel_err:.1f}%  (tolerance {100 * TAU_TOLERANCE:.0f}%)")
    print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (adjust P or L for clearer scaling)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())