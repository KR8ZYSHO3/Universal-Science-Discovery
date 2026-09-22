#!/usr/bin/env python3
"""Write a Crosscheck stdout RESULT token onto protocol YAML (and optionally the hub).

Does **not** set status: confirmed. That remains a human promotion.
INCONCLUSIVE is a first-class last_run_result, not a missing result.

Usage:
  python scripts/apply_crosscheck_result.py --protocol p-b-percolation-oncology-gcc --from-stdout run.txt
  python scripts/apply_crosscheck_result.py --protocol p-b-percolation-oncology-gcc --result INCONCLUSIVE --apply
  python scripts/apply_crosscheck_result.py --protocol ID --from-stdout run.txt --apply --refresh-hub
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "protocols-catalog"
RESULT_RE = re.compile(r"^RESULT:\s*(CONFIRMED|INCONCLUSIVE|FALSIFIED)\b", re.MULTILINE)
VALID = frozenset({"CONFIRMED", "INCONCLUSIVE", "FALSIFIED"})


def parse_result(text: str) -> Optional[str]:
    matches = RESULT_RE.findall(text or "")
    if not matches:
        return None
    return matches[-1]


def find_protocol(protocol_id: str) -> Path:
    hits = list(CATALOG.rglob(f"{protocol_id}.yaml"))
    if not hits:
        raise FileNotFoundError(f"no protocol YAML for {protocol_id}")
    if len(hits) > 1:
        raise RuntimeError(f"multiple YAML files for {protocol_id}: {hits}")
    return hits[0]


def upsert_field(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf"(?m)^{re.escape(key)}:\s*.*$")
    line = f"{key}: {value}"
    if pattern.search(text):
        return pattern.sub(line, text, count=1)
    status = re.compile(r"(?m)^(status:\s*.*)$")
    if status.search(text):
        return status.sub(r"\1\n" + line, text, count=1)
    return text.rstrip() + f"\n{line}\n"


def apply_result(
    yaml_text: str,
    result: str,
    when: str,
    note: str = "",
) -> str:
    if result not in VALID:
        raise ValueError(f"invalid RESULT {result!r}")
    out = upsert_field(yaml_text, "last_run_result", result)
    out = upsert_field(out, "last_run_at", f'"{when}"')
    if note:
        quoted = note.replace('"', "'")
        out = upsert_field(out, "last_run_note", f'"{quoted}"')
    return out


def refresh_hub() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "render_crosscheck_hub.py"), "--apply"],
        cwd=ROOT,
        check=True,
    )


def parse_args(argv=None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--protocol", required=True)
    p.add_argument("--result", choices=sorted(VALID))
    p.add_argument("--from-stdout", type=Path)
    p.add_argument("--note", default="")
    p.add_argument("--apply", action="store_true")
    p.add_argument("--refresh-hub", action="store_true")
    return p.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    result = args.result
    if args.from_stdout:
        text = args.from_stdout.read_text(encoding="utf-8")
        parsed = parse_result(text)
        if not parsed:
            print("ERROR: no RESULT: CONFIRMED|INCONCLUSIVE|FALSIFIED in stdout", file=sys.stderr)
            print("Refusing to invent CONFIRMED.", file=sys.stderr)
            return 2
        if result and result != parsed:
            print(f"ERROR: --result {result} disagrees with stdout {parsed}", file=sys.stderr)
            return 2
        result = parsed
    if not result:
        print("ERROR: pass --result or --from-stdout", file=sys.stderr)
        return 2
    path = find_protocol(args.protocol)
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    original = path.read_text(encoding="utf-8")
    updated = apply_result(original, result, today, args.note)
    print(f"{path.relative_to(ROOT)}  last_run_result={result}  last_run_at={today}")
    print("YAML status is unchanged (human promotion only).")
    if not args.apply:
        print("dry-run (pass --apply to write)")
        return 0
    path.write_text(updated, encoding="utf-8")
    if args.refresh_hub:
        refresh_hub()
        print("refreshed dashboard Crosscheck grid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
