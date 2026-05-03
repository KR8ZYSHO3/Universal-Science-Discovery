# Universal Science Discovery Repository (USDR)

Open-source, Git-based knowledge infrastructure for **discovery-first** science: explicit unknowns, testable hypotheses, cross-domain links, and reproducible workflows.

## New here? (contributors)

1. **Skim this README** (5 min), then **[CONTRIBUTING.md](CONTRIBUTING.md)** — how to participate and what to contribute first.
2. **Contributor hub (recommended after clone):** open **[dashboard/index.html](dashboard/index.html)** locally — contributor path, policies, **where to edit unknowns/hypotheses**, and (with a local server) live **STATE** + **ROADMAP** for maintainers. Run from the repo root: `python -m http.server 8765` → [http://localhost:8765/dashboard/](http://localhost:8765/dashboard/) — details in **[dashboard/README.md](dashboard/README.md)**.
3. **Browsing only on GitHub (no clone):** use **[docs/ONBOARDING.md](docs/ONBOARDING.md)** and the links in CONTRIBUTING; the dashboard’s **GitHub** links next to each doc open the files in the browser.

Everything under **`dashboard/`** is **tracked in git** so anyone who clones the repo gets the same hub; it is not a separate website unless you host it yourself.

## Why this exists

- **Mobilize contributors:** [WHY_CONTRIBUTE.md](WHY_CONTRIBUTE.md)
- **Pitch without unnecessary resistance:** [VISION_COMMUNICATION.md](VISION_COMMUNICATION.md)
- **Full build plan & repo shape:** [universal-science-discovery-repo-blueprint.md](universal-science-discovery-repo-blueprint.md)

## Start here

| Document | Purpose |
|----------|---------|
| [WHY_CONTRIBUTE.md](WHY_CONTRIBUTE.md) | Case for contributing early and at planetary scale |
| [VISION_COMMUNICATION.md](VISION_COMMUNICATION.md) | Elevator pitches and audience-specific framing |
| [universal-science-discovery-repo-blueprint.md](universal-science-discovery-repo-blueprint.md) | Blueprint: vision, structure, MVP, tooling |
| [INTERFACE.md](INTERFACE.md) | User/system interfaces to USDR (full plan; delivery phased per [ROADMAP.md](ROADMAP.md)) |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Technical / system architecture |
| [ROADMAP.md](ROADMAP.md) | Planned phases and priorities |

## Governance, ethics, and legal

| Document | Purpose |
|----------|---------|
| [GOVERNANCE.md](GOVERNANCE.md) | Roles, decisions, maintainer expectations |
| [ETHICS.md](ETHICS.md) | Ethical guardrails for content and collaboration |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community behavior |
| [LEGAL.md](LEGAL.md) | Copyright, licensing posture, DMCA-style policy |
| [DISCLAIMER.md](DISCLAIMER.md) | Limitation of liability, not medical/legal advice |
| [SECURITY.md](SECURITY.md) | Reporting vulnerabilities or leaked secrets |
| [LICENSE](LICENSE) | Default license for this repository |

## Traceability

[DOC_MAP.md](DOC_MAP.md) lists every top-level doc and what it governs.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Content layout (MVP skeleton)

| Path | Role |
|------|------|
| [schemas/](schemas/) | JSON Schemas (YAML): hypothesis, unknown, dataset |
| [templates/](templates/) | PR / issue boilerplate for new records |
| [disciplines/](disciplines/) | Per-field trees; Phase 0 anchors: [physics](disciplines/physics/), [biology](disciplines/biology/), [computer-science](disciplines/computer-science/) |
| [unknowns-catalog/](unknowns-catalog/) | Global research gaps (`u-...`) |
| [hypotheses/](hypotheses/) | Hypothesis registry (`h-...`; `active` / `validated` / `archived`) |
| [cross-domain/](cross-domain/) | Interdisciplinary bridge folders |
| [code/](code/) | Automation and tooling |

Older generic layout (`docs/`, `methods/`, `data/`, …) still applies for governance and prompts.

### Documentation site (preview)

Governance pages under `docs/` can be browsed locally as a static site (see [INTERFACE.md](INTERFACE.md) Phase 1):

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

CI runs `mkdocs build --strict` on every PR and push to `main` (see `.github/workflows/mkdocs-build.yml`).

### arXiv metadata ingest (Phase B starter)

Compliance-oriented **metadata-only** harvest from arXiv OAI-PMH (no PDFs; see [LEGAL.md](LEGAL.md) and [docs/DATA_PLAN.md](docs/DATA_PLAN.md)):

```bash
pip install -r requirements-ingest.txt
pip install -e ./packages/ingest
usdr-ingest harvest --output records.jsonl --max-records 10 --manifest manifest.json
```

Add `--dry-run` to summarize requests without writing files. Tests use recorded XML fixtures (no live HTTP in default CI — see `.github/workflows/ingest-ci.yml`).

### Published documentation (GitHub Pages)

**Live URL:** [https://kr8zysho3.github.io/Universal-Science-Discovery/](https://kr8zysho3.github.io/Universal-Science-Discovery/)

After the first successful run of [`.github/workflows/mkdocs-gh-pages.yml`](.github/workflows/mkdocs-gh-pages.yml) on `main`, configure **Settings → Pages → Build and deployment → Deploy from a branch**: branch **`gh-pages`**, folder **`/` (root)**. Later pushes to `main` rebuild and update that branch via [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages).

## AI-assisted work in this repo

Project-specific Cursor guidance is in [cursorrules](cursorrules) (import or symlink into `.cursor/rules/` per your editor setup).
