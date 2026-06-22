#!/usr/bin/env python3
"""
Inject the Crosscheck protocols grid into dashboard/index.html from protocols-catalog/.

Markers in dashboard/index.html:
  <!-- @hub-crosscheck-grid-begin -->
  <!-- @hub-crosscheck-grid-end -->

Usage:
  python scripts/render_crosscheck_hub.py           # dry-run
  python scripts/render_crosscheck_hub.py --apply   # rewrite dashboard/index.html
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

import yaml

from crosscheck_browser import browser_runner_script, colab_url, run_mode

ROOT = Path(__file__).resolve().parent.parent
DASHBOARD_HTML = ROOT / "dashboard" / "index.html"
CATALOG = ROOT / "protocols-catalog"
BEGIN = "        <!-- @hub-crosscheck-grid-begin -->"
END = "        <!-- @hub-crosscheck-grid-end -->"
PAGES = "https://kr8zysho3.github.io/Universal-Science-Discovery"


def load_protocols() -> list[dict]:
    protos: list[dict] = []
    for path in sorted(CATALOG.rglob("p-b-*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            continue
        bundle = str(data.get("repro_bundle", "")).strip().rstrip("/")
        if not bundle:
            continue
        data["_bundle_dir"] = ROOT / bundle
        protos.append(data)
    return protos


def short_title(title: str, max_len: int = 120) -> str:
    s = " ".join(title.split())
    if len(s) <= max_len:
        return s
    return s[: max_len - 1].rstrip() + "…"


def status_style(status: str) -> tuple[str, str]:
    styles = {
        "executed": ("rgba(34,211,184,0.2)", "#5eead4"),
        "confirmed": ("rgba(34,211,184,0.35)", "#2dd4bf"),
        "falsified": ("rgba(248,113,113,0.2)", "#fca5a5"),
        "ready": ("rgba(79,156,249,0.2)", "#93c5fd"),
        "draft": ("rgba(148,163,184,0.15)", "#94a3b8"),
    }
    return styles.get(status, styles["draft"])


def run_link(proto: dict) -> tuple[str, str]:
    pid = proto["id"]
    bundle = str(proto.get("repro_bundle", "")).strip().rstrip("/")
    bundle_dir: Path = proto["_bundle_dir"]
    repro_href = f"{PAGES}/{bundle}/index.html"
    mode = run_mode(pid, bundle_dir)
    if mode == "browser":
        return repro_href, "Run in browser"
    if mode == "colab":
        href = colab_url(bundle_dir, pid)
        return href or repro_href, "Open in Colab"
    return repro_href, "Run repro"


def render_cards(protos: list[dict]) -> str:
    lines: list[str] = []
    for proto in sorted(protos, key=lambda p: p.get("id", "")):
        pid = proto["id"]
        title = html.escape(short_title(str(proto.get("title", pid))))
        status = str(proto.get("status", "draft"))
        bridge = str(proto.get("source_bridge", ""))
        tier = html.escape(str(proto.get("feasibility_tier", "desktop")))
        bg, fg = status_style(status)
        run_href, run_label = run_link(proto)
        explainer = (
            f"{PAGES}/dashboard/explainers/{html.escape(bridge)}.html#crosscheck"
            if bridge
            else f"{PAGES}/dashboard/"
        )
        lines.append(
            f"""        <article class="crosscheck-hub-card" style="background:rgba(79,156,249,0.06);border:1px solid rgba(79,156,249,0.22);border-radius:12px;padding:1.15rem 1.25rem;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:.75rem;flex-wrap:wrap;margin-bottom:.55rem;">
            <h3 style="margin:0;font-size:.95rem;line-height:1.35;font-weight:600;">{title}</h3>
            <span style="background:{bg};color:{fg};padding:.15rem .55rem;border-radius:999px;font-size:.7rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;">{html.escape(status)}</span>
          </div>
          <p style="margin:0 0 .65rem;font-size:.78rem;color:var(--muted);">Protocol <code style="font-size:.75rem;">{html.escape(pid)}</code> · {tier}</p>
          <div style="display:flex;flex-wrap:wrap;gap:.5rem;font-size:.82rem;">
            <a href="{html.escape(run_href)}" style="color:var(--accent2);font-weight:600;">{html.escape(run_label)} →</a>
            <a href="{explainer}" style="color:var(--muted);">Bridge explainer</a>
          </div>
        </article>"""
        )
    return "\n".join(lines)


def apply(html_text: str, cards: str) -> str:
    pattern = re.compile(
        re.escape(BEGIN) + r".*?" + re.escape(END),
        re.DOTALL,
    )
    block = f"{BEGIN}\n{cards}\n{END}"
    if not pattern.search(html_text):
        print("ERROR: markers not found in dashboard/index.html", file=sys.stderr)
        raise SystemExit(1)
    return pattern.sub(block, html_text, count=1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    protos = load_protocols()
    cards = render_cards(protos)
    print(f"Crosscheck protocols: {len(protos)}")
    if not args.apply:
        print("dry-run (use --apply to write dashboard/index.html)")
        return 0
    text = DASHBOARD_HTML.read_text(encoding="utf-8")
    DASHBOARD_HTML.write_text(apply(text, cards), encoding="utf-8")
    print(f"wrote {DASHBOARD_HTML.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())