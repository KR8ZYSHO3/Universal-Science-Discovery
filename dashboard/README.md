# Contributor hub (`dashboard/`)

This folder is part of the **git repository**. Anyone who **clones** USDR gets an HTML **contributor hub** (`index.html`) that:

- Orders **how to contribute** (same flow as [CONTRIBUTING.md](../CONTRIBUTING.md) and [docs/ONBOARDING.md](../docs/ONBOARDING.md))
- Links to **founding and policy** documents (local + GitHub)
- Points to **folders** where work happens (`unknowns-catalog/`, `hypotheses/`, …)
- For **maintainers**, can **live-load** [`.planning/STATE.md`](../.planning/STATE.md) and [`ROADMAP.md`](../ROADMAP.md) when served over HTTP
- **Presentation:** glassmorphism sticky nav with section highlight, **light/dark theme** (saved in `localStorage`), gradient hero, and card hover depth — uses **Google Fonts** (DM Sans, JetBrains Mono) when online; `prefers-reduced-motion` tones down animation

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

## Publishing & privacy notes

**GitHub Pages:** Pushes to `main` that touch `dashboard/**` or `docs/**` run [`.github/workflows/pages.yml`](../.github/workflows/pages.yml). The workflow writes **`deploy-info.json`** (gitignored locally) next to `index.html` with the deployed commit SHA and timestamp. The hub reads that file and compares it to **`main`** via the GitHub API so visitors see whether **https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/** is current.

For other hosts, copy `dashboard/` to static hosting as needed. The main **policy docs site** may be built with MkDocs separately; this hub targets **developers exploring the repo**.

When online, `index.html` loads **Google Fonts** and **`marked`** from `unpkg` for typography and markdown rendering. Air‑gapped or privacy‑strict environments can still use the hub: text and layout work with system fonts if those requests fail; panels fall back if `marked` does not load.
