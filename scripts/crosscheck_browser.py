"""Shared registry of Crosscheck repros with in-browser JavaScript runners."""
from __future__ import annotations

from pathlib import Path

# Protocol id -> JS filename in repro bundle (stdlib repros only).
BROWSER_RUNNERS: dict[str, str] = {
    "p-b-habitat-percolation-ecology-fss": "simulate_percolation_fss.js",
    "p-b-habitat-percolation-ecology-cluster-exponent": "cluster_size_exponent.js",
}


def browser_runner_script(bundle_dir: Path, proto_id: str) -> str | None:
    js_name = BROWSER_RUNNERS.get(proto_id)
    if not js_name:
        return None
    if (bundle_dir / js_name).is_file():
        return js_name
    return None