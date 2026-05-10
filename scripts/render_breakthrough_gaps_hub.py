#!/usr/bin/env python3
"""
Inject the Breakthrough Gaps grid into dashboard/index.html from breakthrough-gaps/bg-*.yaml.

The hub previously showed a fixed subset of cards and drifted from the catalog. This script
keeps the contributor-facing section aligned with validated YAML.

Markers in dashboard/index.html:
  <!-- @hub-breakthrough-gaps-grid-begin -->
  <!-- @hub-breakthrough-gaps-grid-end -->

Usage:
  python scripts/render_breakthrough_gaps_hub.py           # dry-run (print count)
  python scripts/render_breakthrough_gaps_hub.py --apply   # rewrite dashboard/index.html
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DASHBOARD_HTML = ROOT / "dashboard" / "index.html"
GAPS_DIR = ROOT / "breakthrough-gaps"
BEGIN = "        <!-- @hub-breakthrough-gaps-grid-begin -->"
END = "        <!-- @hub-breakthrough-gaps-grid-end -->"

# Visual hints for cards (fallback ◆)
GAP_ICONS: dict[str, str] = {
    "bg-hydrogen-water-splitting": "💧",
    "bg-quantum-computing-fault-tolerant": "⚛️",
    "bg-scalable-quantum-computing": "⚛️",
    "bg-room-temperature-superconductivity": "🧲",
    "bg-mrna-programmable-medicine": "💉",
    "bg-carbon-direct-air-capture": "🌍",
    "bg-neural-interface-bandwidth": "🧠",
    "bg-controlled-nuclear-fusion-power": "☀️",
    "bg-fusion-energy-ignition": "☀️",
    "bg-antibiotic-resistance-crisis": "🦠",
    "bg-alzheimers-mechanism": "🧬",
    "bg-photosynthesis-efficiency": "🌿",
    "bg-aging-reversal-mechanisms": "⏳",
    "bg-consciousness-neural-correlates": "💭",
    "bg-de-novo-protein-design": "🧪",
    "bg-neuromorphic-computing-at-scale": "🔌",
    "bg-ocean-plastic-remediation": "🌊",
    "bg-post-treatment-lyme-disease-syndrome": "🩺",
    "bg-programmable-matter": "✨",
    "bg-scientific-knowledge-overload": "📚",
    "bg-soil-microbiome-engineering": "🌱",
    "bg-universal-cancer-early-detection": "🔬",
    "bg-whole-brain-neural-recording": "📡",
    "bg-whole-earth-climate-model": "🛰️",
}

GH_BASE = "https://github.com/KR8ZYSHO3/Universal-Science-Discovery/blob/main/breakthrough-gaps"


def load_gap(path: Path) -> dict | None:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        print(f"  WARNING: could not parse {path}: {exc}", file=sys.stderr)
        return None
    if not data.get("id"):
        return None
    return data


def excerpt(text: str, max_len: int = 220) -> str:
    s = " ".join((text or "").split())
    if len(s) <= max_len:
        return s
    return s[: max_len - 1].rstrip() + "…"


def sort_key(entry: dict) -> tuple[int, int, str]:
    pot = (entry.get("world_reshaping_potential") or "").lower()
    order = {"transformative": 0, "significant": 1, "moderate": 2}.get(pot, 3)
    trl = entry.get("current_trl")
    trl_n = int(trl) if isinstance(trl, int) else 0
    title = entry.get("title") or entry.get("id", "")
    return (order, -trl_n, title.lower())


def render_cards(entries: list[dict]) -> str:
    lines: list[str] = []
    for d in sorted(entries, key=sort_key):
        gid = d["id"]
        title = html.escape((d.get("title") or gid).strip())
        trl = d.get("current_trl", "?")
        trl_label = html.escape(str(trl)) if isinstance(trl, int) else "?"
        desc_raw = d.get("breakthrough_description") or ""
        desc = html.escape(excerpt(desc_raw))
        icon = GAP_ICONS.get(gid, "◆")
        gh_url = f"{GH_BASE}/{gid}.yaml"
        lines.append(
            f'''        <a href="{gh_url}" target="_blank" rel="noopener" class="gap-hub-card"
           style="text-decoration:none;color:inherit;display:block;background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.3);border-radius:12px;padding:1.5rem;transition:transform 0.15s ease,border-color 0.15s ease;"
           onmouseover="this.style.transform='translateY(-2px)';this.style.borderColor='rgba(239,68,68,0.55)';"
           onmouseout="this.style.transform='';this.style.borderColor='rgba(239,68,68,0.3)';">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.75rem;">
            <span style="font-size:1.5rem;" aria-hidden="true">{icon}</span>
            <span style="background:rgba(239,68,68,0.2);color:#fca5a5;padding:0.2rem 0.6rem;border-radius:999px;font-size:0.75rem;">TRL {trl_label}</span>
          </div>
          <h3 style="color:#fca5a5;margin:0 0 0.5rem;font-size:1rem;">{title}</h3>
          <p style="color:#94a3b8;font-size:0.85rem;margin:0;line-height:1.45;">{desc}</p>
        </a>'''
        )
    return "\n".join(lines)


def inject(html_text: str, fragment: str) -> str:
    if BEGIN not in html_text or END not in html_text:
        raise SystemExit(f"Markers missing in {DASHBOARD_HTML}: need {BEGIN!r} … {END!r}")
    pattern = re.compile(
        re.escape(BEGIN) + r".*?" + re.escape(END),
        re.DOTALL,
    )
    new_block = BEGIN + "\n" + fragment + "\n" + END
    updated, n = pattern.subn(new_block, html_text, count=1)
    if n != 1:
        raise SystemExit("Could not replace exactly one breakthrough gaps grid block.")
    return updated


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="Write dashboard/index.html")
    args = ap.parse_args()

    entries: list[dict] = []
    for p in sorted(GAPS_DIR.glob("bg-*.yaml")):
        d = load_gap(p)
        if d:
            entries.append(d)

    if not entries:
        print("No breakthrough gap YAML files found.", file=sys.stderr)
        return 1

    fragment = render_cards(entries)
    print(f"Breakthrough gaps: {len(entries)} entries -> hub grid")

    if not args.apply:
        return 0

    raw = DASHBOARD_HTML.read_text(encoding="utf-8")
    DASHBOARD_HTML.write_text(inject(raw, fragment), encoding="utf-8", newline="\n")
    print(f"Updated {DASHBOARD_HTML.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
