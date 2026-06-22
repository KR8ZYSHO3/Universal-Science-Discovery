#!/usr/bin/env python3
"""
Regenerate all Crosscheck-generated artifacts from protocols-catalog/.

Runs, in order:
  1. scripts/generate_repro_index_pages.py
  2. scripts/render_crosscheck_hub.py --apply
  3. scripts/generate_explainers.py <bridge-ids…>

Bridge explainers are generated for every bridge with a promoted protocol,
plus the featured DEFAULT_BRIDGES set (so legacy explainers stay current).

Usage:
  python scripts/build_crosscheck.py --apply
  python scripts/build_crosscheck.py --check   # fail if artifacts would change
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DASHBOARD_HTML = ROOT / "dashboard" / "index.html"
EXPLAINER_DIR = ROOT / "dashboard" / "explainers"
CATALOG = ROOT / "protocols-catalog"
HUB_BEGIN = "        <!-- @hub-crosscheck-grid-begin -->"
HUB_END = "        <!-- @hub-crosscheck-grid-end -->"


def _configure_stdio_utf8() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, OSError, ValueError):
            pass


def bridge_ids_for_explainers() -> list[str]:
    from generate_explainers import DEFAULT_BRIDGES

    ids: set[str] = set(DEFAULT_BRIDGES)
    if CATALOG.is_dir():
        for path in sorted(CATALOG.rglob("p-b-*.yaml")):
            try:
                data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            except OSError:
                continue
            bridge = data.get("source_bridge")
            if isinstance(bridge, str) and bridge.startswith("b-"):
                ids.add(bridge)
    return sorted(ids)


def repro_index_paths() -> list[Path]:
    paths: list[Path] = []
    if not CATALOG.is_dir():
        return paths
    for path in sorted(CATALOG.rglob("p-b-*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        bundle = str(data.get("repro_bundle", "")).strip().rstrip("/")
        if bundle:
            paths.append(ROOT / bundle / "index.html")
    return paths


def explainer_paths(bridge_ids: list[str]) -> list[Path]:
    paths = [EXPLAINER_DIR / f"{bid}.html" for bid in bridge_ids]
    paths.append(EXPLAINER_DIR / "index.html")
    return paths


def extract_hub_block(text: str) -> str | None:
    pattern = re.compile(re.escape(HUB_BEGIN) + r".*?" + re.escape(HUB_END), re.DOTALL)
    match = pattern.search(text)
    return match.group(0) if match else None


def snapshot_artifacts(bridge_ids: list[str]) -> dict[str, str]:
    snap: dict[str, str] = {}
    for path in repro_index_paths() + explainer_paths(bridge_ids):
        if path.is_file():
            snap[str(path.relative_to(ROOT))] = path.read_text(encoding="utf-8")
    if DASHBOARD_HTML.is_file():
        text = DASHBOARD_HTML.read_text(encoding="utf-8")
        hub = extract_hub_block(text)
        if hub is not None:
            snap["@hub-crosscheck-grid"] = hub
    return snap


def run_build(bridge_ids: list[str]) -> None:
    py = sys.executable
    steps = [
        [py, str(SCRIPTS / "generate_repro_index_pages.py")],
        [py, str(SCRIPTS / "render_crosscheck_hub.py"), "--apply"],
        [py, str(SCRIPTS / "generate_explainers.py"), *bridge_ids],
    ]
    for cmd in steps:
        proc = subprocess.run(cmd, cwd=ROOT, check=False)
        if proc.returncode != 0:
            raise SystemExit(proc.returncode)


def diff_snapshots(before: dict[str, str], after: dict[str, str]) -> list[str]:
    changed: list[str] = []
    all_keys = sorted(set(before) | set(after))
    for key in all_keys:
        if before.get(key) != after.get(key):
            changed.append(key)
    return changed


def restore_snapshot(snap: dict[str, str], bridge_ids: list[str]) -> None:
    for rel, content in snap.items():
        if rel == "@hub-crosscheck-grid":
            if not DASHBOARD_HTML.is_file():
                continue
            text = DASHBOARD_HTML.read_text(encoding="utf-8")
            pattern = re.compile(
                re.escape(HUB_BEGIN) + r".*?" + re.escape(HUB_END),
                re.DOTALL,
            )
            if pattern.search(text):
                DASHBOARD_HTML.write_text(pattern.sub(content, text, count=1), encoding="utf-8")
            continue
        path = ROOT / rel
        if content:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")


def main() -> int:
    _configure_stdio_utf8()
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--apply", action="store_true", help="Write regenerated artifacts")
    group.add_argument("--check", action="store_true", help="Fail if artifacts would drift")
    args = parser.parse_args()

    sys.path.insert(0, str(SCRIPTS))
    bridge_ids = bridge_ids_for_explainers()
    print(f"Crosscheck build: {len(bridge_ids)} explainer bridge(s)")

    if args.check:
        before = snapshot_artifacts(bridge_ids)
        run_build(bridge_ids)
        after = snapshot_artifacts(bridge_ids)
        changed = diff_snapshots(before, after)
        if changed:
            print("Crosscheck artifacts are stale. Regenerate with:", file=sys.stderr)
            print("  python scripts/build_crosscheck.py --apply", file=sys.stderr)
            print("Stale paths:", file=sys.stderr)
            for rel in changed:
                print(f"  - {rel}", file=sys.stderr)
            restore_snapshot(before, bridge_ids)
            return 1
        print("OK: Crosscheck artifacts match protocols-catalog/")
        return 0

    run_build(bridge_ids)
    print("Done: Crosscheck artifacts regenerated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())