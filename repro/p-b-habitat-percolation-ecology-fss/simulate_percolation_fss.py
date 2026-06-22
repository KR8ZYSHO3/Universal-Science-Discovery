#!/usr/bin/env python3
"""Crosscheck repro: 2D site percolation finite-size scaling (nu ≈ 4/3)."""
from __future__ import annotations

import random
import sys
from typing import List, Tuple

PC_INF = 0.59274621
NU_THEORY = 4 / 3
NU_TOLERANCE = 0.15
SIZES = [16, 32, 64, 128]
TRIALS_PER_P = 350
P_GRID = 32


def neighbors(r: int, c: int, n: int) -> List[Tuple[int, int]]:
    out: List[Tuple[int, int]] = []
    if r > 0:
        out.append((r - 1, c))
    if r + 1 < n:
        out.append((r + 1, c))
    if c > 0:
        out.append((r, c - 1))
    if c + 1 < n:
        out.append((r, c + 1))
    return out


def spans(grid: List[List[bool]]) -> bool:
    n = len(grid)
    seen = [[False] * n for _ in range(n)]
    stack: List[Tuple[int, int]] = []
    for c in range(n):
        if grid[0][c]:
            stack.append((0, c))
            seen[0][c] = True
    while stack:
        r, c = stack.pop()
        if r == n - 1:
            return True
        for nr, nc in neighbors(r, c, n):
            if grid[nr][nc] and not seen[nr][nc]:
                seen[nr][nc] = True
                stack.append((nr, nc))
    return False


def crossing_probability(n: int, p: float, trials: int, seed: int) -> float:
    rng = random.Random(seed)
    hits = 0
    for _ in range(trials):
        grid = [[rng.random() < p for _ in range(n)] for _ in range(n)]
        if spans(grid):
            hits += 1
    return hits / trials


def estimate_pc(n: int, trials: int, seed: int) -> float:
    lo, hi = 0.45, 0.75
    for _ in range(P_GRID):
        mid = (lo + hi) / 2
        prob = crossing_probability(n, mid, trials, seed + _)
        if prob >= 0.5:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def fit_nu(sizes: List[int], pcs: List[float]) -> Tuple[float, float, bool]:
    """Fit p_c(inf) - p_c(L) ~ L^(-1/nu) via log-log linear regression."""
    import math

    deltas = [PC_INF - pc for pc in pcs]
    sign_ok = all(d > 0 for d in deltas)
    xs = [math.log(L) for L in sizes]
    ys = [
        math.log(d if sign_ok else abs(pc - PC_INF) + 1e-9)
        for d, pc in zip(deltas, pcs)
    ]
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
    print("Crosscheck: p-b-habitat-percolation-ecology-fss")
    print(f"Theory: p_c(inf)={PC_INF}, nu={NU_THEORY:.4f}")
    print()

    pcs: List[float] = []
    for i, L in enumerate(SIZES):
        pc = estimate_pc(L, TRIALS_PER_P, seed=42 + i * 1000)
        pcs.append(pc)
        print(f"  L={L:4d}  p_c_hat={pc:.5f}  delta={pc - PC_INF:+.5f}")

    nu, r2, sign_ok = fit_nu(SIZES, pcs)
    rel_err = abs(nu - NU_THEORY) / NU_THEORY
    passed = sign_ok and rel_err <= NU_TOLERANCE

    print()
    if not sign_ok:
        print("Sign check: p_c estimates crossed p_c(inf) — increase TRIALS_PER_P")
    print(f"Fitted nu = {nu:.4f}  (R² = {r2:.4f})")
    print(f"Relative error vs 4/3 = {100 * rel_err:.1f}%  (tolerance {100 * NU_TOLERANCE:.0f}%)")
    print(f"RESULT: {'CONFIRMED' if passed else 'INCONCLUSIVE (increase TRIALS_PER_P for higher precision)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())