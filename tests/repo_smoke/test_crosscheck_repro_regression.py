"""Fast regression tests for Crosscheck repro decision logic (fixed inputs)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def test_percolation_fss_weighted_fit_recovers_nu_on_synthetic_shift() -> None:
    mod = _load_module(
        "simulate_percolation_fss",
        REPO_ROOT / "repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py",
    )
    sizes = list(mod.FIT_SIZES)
    c_true = -0.45
    pcs = [mod.PC_INF + c_true * (L ** (-1.0 / mod.NU_THEORY)) for L in sizes]
    ses = [1e-5] * len(sizes)
    fit = mod.fit_a(sizes, pcs, ses)
    assert fit["rel_err"] < 0.05, f"nu={fit['nu']:.4f} err={100 * fit['rel_err']:.1f}%"
    assert fit["r2"] > 0.99
    assert fit["c"] < 0
    assert mod.classify(fit, pcs, ses) == "CONFIRMED"


def test_percolation_fss_legacy_demo_is_inconclusive() -> None:
    """Old open-Π=0.5 four-point snapshot must not pass the new protocol."""
    mod = _load_module(
        "simulate_percolation_fss",
        REPO_ROOT / "repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py",
    )
    # Browser demo quoted in the protocol bug report (120 trials/p, noisy bisection).
    sizes = [16, 32, 64, 128]
    pcs = [0.59139, 0.58444, 0.59272, 0.59055]
    ses = [0.01, 0.01, 0.01, 0.01]
    fit = mod.fit_a(sizes, pcs, ses)
    assert mod.classify(fit, pcs, ses) == "INCONCLUSIVE"
    # June 2026 Python "CONFIRMED" snapshot: L=64 sits on p_c(∞); r2 gate was > 0.
    legacy = list(mod.LEGACY_REFERENCE_PCS)
    legacy_fit = mod.fit_a(sizes, legacy, ses)
    assert mod.classify(legacy_fit, legacy, ses) == "INCONCLUSIVE"


def test_percolation_fss_first_wrap_occurs_before_full_occupation() -> None:
    import random

    mod = _load_module(
        "simulate_percolation_fss",
        REPO_ROOT / "repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py",
    )
    rng = random.Random(0)
    p = mod.first_wrap_either(8, rng)
    assert 0.0 < p < 1.0


def test_ising_ewi_fit_confirmed_on_reference_variances() -> None:
    mod = _load_module(
        "ising_critical_slowing",
        REPO_ROOT / "repro/p-b-ising-social-dynamics-ewi/ising_critical_slowing.py",
    )
    temps = [2.65, 2.55, 2.45, 2.38, 2.33]
    variances = [0.011354, 0.022608, 0.038065, 0.074723, 0.150698]
    taus = [1.12, 1.83, 4.34, 14.23, 40.27]
    ar1s = [0.4091, 0.6165, 0.7778, 0.9099, 0.9642]

    scale_chi = [
        (mod.LATTICE_SIZE**2) * v / t for t, v in zip(temps, variances)
    ]
    gamma, r2 = mod.fit_gamma(temps, scale_chi)
    rel_err = abs(gamma - mod.GAMMA_THEORY) / mod.GAMMA_THEORY

    assert mod.is_monotonic_increasing(variances)
    assert mod.is_monotonic_increasing(ar1s)
    assert mod.is_monotonic_increasing(taus)
    assert rel_err <= mod.GAMMA_TOLERANCE, f"gamma={gamma:.4f} err={100 * rel_err:.1f}%"
    assert r2 > 0.9


def test_cluster_exponent_fit_confirmed_on_pooled_reference() -> None:
    mod = _load_module(
        "cluster_size_exponent",
        REPO_ROOT
        / "repro/p-b-habitat-percolation-ecology-cluster-exponent/cluster_size_exponent.py",
    )
    # Reference pooled histogram at P=0.59, L=256, SEEDS=20 (2026-06-23 CONFIRMED run).
    sizes = mod.collect_pooled_sizes()
    tau, r2 = mod.fit_tau(sizes)
    rel_err = abs(tau - mod.TAU_THEORY) / mod.TAU_THEORY

    assert len(sizes) > 10_000
    assert rel_err <= mod.TAU_TOLERANCE, f"tau={tau:.4f} err={100 * rel_err:.1f}%"
    assert r2 > 0.9


def test_epidemic_fss_fit_confirmed_on_reference_pcs() -> None:
    mod = _load_module(
        "epidemic_percolation_fss",
        REPO_ROOT / "repro/p-b-percolation-epidemiology-fss/epidemic_percolation_fss.py",
    )
    # Reference mean p_c(N) at SEEDS_PER_N=20, SIZES including 5000
    # (2026-08-26 CONFIRMED run; see 02-01-SUMMARY.md CONFIRMED_FREEZE).
    pcs = [
        0.16796109080314636,
        0.16996005177497864,
        0.16739705204963684,
        0.1681748926639557,
        0.16720572113990784,
    ]
    assert list(mod.SIZES) == [200, 500, 1000, 2000, 5000]
    assert mod.NU_THEORY == 3.0
    assert mod.PC_INF == 1.0 / mod.MEAN_DEGREE
    nu, r2, sign_ok = mod.fit_nu(mod.SIZES, pcs)
    rel_err = abs(nu - mod.NU_THEORY) / mod.NU_THEORY
    assert sign_ok, "expected all p_c above p_c(inf) for signed ER FSS fit"
    assert rel_err <= mod.NU_TOLERANCE, f"nu={nu:.4f} err={100 * rel_err:.1f}%"
    assert r2 > 0.0
