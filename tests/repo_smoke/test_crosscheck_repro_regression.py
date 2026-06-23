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


def test_percolation_fss_fit_confirmed_on_reference_pcs() -> None:
    mod = _load_module(
        "simulate_percolation_fss",
        REPO_ROOT / "repro/p-b-habitat-percolation-ecology-fss/simulate_percolation_fss.py",
    )
    # Reference p_c estimates at TRIALS_PER_P=350, seed=42 (2026-06-22 CONFIRMED run).
    pcs = [0.59080, 0.59059, 0.59268, 0.59179]
    nu, r2, sign_ok = mod.fit_nu(mod.SIZES, pcs)
    rel_err = abs(nu - mod.NU_THEORY) / mod.NU_THEORY
    assert sign_ok, "expected all p_c below p_c(inf) for signed FSS fit"
    assert rel_err <= mod.NU_TOLERANCE, f"nu={nu:.4f} err={100 * rel_err:.1f}%"
    assert r2 > 0.0


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