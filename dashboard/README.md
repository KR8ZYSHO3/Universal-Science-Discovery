# Contributor hub (`dashboard/`)

This folder is part of the **git repository**. Anyone who **clones** USDR gets an HTML **contributor hub** (`index.html`) that:

- Orders **how to contribute** (same flow as [CONTRIBUTING.md](../CONTRIBUTING.md) and [docs/ONBOARDING.md](../docs/ONBOARDING.md))
- Links to **founding and policy** documents (local + GitHub)
- Points to **folders** where work happens (`unknowns-catalog/`, `hypotheses/`, …)
- For **maintainers**, can **live-load** [`.planning/STATE.md`](../.planning/STATE.md) and [`ROADMAP.md`](../ROADMAP.md) when served over HTTP
- **Presentation:** glassmorphism sticky nav with section highlight, **dark theme only** (default; light theme removed), gradient hero, and card hover depth — uses **Google Fonts** (DM Sans, JetBrains Mono) when online; `prefers-reduced-motion` tones down CSS animation, the **particle canvas** (static frame instead of a continuous loop), and decorative spinners where applicable.
- **Catalog search → graph:** Lunr + domain chips in **`dashboard/index.html`**; a short **status line** shows while the graph JSON and optional API metadata load; choosing a result scrolls to **Knowledge graph**, highlights the neighborhood, zooms toward the node (D3), and opens the YAML panel. **GitHub:** panel blob + raw links; each hit row includes **View YAML on GitHub** (repo-scoped filename search). The graph chrome shows **touch-oriented zoom hints** on coarse pointers (`hover: none` + `pointer: coarse`); the loading line exposes **`aria-live="polite"`** while D3 hydrates.
- **Xref hygiene panel:** static **`api/v1/orphan_xref_panel.json`** (regenerate with **`python scripts/export_orphan_xref_panel.py`**) lists capped missing cross-references and disconnected unknowns — contributor tooling, not a scientific ranking.
- **Strategic checklist:** the live snapshot footnote links **`docs/PATH_TO_SUCCESS.md`** (bounded content waves) next to **`ROADMAP.md`**.
- **First contribution checklist:** at **`#start`** (first section in `<main>`), a **How this project works** tool table plus five-step card walks newcomers through clone → pick a task (xref hygiene, Stream A, or good-first issues) → edit YAML → run `python scripts/validate_schemas.py` and `python -m pytest tests/repo_smoke` → open a PR and merge any follow-up graph bot PR. The hub browses and routes; it does not edit catalog files.

## Run it locally

From the **repository root** (parent of `dashboard/`):

```bash
python -m http.server 8765
```

After `python -m http.server 8765` from the repo root, open [`dashboard/index.html`](index.html) in the browser (local URL `http://localhost:8765/dashboard/`), or browse [`index.html`](index.html) from this folder on GitHub.

Double-clicking `index.html` works for **static links**, but the **roadmap/state panels** need the server (browser security).

## GitHub only (no clone)

The [README](../README.md) and [CONTRIBUTING](../CONTRIBUTING.md) point newcomers here. Open **[index.html](index.html)** from a clone (or view raw on GitHub under `dashboard/` once that path exists on the default branch); for a guided read, use [docs/ONBOARDING.md](../docs/ONBOARDING.md).

## Domain landing pages (`domains/`)

Static HTML per discipline under **`dashboard/domains/`** (and **`domains/index.html`**). Counts and bridge lists are **generated** from the YAML catalog — run **`python scripts/generate_domain_pages.py`** from the repo root after adding or reshaping bridges/unknowns so numbers stay honest. Matching logic lives in **`scripts/domain_matching.py`** (bridges use schema **`fields`**, not legacy `source_domain` / `target_domain`). CI checks **`scripts/verify_domain_pages.py`**.

## Maintainer playbook

See **[docs/DEV_DASHBOARD.md](../docs/DEV_DASHBOARD.md)** for the ordered checklist (graph rebuild, `update_dashboard_stats.py --apply`, domain pages, breakthrough grid, consistency verify). Run **`python scripts/verify_dashboard_consistency.py`** before merge when catalog counts or `dashboard/index.html` stats change.

## Publishing & privacy notes

**GitHub Pages:** Pushes to `main` that touch `dashboard/**` or `docs/**` run [`.github/workflows/pages.yml`](../.github/workflows/pages.yml). The workflow patches **`api/v1/meta.json`** with a **`pages_deploy`** block (commit SHA, ref, timestamps) in the Pages artifact and also writes gitignored **`deploy-info.json`** next to `index.html` for backwards compatibility. The hosted hub reads **`pages_deploy`** from **`meta.json`** (fallback: **`deploy-info.json`**) and compares the deploy SHA to **`main`** via the GitHub API so visitors see whether **https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/** is current. **Local `python -m http.server`:** neither field is present until you run a Pages deploy; the hub shows the local-preview banner instead of throwing.

For other hosts, copy `dashboard/` to static hosting as needed. The main **policy docs site** may be built with MkDocs separately; this hub targets **developers exploring the repo**.

When online, `index.html` loads **Google Fonts** and **`marked`** from `unpkg` for typography and markdown rendering. Air‑gapped or privacy‑strict environments can still use the hub: text and layout work with system fonts if those requests fail; panels fall back if `marked` does not load.
