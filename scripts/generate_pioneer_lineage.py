#!/usr/bin/env python3
"""Generate pioneer lineage JSON for dashboard."""
import json, yaml, pathlib, sys

ROOT = pathlib.Path(__file__).parent.parent
pioneers_dir = ROOT / "pioneers"
bridges_dir  = ROOT / "cross-domain"

lineage = {}

for f in sorted(pioneers_dir.glob("*.yaml")):
    try:
        p = yaml.safe_load(f.read_text(encoding="utf-8"))
        pid  = p.get("id") or f.stem
        seeded  = p.get("seeded_bridges", [])
        modern  = p.get("modern_open_problems", [])

        bridge_details = []
        for bid in seeded:
            matches = list(bridges_dir.rglob(f"{bid}.yaml"))
            if matches:
                try:
                    b = yaml.safe_load(matches[0].read_text(encoding="utf-8"))
                    domains = b.get("domains", b.get("fields", []))
                    bridge_details.append({
                        "id":           bid,
                        "title":        b.get("title", bid).strip(),
                        "domains":      domains,
                        "status":       b.get("status", "proposed"),
                        "bridge_claim": (b.get("bridge_claim", "") or "").strip()[:200],
                    })
                except Exception as exc:
                    print(f"  Warning: could not parse {matches[0].name}: {exc}", file=sys.stderr)
                    bridge_details.append({"id": bid, "title": bid, "domains": [], "status": "proposed", "bridge_claim": ""})
            else:
                print(f"  Warning: bridge not found: {bid}", file=sys.stderr)
                bridge_details.append({"id": bid, "title": bid, "domains": [], "status": "proposed", "bridge_claim": ""})

        # Normalise modern_open_problems — may be list of strings or list of dicts
        normalised_modern = []
        for m in (modern or []):
            if isinstance(m, str):
                normalised_modern.append({"title": m, "rationale": ""})
            elif isinstance(m, dict):
                normalised_modern.append({
                    "title":     str(m.get("title", "")).strip(),
                    "rationale": str(m.get("rationale", "")).strip()[:300],
                })

        lineage[pid] = {
            "id":                  pid,
            "name":                p.get("name", pid),
            "fields":              p.get("fields", p.get("primary_domains", [])),
            "key_insight":         (p.get("key_cross_domain_insight", "") or "").strip()[:300],
            "seeded_bridges":      bridge_details,
            "modern_open_problems": normalised_modern,
            "birth_year":          p.get("birth_year"),
            "death_year":          p.get("death_year"),
        }
    except Exception as e:
        print(f"Warning: {f.name}: {e}", file=sys.stderr)

out = ROOT / "api" / "v1" / "pioneer_lineage.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(lineage, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {len(lineage)} pioneer entries to {out}")
