#!/usr/bin/env python3
"""Promote staged *unknowns only* into unknowns-catalog/. Never moves bridges.

Default is dry-run. Human still passes --apply after skimming the briefing.

Usage:
  python scripts/harvesters/promote_unknowns.py
  python scripts/harvesters/promote_unknowns.py --apply
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import shutil
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_STAGE = ROOT / "drafts" / "unknowns_harvest"


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} is not a mapping")
    return data


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--stage", default=str(DEFAULT_STAGE.relative_to(ROOT)))
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    stage = (ROOT / args.stage).resolve()
    if not stage.exists():
        print(f"[promote-unknowns] no stage dir {stage}")
        return 0
    schema = yaml.safe_load((ROOT / "schemas" / "unknown.yaml").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    files = sorted(stage.rglob("u-*.yaml"))
    errors: list[str] = []
    plans: list[tuple[Path, Path]] = []
    for path in files:
        inst = load_yaml(path)
        reviewed = inst.get("last_reviewed")
        if isinstance(reviewed, dt.date):
            inst["last_reviewed"] = reviewed.isoformat()
        for err in validator.iter_errors(inst):
            loc = "/".join(str(x) for x in err.absolute_path) or "(root)"
            errors.append(f"{path.relative_to(ROOT)} [{loc}]: {err.message}")
        uid = str(inst.get("id") or "")
        if not uid.startswith("u-"):
            errors.append(f"{path}: id must start with u-")
        rel = path.relative_to(stage)
        target = ROOT / "unknowns-catalog" / rel
        plans.append((path, target))
    if errors:
        print("[promote-unknowns] validation failed:")
        for e in errors:
            print(f"  - {e}")
        return 1
    collisions = [
        f"{s.relative_to(ROOT)} -> {d.relative_to(ROOT)}"
        for s, d in plans
        if d.exists() and file_hash(s) != file_hash(d)
    ]
    if collisions:
        print("[promote-unknowns] collisions:")
        for c in collisions:
            print(f"  - {c}")
        return 1
    print(f"[promote-unknowns] OK. planned unknowns={len(plans)}")
    print("Bridges are not in this command. Wave Factory still needs a human.")
    if not args.apply:
        print("[promote-unknowns] dry-run. Pass --apply to copy into unknowns-catalog/.")
        return 0
    moved = 0
    for src, dst in plans:
        if dst.exists() and file_hash(src) == file_hash(dst):
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        moved += 1
        print(f"  + {dst.relative_to(ROOT)}")
    print(f"[promote-unknowns] copied {moved} unknowns")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
