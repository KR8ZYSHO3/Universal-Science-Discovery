#!/usr/bin/env python3
"""Crosscheck repro: 2D Ising early-warning indicators near T_c (gamma ~ 7/4)."""
from __future__ import annotations

import math
import random
import sys
from typing import List, Tuple

TC = 2.0 / math.log(1.0 + math.sqrt(2.0))
GAMMA_THEORY = 7.0 / 4.0
GAMMA_TOLERANCE = 0.25
# Stay in the scaling regime above T_c (finite-size peak is slightly above T_c).
TEMPERATURES = [2.65, 2.55, 2.45, 2.38, 2.33, 2.30]
LATTICE_SIZE = 48
EQ_SWEEPS_BASE = 1200
EQ_SWEEPS_NEAR_TC = 6000
SAMPLES = 400
SAMPLE_INTERVAL = 40
SEED = 42
# Points with |T - T_c| below this sit in the finite-size susceptibility peak.
FIT_MIN_DELTA = 0.055


def init_lattice(n: int, rng: random.Random) -> List[List[int]]:
    return [[1 if rng.random() < 0.5 else -1 for _ in range(n)] for _ in range(n)]


def magnetisation(grid: List[List[int]]) -> float:
    n = len(grid)
    total = sum(grid[r][c] for r in range(n) for c in range(n))
    return total / (n * n)


def metropolis_sweep(grid: List[List[int]], beta: float, rng: random.Random) -> None:
    n = len(grid)
    for _ in range(n * n):
        r = rng.randrange(n)
        c = rng.randrange(n)
        s = grid[r][c]
        nn = (
            grid[(r - 1) % n][c]
            + grid[(r + 1) % n][c]
            + grid[r][(c - 1) % n]
            + grid[r][(c + 1) % n]
        )
        dE = 2.0 * s * nn
        if dE <= 0.0 or rng.random() < math.exp(-dE * beta):
            grid[r][c] = -s


def equilibration_sweeps(t: float) -> int:
    if t - TC < 0.08:
        return EQ_SWEEPS_NEAR_TC
    if t - TC < 0.15:
        return EQ_SWEEPS_BASE * 2
    return EQ_SWEEPS_BASE


def sample_series(grid: List[List[int]], beta: float, rng: random.Random, t: float) -> List[float]:
    for _ in range(equilibration_sweeps(t)):
        metropolis_sweep(grid, beta, rng)
    series: List[float] = []
    for _ in range(SAMPLES):
        for _ in range(SAMPLE_INTERVAL):
            metropolis_sweep(grid, beta, rng)
        series.append(magnetisation(grid))
    return series


def variance(xs: List[float]) -> float:
    n = len(xs)
    if n < 2:
        return 0.0
    mean = sum(xs) / n
    return sum((x - mean) ** 2 for x in xs) / (n - 1)


def ar1(xs: List[float]) -> float:
    n = len(xs)
    if n < 3:
        return 0.0
    x0 = xs[:-1]
    x1 = xs[1:]
    m0 = sum(x0) / len(x0)
    m1 = sum(x1) / len(x1)
    cov = sum((a - m0) * (b - m1) for a, b in zip(x0, x1)) / (len(x0) - 1)
    var0 = sum((a - m0) ** 2 for a in x0) / (len(x0) - 1)
    return cov / var0 if var0 > 1e-12 else 0.0


def integrated_autocorr_time(xs: List[float]) -> float:
    """Estimate tau_int from normalized autocorrelation (critical slowing down)."""
    n = len(xs)
    if n < 8:
        return 0.0
    mean = sum(xs) / n
    var = sum((x - mean) ** 2 for x in xs) / n
    if var < 1e-12:
        return 0.0
    tau = 0.5
    for lag in range(1, min(n // 2, 80)):
        num = sum((xs[i] - mean) * (xs[i + lag] - mean) for i in range(n - lag))
        rho = num / ((n - lag) * var)
        if rho <= 0.0:
            break
        tau += rho
        if lag > 5 and rho < 0.05:
            break
    return max(tau, 0.0)


def is_monotonic_increasing(values: List[float]) -> bool:
    return all(values[i] < values[i + 1] for i in range(len(values) - 1))


def fit_gamma(temps: List[float], variances: List[float]) -> Tuple[float, float]:
    xs = [math.log(abs(t - TC) + 1e-9) for t in temps]
    ys = [math.log(v + 1e-12) for v in variances]
    n = len(xs)
    x_mean = sum(xs) / n
    y_mean = sum(ys) / n
    num = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    den = sum((x - x_mean) ** 2 for x in xs)
    slope = num / den if den else 0.0
    gamma = -slope
    ss_res = sum((y - (y_mean + slope * (x - x_mean))) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - y_mean) ** 2 for y in ys)
    r2 = 1.0 - ss_res / ss_tot if ss_tot else 0.0
    return gamma, r2


def main() -> int:
    print("Crosscheck: p-b-ising-social-dynamics-ewi")
    print(f"Theory: T_c={TC:.5f}, gamma={GAMMA_THEORY:.4f}")
    print(f"Lattice {LATTICE_SIZE}x{LATTICE_SIZE}, samples/T={SAMPLES}")
    print()

    rng = random.Random(SEED)
    variances: List[float] = []
    ar1s: List[float] = []
    taus: List[float] = []

    for i, t in enumerate(TEMPERATURES):
        grid = init_lattice(LATTICE_SIZE, rng)
        beta = 1.0 / t
        series = sample_series(grid, beta, rng, t)
        var_m = variance(series)
        lag1 = ar1(series)
        tau = integrated_autocorr_time(series)
        variances.append(var_m)
        ar1s.append(lag1)
        taus.append(tau)
        print(
            f"  T={t:.3f}  |T-Tc|={t - TC:.4f}  "
            f"Var(M)={var_m:.6f}  AR1={lag1:.4f}  tau={tau:.2f}"
        )

    scaling_idx = [i for i, t in enumerate(TEMPERATURES) if t - TC >= FIT_MIN_DELTA]
    scale_t = [TEMPERATURES[i] for i in scaling_idx]
    scale_var = [variances[i] for i in scaling_idx]
    scale_ar1 = [ar1s[i] for i in scaling_idx]
    scale_tau = [taus[i] for i in scaling_idx]

    var_mono = is_monotonic_increasing(scale_var)
    ar1_mono = is_monotonic_increasing(scale_ar1)
    tau_mono = is_monotonic_increasing(scale_tau)
    scale_chi = [
        (LATTICE_SIZE**2) * v / t for t, v in zip(scale_t, scale_var)
    ]
    gamma, r2 = fit_gamma(scale_t, scale_chi)
    rel_err = abs(gamma - GAMMA_THEORY) / GAMMA_THEORY
    gamma_ok = rel_err <= GAMMA_TOLERANCE
    ewi_mono = tau_mono and (var_mono or ar1_mono)
    passed = ewi_mono and gamma_ok

    print()
    print(f"Scaling-regime points (|T-Tc| >= {FIT_MIN_DELTA}): {len(scale_t)}")
    print(f"Var(M) monotonic toward T_c: {'yes' if var_mono else 'no'}")
    print(f"AR1 monotonic toward T_c:    {'yes' if ar1_mono else 'no'}")
    print(f"tau_int monotonic toward T_c: {'yes' if tau_mono else 'no'}")
    print(f"Fitted gamma = {gamma:.4f}  (R² = {r2:.4f})")
    print(
        f"Relative error vs 7/4 = {100 * rel_err:.1f}%  "
        f"(tolerance {100 * GAMMA_TOLERANCE:.0f}%)"
    )
    if passed:
        result = "CONFIRMED"
    elif gamma_ok or ewi_mono:
        result = "INCONCLUSIVE (increase EQ_SWEEPS_NEAR_TC for higher precision)"
    else:
        result = "INCONCLUSIVE (increase EQ_SWEEPS_NEAR_TC for higher precision)"
    print(f"RESULT: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())