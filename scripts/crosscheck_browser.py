"""Shared registry of Crosscheck repros with in-browser JavaScript runners."""
from __future__ import annotations

from pathlib import Path

# Protocol id -> JS filename in repro bundle (stdlib repros only).
BROWSER_RUNNERS: dict[str, str] = {
    "p-b-habitat-percolation-ecology-fss": "simulate_percolation_fss.js",
    "p-b-habitat-percolation-ecology-cluster-exponent": "cluster_size_exponent.js",
    "p-b-ising-social-dynamics-ewi": "ising_critical_slowing.js",
}


COLAB_NOTEBOOK = "run_crosscheck.ipynb"


def browser_runner_script(bundle_dir: Path, proto_id: str) -> str | None:
    js_name = BROWSER_RUNNERS.get(proto_id)
    if not js_name:
        return None
    if (bundle_dir / js_name).is_file():
        return js_name
    return None


def colab_url(bundle_dir: Path, proto_id: str, repo: str = "KR8ZYSHO3/Universal-Science-Discovery") -> str | None:
    if not (bundle_dir / COLAB_NOTEBOOK).is_file():
        return None
    bundle = bundle_dir.relative_to(bundle_dir.parents[1]).as_posix()
    return (
        f"https://colab.research.google.com/github/{repo}/blob/main/"
        f"{bundle}/{COLAB_NOTEBOOK}"
    )


def run_mode(proto_id: str, bundle_dir: Path) -> str:
    """Human label for how to run: browser, colab, or local."""
    if browser_runner_script(bundle_dir, proto_id):
        return "browser"
    if colab_url(bundle_dir, proto_id):
        return "colab"
    return "local"