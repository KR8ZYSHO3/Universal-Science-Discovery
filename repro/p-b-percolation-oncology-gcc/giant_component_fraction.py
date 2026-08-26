#!/usr/bin/env python3
"""Crosscheck repro: thin synthetic-lattice giant-component / spanning sweep.

Operationalizes b-percolation-oncology opportunity 1 (GCC as a
treatment-response metric) on an L=32 site lattice. Not a clinical
biomarker. Not an FSS precision pass. Always prints RESULT: INCONCLUSIVE
and returns 0.
"""
from __future__ import annotations

import random
import sys
from typing import Dict, List, Tuple

L = 32
TRIALS = 8
P_VALUES = [0.40, 0.50, 0.59, 0.70]
SPAN_THRESHOLD = 0.5
SEED = 42


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


def giant_fraction(grid: List[List[bool]]) -> float:
    n = len(grid)
    if n == 0:
        return 0.0
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
    sizes: Dict[int, int] = {}
    for r in range(n):
        for c in range(n):
            if grid[r][c]:
                root = uf.find(r * n + c)
                sizes[root] = sizes.get(root, 0) + 1
    if not sizes:
        return 0.0
    return max(sizes.values()) / float(n * n)


def main() -> int:
    print("Crosscheck: p-b-percolation-oncology-gcc")
    print(f"L={L} TRIALS={TRIALS} SPAN_THRESHOLD={SPAN_THRESHOLD}")
    print("Synthetic site lattice only — not a clinical biomarker; not FSS.")
    print()
    for p in P_VALUES:
        span_hits = 0
        giant_sum = 0.0
        for t in range(TRIALS):
            rng = random.Random(SEED + int(round(p * 1000)) + t)
            grid = [[rng.random() < p for _ in range(L)] for _ in range(L)]
            if spans(grid):
                span_hits += 1
            giant_sum += giant_fraction(grid)
        span_frac = span_hits / TRIALS
        mean_s = giant_sum / TRIALS
        flag = "above" if span_frac >= SPAN_THRESHOLD else "below"
        print(
            f"  p={p:.2f}  span={span_frac:.3f} ({flag} {SPAN_THRESHOLD})  "
            f"giant={mean_s:.3f}"
        )
    print()
    print(
        "RESULT: INCONCLUSIVE (thin synthetic lattice; not a clinical "
        "biomarker; not an FSS precision pass)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
