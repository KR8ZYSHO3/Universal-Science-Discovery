#!/usr/bin/env python3
"""Export orphan-unknowns panel JSON for the contributor hub (DISC-03).

Unknowns with no graph edges to bridges or hypotheses — priority contribution
targets. Complements ``export_orphan_xref_panel.py`` (broken xref IDs).

Usage (from repo root)::

    python scripts/export_orphan_unknowns_panel.py

See ``docs/DEV_DASHBOARD.md`` for when to regenerate.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from find_orphan_unknowns import ROOT, analyze_orphan_unknowns  # noqa: E402

API_OUT = ROOT / "api" / "v1" / "orphan_unknowns_panel.json"
ITEM_CAP = 50


def main() -> int:
    try:
        analysis = analyze_orphan_unknowns()
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    orphans = list(analysis["orphans"])
    items = orphans[:ITEM_CAP]
    generated = (
        datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    )
    payload = {
        "generated_at": generated,
        "source": (
            "scripts/export_orphan_unknowns_panel.py "
            "(docs/knowledge_graph.json orphan unknown scan; same logic as find_orphan_unknowns.py)"
        ),
        "meta": {
            "total_unknowns": analysis["total_unknowns"],
            "connected_unknowns": analysis["connected_unknowns"],
            "orphan_count": analysis["orphan_count"],
            "item_cap": ITEM_CAP,
        },
        "items": items,
    }
    API_OUT.parent.mkdir(parents=True, exist_ok=True)
    API_OUT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {API_OUT.relative_to(ROOT)} "
        f"({len(items)} items, {analysis['orphan_count']} orphans total)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())