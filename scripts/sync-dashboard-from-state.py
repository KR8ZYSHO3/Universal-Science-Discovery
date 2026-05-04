#!/usr/bin/env python3
"""
Sync embedded dashboard constants from `.planning/STATE.md` into `canvases/Progress.canvas.tsx`.

Usage (repo root):
  python scripts/sync-dashboard-from-state.py           # rewrite canvas markers in place
  python scripts/sync-dashboard-from-state.py --dry-run # print generated block only

Requires CPython 3.9+ (stdlib only). Section titles must match STATE.md `##` headers:
  Last updated, Current focus, Active git branches / PRs, Shipped recently,
  Blocked / needs human, Next actions (max 5)

Bullets are lines starting with `- ` under each section. For *Last updated*, the first
non-empty line after the header is also accepted if it is not a bullet.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = REPO_ROOT / ".planning" / "STATE.md"
CANVAS_PATH = REPO_ROOT / "canvases" / "Progress.canvas.tsx"

BEGIN = "// @sync-dashboard-begin"
END = "// @sync-dashboard-end"


def parse_state(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    buf: list[str] = []

    def flush() -> None:
        nonlocal current, buf
        if current is not None:
            sections[current] = buf[:]
        buf = []

    for line in text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            flush()
            current = m.group(1).strip().lower()
            buf = []
            continue
        if current is None:
            continue
        s = line.strip()
        if s.startswith("- "):
            buf.append(s[2:].strip())
        elif s and not s.startswith("#") and current == "last updated" and not buf:
            buf.append(s)

    flush()
    return sections


def build_ts_object(parsed: dict[str, list[str]]) -> str:
    def items(title: str) -> list[str]:
        return parsed.get(title, [])

    lu = items("last updated")
    last_updated = lu[0] if lu else ""
    bundles = [
        ("currentFocus", items("current focus")),
        ("activeBranches", items("active git branches / prs")),
        ("shippedRecently", items("shipped recently")),
        ("blocked", items("blocked / needs human")),
        ("nextActions", items("next actions (max 5)")[:5]),
    ]
    lines = [
        "const dashboardSnapshot = {",
        f"  lastUpdated: {json.dumps(last_updated, ensure_ascii=False)},",
    ]
    for key, arr in bundles:
        inner = ",\n    ".join(json.dumps(x, ensure_ascii=False) for x in arr)
        lines.append(f"  {key}: [\n    {inner}\n  ],")
    lines.append("} as const;")
    return "\n".join(lines)


def replace_block(canvas: str, generated: str) -> str:
    if BEGIN not in canvas or END not in canvas:
        raise SystemExit(f"Markers missing in {CANVAS_PATH}: need {BEGIN} ... {END}")
    pre, rest = canvas.split(BEGIN, 1)
    _, post = rest.split(END, 1)
    new_inner = f"{BEGIN}\n{generated}\n{END}"
    return pre + new_inner + post


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="print TS block only")
    args = ap.parse_args()

    if not STATE_PATH.is_file():
        print(f"Missing {STATE_PATH}", file=sys.stderr)
        sys.exit(1)

    raw = STATE_PATH.read_text(encoding="utf-8")
    parsed = parse_state(raw)
    ts_block = build_ts_object(parsed)

    if args.dry_run:
        print(ts_block)
        return

    if not CANVAS_PATH.is_file():
        print(f"Missing {CANVAS_PATH}", file=sys.stderr)
        sys.exit(1)

    canvas = CANVAS_PATH.read_text(encoding="utf-8")
    updated = replace_block(canvas, ts_block)
    CANVAS_PATH.write_text(updated, encoding="utf-8", newline="\n")
    print(f"Updated embedded snapshot in {CANVAS_PATH}")


if __name__ == "__main__":
    main()
