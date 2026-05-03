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

Open: [http://localhost:8765/dashboard/](http://localhost:8765/dashboard/)

Double-clicking `index.html` works for **static links**, but the **roadmap/state panels** need the server (browser security).

## GitHub only (no clone)

The [README](../README.md) and [CONTRIBUTING](../CONTRIBUTING.md) point newcomers here. Open **[index.html](index.html)** from a clone (or view raw on GitHub under `dashboard/` once that path exists on the default branch); for a guided read, use [docs/ONBOARDING.md](../docs/ONBOARDING.md).

## Publishing & privacy notes

This is **not** automatically the public project website unless you add hosting (e.g. copy `dashboard/` to static hosting or wire GitHub Pages). The main **policy docs site** may be built with MkDocs separately; this hub is for **developers who have the repo**.

When online, `index.html` loads **Google Fonts** and **`marked`** from `unpkg` for typography and markdown rendering. Air‑gapped or privacy‑strict environments can still use the hub: text and layout work with system fonts if those requests fail; panels fall back if `marked` does not load.
