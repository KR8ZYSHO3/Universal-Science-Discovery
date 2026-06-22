#!/usr/bin/env python3
"""Generate index.html landing pages for Crosscheck repro bundles (GitHub Pages)."""
from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path

import yaml

from crosscheck_browser import browser_runner_script, colab_url

REPO = "KR8ZYSHO3/Universal-Science-Discovery"
ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "protocols-catalog"


def load_protocols() -> list[dict]:
    protos: list[dict] = []
    for path in sorted(CATALOG.rglob("p-b-*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            continue
        bundle = str(data.get("repro_bundle", "")).strip().rstrip("/")
        if not bundle:
            continue
        data["_catalog_path"] = path.relative_to(ROOT).as_posix()
        data["_bundle_dir"] = ROOT / bundle
        protos.append(data)
    return protos


def script_name(bundle_dir: Path) -> str:
    for py in sorted(bundle_dir.glob("*.py")):
        if py.name != "__init__.py":
            return py.name
    return "run.py"





def runner_section(proto_id: str, runner_js: str) -> str:
    e = html.escape
    return f"""
  <h2>Run Crosscheck in your browser</h2>
  <div id=\"crosscheck-runner\" class=\"runner\" data-protocol=\"{e(proto_id)}\">
    <p class=\"runner-lead\">One-click demo — same algorithm as the Python repro. Results stream live;
    clone the repo for full-precision verification.</p>
    <button type=\"button\" data-action=\"run\">Run Crosscheck</button>
    <span class=\"result-badge\" data-role=\"result-badge\" hidden></span>
    <div class=\"progress\" data-role=\"progress\" hidden><div class=\"progress-bar\" data-role=\"progress-bar\"></div></div>
    <pre class=\"runner-output\" data-role=\"output\"></pre>
  </div>
  <script src=\"{e(runner_js)}\"></script>
  <script src=\"../_shared/crosscheck-runner.js\"></script>
"""


def colab_section(colab_href: str) -> str:
    e = html.escape
    return f"""
  <h2>Run in Google Colab</h2>
  <p class=\"runner-lead\">No local Python setup — opens a notebook that clones the repo and runs the repro.</p>
  <p><a class=\"colab-btn\" href=\"{e(colab_href)}\" target=\"_blank\" rel=\"noopener\">Open in Colab</a></p>
"""


def note_section(has_browser: bool, has_colab: bool) -> str:
    if has_browser:
        return """  <div class=\"note\">
    <strong>Try the in-browser runner below</strong> for a live demo, or clone this folder for
    the canonical Python repro (source of truth for verification).
  </div>"""
    if has_colab:
        return """  <div class=\"note\">
    <strong>Open in Colab below</strong> for a one-click cloud run (requires networkx), or clone this
    folder for the canonical Python repro.
  </div>"""
    return """  <div class=\"note\">
    This page is served on GitHub Pages for discovery. <strong>Run the repro on your machine</strong>
    (clone the repo or download this folder) — the script is not executed in the browser.
  </div>"""


def render_page(proto: dict) -> str:
    pid = proto["id"]
    title = " ".join(str(proto.get("title", pid)).split())
    bridge = proto.get("source_bridge", "")
    bundle = str(proto.get("repro_bundle", "")).strip().rstrip("/")
    bundle_dir: Path = proto["_bundle_dir"]
    script = script_name(bundle_dir)
    catalog_path = proto["_catalog_path"]
    tier = proto.get("feasibility_tier", "desktop")
    runtime = proto.get("estimated_runtime", "a few minutes")
    pred = " ".join(str(proto.get("falsifiable_prediction", "")).split())
    if len(pred) > 400:
        pred = pred[:397] + "..."

    dash = "https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/"
    gh_tree = f"https://github.com/{REPO}/tree/main/{bundle}"
    gh_yaml = f"https://github.com/{REPO}/blob/main/{catalog_path}"
    explainer = (
        f"https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/"
        f"explainers/{bridge}.html#crosscheck"
        if bridge
        else dash
    )

    runner_js = browser_runner_script(bundle_dir, pid)
    has_browser = runner_js is not None
    colab_href = colab_url(bundle_dir, pid)
    has_colab = colab_href is not None

    e = html.escape
    runner_html = runner_section(pid, runner_js) if has_browser else ""
    colab_html = colab_section(colab_href) if has_colab and not has_browser else ""
    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <meta name=\"color-scheme\" content=\"dark\" />
  <title>Crosscheck repro — {e(pid)}</title>
  <style>
    :root {{
      --bg: #060d1a; --text: #ddeeff; --muted: #6b8aac; --accent: #4f9cf9;
      --teal: #22d3b8; --border: rgba(79,156,249,0.2); --mono: ui-monospace, monospace;
    }}
    body {{ font-family: system-ui, sans-serif; background: var(--bg); color: var(--text);
      line-height: 1.6; max-width: 46rem; margin: 0 auto; padding: 2rem 1.25rem 4rem; }}
    a {{ color: var(--accent); }}
    h1 {{ font-size: 1.35rem; margin-bottom: .25rem; }}
    h2 {{ font-size: 1.05rem; margin-top: 1.75rem; }}
    .meta {{ color: var(--muted); font-size: .9rem; margin-bottom: 1.5rem; }}
    pre {{ background: #0b1527; border: 1px solid var(--border); border-radius: 10px;
      padding: 1rem; overflow-x: auto; font-family: var(--mono); font-size: .85rem; }}
    .note {{ background: rgba(34,211,184,0.08); border: 1px solid rgba(34,211,184,0.25);
      border-radius: 10px; padding: .85rem 1rem; font-size: .9rem; margin: 1.25rem 0; }}
    .links {{ display: flex; flex-wrap: wrap; gap: .65rem; margin-top: 1.5rem; font-size: .88rem; }}
    .pill {{ display: inline-block; padding: .2rem .55rem; border-radius: 999px;
      border: 1px solid var(--border); color: var(--teal); font-size: .75rem; }}
    .runner {{ margin: 1.25rem 0 1.75rem; }}
    .runner-lead {{ color: var(--muted); font-size: .9rem; margin-bottom: .85rem; }}
    .runner button {{ background: var(--accent); color: #04101f; border: none; border-radius: 8px;
      padding: .55rem 1.1rem; font-weight: 600; font-size: .92rem; cursor: pointer; }}
    .runner button:disabled {{ opacity: .55; cursor: wait; }}
    .runner-output {{ min-height: 6rem; margin-top: .85rem; white-space: pre-wrap; }}
    .progress {{ height: 4px; background: rgba(79,156,249,0.15); border-radius: 999px;
      margin-top: .75rem; overflow: hidden; }}
    .progress-bar {{ height: 100%; width: 0; background: var(--teal); transition: width .2s ease; }}
    .result-badge {{ display: inline-block; margin-left: .65rem; padding: .15rem .5rem;
      border-radius: 6px; font-size: .75rem; font-weight: 700; letter-spacing: .03em; }}
    .result-badge.confirmed {{ background: rgba(34,211,184,0.2); color: var(--teal); }}
    .result-badge.inconclusive {{ background: rgba(251,191,36,0.15); color: #fbbf24; }}
    .result-badge.error {{ background: rgba(248,113,113,0.15); color: #f87171; }}
    .colab-btn {{ display: inline-block; background: #f9ab00; color: #1a1200; font-weight: 600;
      padding: .5rem 1rem; border-radius: 8px; text-decoration: none; font-size: .92rem; }}
    .colab-btn:hover {{ filter: brightness(1.05); }}
  </style>
</head>
<body>
  <p class=\"pill\">USDR Crosscheck · {e(tier)}</p>
  <h1>{e(title)}</h1>
  <p class=\"meta\">Protocol <code>{e(pid)}</code> · bridge <code>{e(bridge)}</code></p>
  <p>{e(pred)}</p>
{note_section(has_browser, has_colab)}
{runner_html}
{colab_html}
  <h2>Run locally</h2>
  <pre>git clone https://github.com/{REPO}.git
cd Universal-Science-Discovery/{bundle}
pip install -r requirements.txt
python {script}</pre>
  <p>Estimated runtime: {e(str(runtime))}. Exit code <code>0</code> = prediction within tolerance;
  <code>1</code> = falsified at stated precision.</p>
  <div class=\"links\">
    <a href=\"README.md\">README</a>
    <a href=\"{e(gh_tree)}\">Source on GitHub</a>
    <a href=\"{e(gh_yaml)}\">Protocol YAML</a>
    <a href=\"{e(explainer)}\">Bridge explainer</a>
    <a href=\"{e(dash)}\">USDR dashboard</a>
  </div>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    written = 0
    for proto in load_protocols():
        out = proto["_bundle_dir"] / "index.html"
        content = render_page(proto)
        if args.dry_run:
            print(f"would write {out.relative_to(ROOT)}")
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")
        written += 1
    if not written and not args.dry_run:
        print("no repro bundles found", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
