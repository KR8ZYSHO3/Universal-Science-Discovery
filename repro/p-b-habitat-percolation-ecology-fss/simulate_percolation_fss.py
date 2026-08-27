#!/usr/bin/env python3
"""Crosscheck repro: 2D site percolation finite-size scaling of p_c(L).

Lattice:        L × L square
Neighborhood:   4-neighbor (von Neumann)
Boundary:       periodic (torus)
Spanning rule:  wrapping in either direction (horizontal or vertical)
Algorithm:      Newman–Ziff union-find (one occupation sequence per sample)
Estimator:      p_c(L) = mean occupation fraction at first wrapping
                (named: mean first either-wrap). SE = sample SE of the mean.

Theory:  p_c(∞) = 0.59274621,  ν = 4/3
Model:   p_c(L) = p_c(∞) + c L^{-1/ν}

Fit L ∈ {32, 64, 128, 256}. L=16 is printed as a diagnostic (corrections-to-
scaling) and is not used in the exponent fit.

This protocol measures the finite-size *shift* of an effective threshold, not
a generic spanning-probability demo. Open-boundary Π_TB = 0.5 is the wrong
estimator here: Cardy's result says that crossing probability on a square
tends to 1/2 at p_c(∞), so the leading L^{-1/ν} amplitude is ~0 and a
noisy four-point log|Δp| fit cannot recover ν.

Pass / fail / inconclusive (stdout RESULT token; exit code is always 0):
  CONFIRMED     weighted Fit A recovers ν within 15% of 4/3, with SE(ν)
                inside that tolerance, significant c, and R² ≥ 0.85
  INCONCLUSIVE  underpowered (SE too large, sign flips, or R² too low).
                Not a claim that percolation theory is wrong.
  FALSIFIED     powered, and ν is more than 15% from 4/3 with 4/3 outside 2σ

The in-browser JS runner is a smoke test and must not emit CONFIRMED.

CI greps stdout for RESULT: CONFIRMED on a powered run.
"""
from __future__ import annotations

import argparse
import math
import random
import sys
import time
from typing import Dict, List, Sequence, Tuple

PC_INF = 0.59274621
NU_THEORY = 4 / 3
NU_TOLERANCE = 0.15
R2_MIN = 0.85
FIT_SIZES = [32, 64, 128, 256]
DIAGNOSTIC_SIZES = [16]
N_SAMPLES = 400
SEED = 42

# Legacy (pre-fix) demo / DFS-bisection numbers, kept for the power note.
LEGACY_DEMO_TRIALS_PER_P = 120
LEGACY_PYTHON_TRIALS_PER_P = 350
LEGACY_SIZES = [16, 32, 64, 128]
# 2026-06-22 "CONFIRMED" snapshot stored in tests — noisy, L=64 ≈ p_c(∞).
LEGACY_REFERENCE_PCS = [0.59080, 0.59059, 0.59268, 0.59179]


def first_wrap_either(L: int, rng: random.Random) -> float:
    """Occupation fraction at first either-direction wrap on an L×L torus."""
    n = L * L
    parent = list(range(n))
    dx = [0] * n
    dy = [0] * n
    rank = [0] * n
    occupied = [False] * n

    def find(x: int) -> int:
        if parent[x] != x:
            orig = parent[x]
            root = find(orig)
            dx[x] += dx[orig]
            dy[x] += dy[orig]
            parent[x] = root
            return root
        return x

    wrap_h = False
    wrap_v = False
    order = list(range(n))
    rng.shuffle(order)
    for k, s in enumerate(order, start=1):
        occupied[s] = True
        r, c = divmod(s, L)
        bonds = (
            ((r - 1) % L, c, -1, 0),
            ((r + 1) % L, c, 1, 0),
            (r, (c - 1) % L, 0, -1),
            (r, (c + 1) % L, 0, 1),
        )
        for nr, nc, by, bx in bonds:
            t = nr * L + nc
            if not occupied[t]:
                continue
            rs, rt = find(s), find(t)
            if rs == rt:
                wx = dx[s] + bx - dx[t]
                wy = dy[s] + by - dy[t]
                if wx != 0:
                    wrap_h = True
                if wy != 0:
                    wrap_v = True
            elif rank[rs] < rank[rt]:
                parent[rs] = rt
                dx[rs] = dx[t] - bx - dx[s]
                dy[rs] = dy[t] - by - dy[s]
            else:
                parent[rt] = rs
                dx[rt] = dx[s] + bx - dx[t]
                dy[rt] = dy[s] + by - dy[t]
                if rank[rs] == rank[rt]:
                    rank[rs] += 1
        if wrap_h or wrap_v:
            return k / n
    return 1.0


def sample_pc(L: int, n_samples: int, rng: random.Random) -> Tuple[List[float], float, float, float]:
    """Return (samples, mean, SE of mean, stdev)."""
    ps = [first_wrap_either(L, rng) for _ in range(n_samples)]
    mean = sum(ps) / n_samples
    var = sum((p - mean) ** 2 for p in ps) / (n_samples - 1) if n_samples > 1 else 0.0
    sigma = math.sqrt(var)
    se = sigma / math.sqrt(n_samples) if n_samples else float("inf")
    return ps, mean, se, sigma


def _se_nu_from_chi2(
    chi2_of: Sequence[Tuple[float, float]], nu_hat: float, chi2_min: float
) -> float:
    """1σ width from the χ² = χ²min + 1 contour (1 parameter)."""
    target = chi2_min + 1.0
    left = chi2_of[0][0]
    right = chi2_of[-1][0]
    prev_nu, prev_chi = chi2_of[0]
    found_left = False
    found_right = False
    for nu, chi2 in chi2_of[1:]:
        if (not found_left) and prev_nu <= nu_hat and prev_chi >= target > chi2:
            denom = prev_chi - chi2
            frac = (prev_chi - target) / denom if denom else 0.0
            left = prev_nu + frac * (nu - prev_nu)
            found_left = True
        if (not found_right) and prev_nu >= nu_hat and prev_chi < target <= chi2:
            denom = chi2 - prev_chi
            frac = (target - prev_chi) / denom if denom else 0.0
            right = prev_nu + frac * (nu - prev_nu)
            found_right = True
        prev_nu, prev_chi = nu, chi2
    if not found_left:
        left = chi2_of[0][0]
    if not found_right:
        right = chi2_of[-1][0]
    return max(nu_hat - left, right - nu_hat)


def wls_through_origin(
    x: Sequence[float], y: Sequence[float], se: Sequence[float]
) -> Tuple[float, float, float, float]:
    """Weighted least squares y = c x (no intercept). Returns c, se_c, chi2, R²."""
    w = [1.0 / (s * s) if s > 0 else 0.0 for s in se]
    den = sum(wi * xi * xi for wi, xi in zip(w, x))
    if den <= 0:
        return 0.0, float("inf"), float("inf"), 0.0
    c = sum(wi * xi * yi for wi, xi, yi in zip(w, x, y)) / den
    se_c = math.sqrt(1.0 / den)
    resid = [yi - c * xi for xi, yi in zip(x, y)]
    chi2 = sum(wi * ri * ri for wi, ri in zip(w, resid))
    y_mean = sum(y) / len(y)
    ss_tot = sum((yi - y_mean) ** 2 for yi in y)
    ss_res = sum(ri * ri for ri in resid)
    r2 = 1.0 - ss_res / ss_tot if ss_tot else 0.0
    return c, se_c, chi2, r2


def fit_a(
    sizes: Sequence[int], pcs: Sequence[float], ses: Sequence[float]
) -> Dict[str, float]:
    """Fix p_c(∞), fit c and ν in p_c = p_c(∞) + c L^{-1/ν}."""
    y = [pc - PC_INF for pc in pcs]
    nu_grid = [0.50 + i * 0.002 for i in range(int((2.50 - 0.50) / 0.002) + 1)]
    best = None
    chi2_of: List[Tuple[float, float]] = []
    for nu in nu_grid:
        x = [L ** (-1.0 / nu) for L in sizes]
        c, se_c, chi2, r2 = wls_through_origin(x, y, ses)
        chi2_of.append((nu, chi2))
        if best is None or chi2 < best[0]:
            best = (chi2, nu, c, se_c, r2)
    assert best is not None
    chi2_min, nu_hat, c_hat, se_c, r2 = best
    se_nu = _se_nu_from_chi2(chi2_of, nu_hat, chi2_min)
    return {
        "nu": nu_hat,
        "se_nu": se_nu,
        "c": c_hat,
        "se_c": se_c,
        "chi2": chi2_min,
        "r2": r2,
        "rel_err": abs(nu_hat - NU_THEORY) / NU_THEORY,
    }


def fit_b(
    sizes: Sequence[int], pcs: Sequence[float], ses: Sequence[float]
) -> Dict[str, float]:
    """Fix ν = 4/3, fit c in p_c = p_c(∞) + c L^{-3/4}."""
    y = [pc - PC_INF for pc in pcs]
    x = [L ** (-1.0 / NU_THEORY) for L in sizes]
    c, se_c, chi2, r2 = wls_through_origin(x, y, ses)
    return {"c": c, "se_c": se_c, "chi2": chi2, "r2": r2, "nu": NU_THEORY}


def fit_width_nu(sizes: Sequence[int], sigmas: Sequence[float]) -> Tuple[float, float]:
    """Sanity: σ(p_span) ~ L^{-1/ν} via unweighted log-log. Returns (ν, R²)."""
    xs = [math.log(L) for L in sizes]
    ys = [math.log(s) for s in sigmas]
    n = len(xs)
    x_mean = sum(xs) / n
    y_mean = sum(ys) / n
    den = sum((x - x_mean) ** 2 for x in xs)
    if den <= 0:
        return float("inf"), 0.0
    slope = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys)) / den
    nu = -1.0 / slope if slope else float("inf")
    ss_res = sum((y - (y_mean + slope * (x - x_mean))) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - y_mean) ** 2 for y in ys)
    r2 = 1.0 - ss_res / ss_tot if ss_tot else 0.0
    return nu, r2


def same_sign_deltas(pcs: Sequence[float]) -> bool:
    deltas = [pc - PC_INF for pc in pcs]
    if any(d == 0 for d in deltas):
        return False
    signs = [d > 0 for d in deltas]
    return all(signs) or not any(signs)


def approaches_pc(sizes: Sequence[int], pcs: Sequence[float], ses: Sequence[float]) -> bool:
    """|p_c(L) - p_c(∞)| shrinks with L, allowing 2σ noise."""
    abs_d = [abs(pc - PC_INF) for pc in pcs]
    for i in range(len(sizes) - 1):
        slack = 2.0 * (ses[i] + ses[i + 1])
        if abs_d[i + 1] > abs_d[i] + slack:
            return False
    return True


def classify(fit_a_res: Dict[str, float], pcs: Sequence[float], ses: Sequence[float]) -> str:
    powered = fit_a_res["se_nu"] <= NU_TOLERANCE * NU_THEORY
    r2_ok = fit_a_res["r2"] >= R2_MIN
    slope_sig = abs(fit_a_res["c"]) > 2.0 * fit_a_res["se_c"]
    within = fit_a_res["rel_err"] <= NU_TOLERANCE
    sign_ok = same_sign_deltas(pcs)
    mono = approaches_pc(FIT_SIZES, pcs, ses) if len(pcs) == len(FIT_SIZES) else sign_ok

    if not sign_ok or not powered or not slope_sig or not r2_ok:
        return "INCONCLUSIVE"
    if within and mono:
        return "CONFIRMED"
    if (not within) and abs(fit_a_res["nu"] - NU_THEORY) > 2.0 * fit_a_res["se_nu"]:
        return "FALSIFIED"
    return "INCONCLUSIVE"


def samples_for_tolerance(n_samples: int, se_nu: float) -> int:
    target = NU_TOLERANCE * NU_THEORY
    if se_nu <= 0 or se_nu == float("inf"):
        return n_samples
    return max(n_samples, int(math.ceil(n_samples * (se_nu / target) ** 2)))


def legacy_power_note() -> str:
    """Why the old 120-trial open-Π=0.5 demo was INCONCLUSIVE."""
    width_128 = 128 ** (-1.0 / NU_THEORY)
    se_pi = math.sqrt(0.25 / LEGACY_DEMO_TRIALS_PER_P)
    # dΠ/dp ~ L^{1/ν}; Cardy Π(p_c)=1/2 so the *shift* amplitude is ~0.
    se_pc_rough = se_pi * (128 ** (1.0 / NU_THEORY)) / 8.0
    return (
        "Legacy demo (open TB spanning, noisy independent-seed bisection, "
        f"{LEGACY_DEMO_TRIALS_PER_P} trials/p, L∈{LEGACY_SIZES}):\n"
        f"  transition width at L=128 is ~L^{{-3/4}} ≈ {width_128:.4f}\n"
        f"  SE(Π) at Π=0.5 with {LEGACY_DEMO_TRIALS_PER_P} Bernoulli trials ≈ {se_pi:.3f}\n"
        f"  rough SE(p_c) ≳ {se_pc_rough:.4f}, comparable to (or larger than) the\n"
        "  expected shift because Cardy puts Π_TB(p_c(∞)) → 1/2, so c ≈ 0.\n"
        "  log|Δp| vs log L is unstable when a point (e.g. L=64) has Δp ≈ 0.\n"
        f"  The 2026-06-22 Python snapshot at {LEGACY_PYTHON_TRIALS_PER_P} trials/p was\n"
        f"  p_c = {LEGACY_REFERENCE_PCS} — non-monotonic, L=64 on top of p_c(∞).\n"
        "  INCONCLUSIVE there is a power/estimator bug, not a disproof of ν=4/3."
    )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="2D site percolation FSS of p_c(L)")
    p.add_argument("--samples", type=int, default=N_SAMPLES)
    p.add_argument("--seed", type=int, default=SEED)
    return p.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    n_samples = args.samples
    seed = args.seed
    all_sizes = DIAGNOSTIC_SIZES + FIT_SIZES
    t0 = time.perf_counter()

    print("Crosscheck: p-b-habitat-percolation-ecology-fss")
    print("Lattice: L×L square | neighborhood: 4-neighbor | BC: periodic")
    print("Estimator: mean occupation at first either-direction wrapping")
    print("Algorithm: Newman–Ziff union-find")
    print(f"Theory: p_c(inf)={PC_INF}, nu={NU_THEORY:.4f}")
    print(f"Params: L in {all_sizes}, N_SAMPLES={n_samples}, seed={seed}")
    print(f"Fit uses L={FIT_SIZES}; L={DIAGNOSTIC_SIZES} diagnostic only")
    print()
    print(legacy_power_note())
    print()

    means: Dict[int, float] = {}
    ses: Dict[int, float] = {}
    sigmas: Dict[int, float] = {}
    rng = random.Random(seed)
    for L in all_sizes:
        _ps, mean, se, sigma = sample_pc(L, n_samples, rng)
        means[L] = mean
        ses[L] = se
        sigmas[L] = sigma
        delta = mean - PC_INF
        x = L ** (-1.0 / NU_THEORY)
        flag = "fit" if L in FIT_SIZES else "diag"
        print(
            f"  L={L:4d}  p_c_hat={mean:.5f} ± {se:.5f}  "
            f"delta={delta:+.5f}  L^(-3/4)={x:.5f}  sigma={sigma:.5f}  [{flag}]"
        )

    fit_sizes = FIT_SIZES
    fit_pcs = [means[L] for L in fit_sizes]
    fit_ses = [ses[L] for L in fit_sizes]
    fit_sig = [sigmas[L] for L in fit_sizes]

    a = fit_a(fit_sizes, fit_pcs, fit_ses)
    b = fit_b(fit_sizes, fit_pcs, fit_ses)
    nu_w, r2_w = fit_width_nu(fit_sizes, fit_sig)
    result = classify(a, fit_pcs, fit_ses)
    need = samples_for_tolerance(n_samples, a["se_nu"])
    wall = time.perf_counter() - t0
    n_trials = n_samples * len(all_sizes)

    print()
    print("Fit A  (fix p_c(inf), fit c and nu; weighted by SE):")
    print(
        f"  nu = {a['nu']:.4f} ± {a['se_nu']:.4f}   "
        f"c = {a['c']:+.4f} ± {a['se_c']:.4f}"
    )
    print(
        f"  R² = {a['r2']:.4f}   chi² = {a['chi2']:.3f}   "
        f"rel err vs 4/3 = {100 * a['rel_err']:.1f}%  (tolerance {100 * NU_TOLERANCE:.0f}%)"
    )
    print("Fit B  (fix nu=4/3, fit c):")
    print(
        f"  c = {b['c']:+.4f} ± {b['se_c']:.4f}   "
        f"R² = {b['r2']:.4f}   chi² = {b['chi2']:.3f}"
    )
    print(
        f"Width sanity  sigma ~ L^(-1/nu):  nu = {nu_w:.4f}  (R² = {r2_w:.4f})"
    )
    print()
    print(
        f"Power: SE(nu)={a['se_nu']:.4f}; "
        f"target SE ≤ {NU_TOLERANCE * NU_THEORY:.4f} "
        f"needs ~{need} samples/L (current {n_samples})."
    )
    if result == "INCONCLUSIVE":
        print("INCONCLUSIVE means this run is underpowered or the fit is unstable.")
        print("It is not a claim that 2D percolation has the wrong nu.")
    elif result == "FALSIFIED":
        print("FALSIFIED means this estimator+budget disagrees with nu=4/3.")
        print("That is a protocol failure, not a disproof of percolation theory.")
    print(f"Wall-clock {wall:.1f}s  independent sequences={n_trials}")
    print()
    extra = {
        "CONFIRMED": "",
        "INCONCLUSIVE": " (increase --samples; demo JS cannot confirm nu)",
        "FALSIFIED": " (powered disagreement with nu=4/3 for this estimator)",
    }[result]
    print(f"RESULT: {result}{extra}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
