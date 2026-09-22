#!/usr/bin/env python3
"""Write api/v1/frontier.json — a small rail of live unsolvables for the hub."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "api" / "v1" / "frontier.json"


def load_unknowns() -> list[dict]:
    rows: list[dict] = []
    for path in (ROOT / "unknowns-catalog").rglob("u-*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not isinstance(data, dict) or data.get("status") != "open":
            continue
        uid = str(data.get("id") or path.stem)
        discs = data.get("disciplines") or []
        if not isinstance(discs, list):
            discs = [discs] if discs else []
        rows.append(
            {
                "id": uid,
                "title": " ".join(str(data.get("title") or uid).split()),
                "domain": str(discs[0]) if discs else path.parent.name,
                "harvested": uid.startswith("u-gap-")
                or "HARVESTED" in str(data.get("summary") or ""),
            }
        )
    return rows


def pick(rows: list[dict], limit: int = 8) -> list[dict]:
    harvested = [r for r in rows if r.get("harvested")]
    rest = [r for r in rows if not r.get("harvested")]
    seen_domain: set[str] = set()
    out: list[dict] = []
    for pool in (harvested, rest):
        for row in pool:
            if len(out) >= limit:
                break
            dom = row["domain"]
            if dom in seen_domain and not row.get("harvested"):
                continue
            seen_domain.add(dom)
            out.append({k: row[k] for k in ("id", "title", "domain", "harvested")})
        if len(out) >= limit:
            break
    return out[:limit]


def main() -> int:
    items = pick(load_unknowns())
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps({"count": len(items), "items": items}, indent=2, ensure_ascii=False)
        + "\n",
        encoding="utf-8",
    )
    print(f"[frontier] wrote {OUT.relative_to(ROOT)} items={len(items)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
