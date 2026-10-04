#!/usr/bin/env python3
"""Generate index.html landing pages for Crosscheck repro bundles (GitHub Pages)."""
from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path

import yaml

from crosscheck_browser import browser_runner_script, colab_url, visitor_title

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





def runner_lead(proto_id: str) -> str:
    if proto_id == "p-b-habitat-percolation-ecology-fss":
        return (
            "Press Run. One landscape, 48 patches wide, fills over about 15 seconds and then repeats. "
            "Colors name connected habitats. They are not a measurement. The chart is 400 real runs "
            "at each size. The result is that fit, not a preset."
        )
    return (
        "One-click demo — cheaper trial budget than the Python repro. Results stream live; "
        "clone the repo for full-precision verification."
    )


def habitat_stage() -> str:
    return """
  <section class=\"perc-stage\" id=\"perc-stage\">
    <div class=\"perc-grid\">
      <div class=\"lattice-wrap\">
        <canvas id=\"perc-lattice\" width=\"64\" height=\"64\" aria-label=\"Habitat patches filling a landscape\"></canvas>
      </div>
      <div class=\"perc-copy\">
        <h2>What you are watching</h2>
        <p id=\"perc-story\">Press Run. One real landscape fills over about 15 seconds, then starts over. Each color is a label for one connected habitat, so you can tell them apart. The color is not height, density, or quality. Gold, at the end, is only the habitat that wrapped around the landscape. Dark cells are empty. This picture is not the average, and it is not a photograph of a real park.</p>
        <ul class=\"perc-key\">
          <li><span class=\"swatch dark\"></span> Empty patch</li>
          <li><span class=\"swatch c1\"></span><span class=\"swatch c2\"></span><span class=\"swatch c3\"></span> Connected habitats. The color is only a name.</li>
          <li><span class=\"swatch gold\"></span> The habitat that wrapped around</li>
        </ul>
        <p id=\"perc-readout\" class=\"perc-readout\">Waiting.</p>
        <div class=\"perc-meter\" aria-hidden=\"true\"><div id=\"perc-meter-fill\"></div><span class=\"perc-meter-mark\" title=\"Infinite-landscape threshold\"></span></div>
        <p class=\"perc-meter-label">Filled fraction. The gold tick is 59.27%.</p>
      </div>
    </div>
    <h2 class=\"perc-evidence-title\">The evidence</h2>
    <p class=\"perc-chart-caption\">Each dot is the average breaking point from 400 runs at that width. The number on the dot is the filled percent where the habitat wrapped. The gold dashed line is 59.3%, where a huge landscape breaks. When the run finishes, the teal line is the curve fitted to these dots.</p>
    <ul class=\"perc-legend\">
      <li><span class=\"swatch c1\"></span> Measured breaking point</li>
      <li><span class=\"swatch gold\"></span> Huge landscape, 59.3%</li>
      <li><span class=\"swatch teal\"></span> Fitted curve</li>
    </ul>
    <canvas id=\"perc-chart\" class=\"perc-chart\" aria-label=\"Chart of breaking point versus landscape width. Each dot is 400 runs.\"></canvas>
  </section>
"""


def habitat_css() -> str:
    return """
    body.habitat-demo { max-width: 72rem; }
    .perc-stage { margin: 1.25rem 0 0.5rem; }
    .perc-grid { display: grid; grid-template-columns: minmax(240px, 1.1fr) minmax(260px, 0.9fr); gap: 1.25rem; align-items: start; }
    @media (max-width: 800px) { .perc-grid { grid-template-columns: 1fr; } }
    .lattice-wrap { background: #070f1e; border: 1px solid rgba(79,156,249,0.35); border-radius: 16px; padding: .6rem; box-shadow: 0 0 0 1px rgba(34,211,184,0.05), 0 20px 60px rgba(0,0,0,.35); }
    #perc-stage.is-wrapped .lattice-wrap { box-shadow: 0 0 0 2px #fbbf24, 0 0 40px rgba(251,191,36,.35); }
    #perc-lattice { width: 100%; height: auto; image-rendering: pixelated; display: block; border-radius: 8px; background: #081020; }
    .perc-copy h2 { margin-top: 0; }
    #perc-story { font-size: .95rem; }
    .perc-readout { font-family: var(--mono); color: var(--teal); min-height: 1.4rem; }
    .perc-meter { position: relative; height: 10px; border-radius: 999px; background: #101a2e; border: 1px solid var(--border); overflow: hidden; }
    #perc-meter-fill { height: 100%; width: 0; background: linear-gradient(90deg, #1d4ed8, #22d3b8); }
    .perc-meter-mark { position: absolute; top: -3px; bottom: -3px; left: 59.27%; width: 2px; background: #fbbf24; }
    .perc-meter-label { color: var(--muted); font-size: .78rem; margin-top: .35rem; }
    .perc-chart { width: 100%; height: 250px; margin-top: 1rem; background: #070f1e; border: 1px solid var(--border); border-radius: 12px; }
    .perc-key { list-style: none; padding: 0; margin: .4rem 0 .8rem; font-size: .86rem; color: var(--muted); }
    .perc-key li { display: flex; align-items: center; gap: .4rem; margin: .28rem 0; }
    .swatch { width: 14px; height: 14px; border-radius: 3px; display: inline-block; flex: 0 0 auto; }
    .swatch.dark { background: #081020; border: 1px solid rgba(107,138,172,.5); }
    .swatch.c1 { background: rgb(0,114,178); }
    .swatch.c2 { background: rgb(0,158,115); }
    .swatch.c3 { background: rgb(213,94,0); }
    .swatch.gold { background: rgb(245,193,108); }
    .swatch.teal { background: #22d3b8; }
    body.habitat-demo h1 { font-size: 1.7rem; line-height: 1.25; max-width: 22em; }
    .formula { color: var(--muted); font-family: var(--mono); font-size: .82rem; margin: 0 0 1rem; }
    .perc-evidence-title { margin: 1.35rem 0 .25rem; }
    .perc-chart-caption { color: var(--text); font-size: .95rem; margin: 0 0 .45rem; }
    .perc-legend { list-style: none; display: flex; flex-wrap: wrap; gap: .35rem 1rem; padding: 0; margin: 0 0 .55rem; font-size: .86rem; color: var(--muted); }
    .perc-legend li { display: flex; align-items: center; gap: .4rem; }
    .perc-conclusion { margin: 1rem 0 1.25rem; border-radius: 14px; padding: 1rem 1.15rem 1.05rem; border: 1px solid var(--border); background: rgba(79,156,249,0.08); }
    .perc-conclusion-title { font-size: 1.28rem; font-weight: 700; margin: 0 0 .45rem; line-height: 1.35; }
    .perc-conclusion-body { margin: 0; font-size: 1rem; }
    .perc-conclusion.confirmed { border-color: rgba(34,211,184,.6); background: rgba(34,211,184,.12); }
    .perc-conclusion.inconclusive { border-color: rgba(251,191,36,.55); background: rgba(251,191,36,.1); }
    .perc-conclusion.falsified { border-color: rgba(248,113,113,.55); background: rgba(248,113,113,.1); }
    .result-badge.falsified { background: rgba(248,113,113,0.15); color: #f87171; }
"""


def runner_section(proto_id: str, runner_js: str) -> str:
    e = html.escape
    lead = e(runner_lead(proto_id))
    stage = habitat_stage() if proto_id == "p-b-habitat-percolation-ecology-fss" else ""
    heading = "Run the check" if stage else "Run Crosscheck in your browser"
    stage_html = "\n" + stage if stage else ""
    return f"""
  <h2>{heading}</h2>{stage_html}
  <div id=\"crosscheck-runner\" class=\"runner\" data-protocol=\"{e(proto_id)}\">
    <p class=\"runner-lead\">{lead}</p>
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
    title = visitor_title(pid, str(proto.get("title", pid)))
    bridge = proto.get("source_bridge", "")
    bundle = str(proto.get("repro_bundle", "")).strip().rstrip("/")
    bundle_dir: Path = proto["_bundle_dir"]
    script = script_name(bundle_dir)
    catalog_path = proto["_catalog_path"]
    tier = proto.get("feasibility_tier", "desktop")
    runtime = " ".join(str(proto.get("estimated_runtime", "a few minutes")).split()).rstrip(".")
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
    habitat = pid == "p-b-habitat-percolation-ecology-fss"
    formula_html = ""
    conclusion_html = ""
    if habitat:
        pred = (
            "Fill a grid until one habitat wraps all the way around. "
            "That filled percent is the breaking point for that width. "
            "A huge landscape breaks near 59.3%. A smaller one should break somewhere else, "
            "and the gap should shrink in a known way as the width grows."
        )
        formula_html = (
            "  <p class=\"formula\">The check is whether that breaking point follows "
            "p_c(L) = p_c(∞) + c × L^(−1/ν), with ν within 15% of 4/3.</p>\n"
        )
        conclusion_html = """  <div id=\"perc-conclusion\" class=\"perc-conclusion pending\" role=\"status\" aria-live=\"polite\">
    <p class=\"perc-conclusion-title\">The conclusion appears here after the four widths are measured.</p>
    <p class=\"perc-conclusion-body\">This run writes that sentence from the dots on the chart.</p>
  </div>
"""
    runner_html = runner_section(pid, runner_js) if has_browser else ""
    colab_html = colab_section(colab_href) if has_colab and not has_browser else ""
    extra_css = habitat_css() if habitat else ""
    body_tag = '<body class="habitat-demo">' if habitat else "<body>"
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
    .colab-btn:hover {{ filter: brightness(1.05); }}{extra_css}
  </style>
</head>
{body_tag}
  <p class=\"pill\">USDR Crosscheck · {e(tier)}</p>
  <h1>{e(title)}</h1>
  <p class=\"meta\">Protocol <code>{e(pid)}</code> · bridge <code>{e(bridge)}</code></p>
{formula_html}  <p>{e(pred)}</p>
{conclusion_html}{note_section(has_browser, has_colab)}
{runner_html}
{colab_html}
  <h2>Run locally</h2>
  <pre>git clone https://github.com/{REPO}.git
cd Universal-Science-Discovery/{bundle}
pip install -r requirements.txt
python {script}</pre>
  <p>Estimated runtime: {e(str(runtime))}. Exit code is always <code>0</code>; inspect stdout for CONFIRMED vs INCONCLUSIVE.</p>
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
