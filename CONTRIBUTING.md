# Contributing to USDR

## Contributor hub (map of the repo)

After you **clone** this repository, open the **contributor hub**: [`dashboard/index.html`](dashboard/index.html). From the repo root run `python -m http.server 8765`, then visit [http://localhost:8765/dashboard/](http://localhost:8765/dashboard/) (see [`dashboard/README.md`](dashboard/README.md)). It lists the same orientation steps below in order, plus links to **unknowns**, **hypotheses**, and policies — easier than hunting through folders on first visit.

If you only have the GitHub website, follow the steps in this file and [docs/ONBOARDING.md](docs/ONBOARDING.md); after you clone, open [`dashboard/index.html`](dashboard/index.html) locally, or browse the `dashboard/` folder on GitHub (live roadmap panels need a local server — see [`dashboard/README.md`](dashboard/README.md)).

## Orientation

1. **Motivation and impact:** Read [WHY_CONTRIBUTE.md](WHY_CONTRIBUTE.md).
2. **How to talk about the project:** Read [VISION_COMMUNICATION.md](VISION_COMMUNICATION.md) before external outreach so messaging stays accurate and low-friction.
3. **What we are building:** Follow [universal-science-discovery-repo-blueprint.md](universal-science-discovery-repo-blueprint.md) for structure, quality bar, and legal boundaries (e.g. no full copyrighted papers in-repo).
4. **Rules of the road:** [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [GOVERNANCE.md](GOVERNANCE.md), [ETHICS.md](ETHICS.md), [LEGAL.md](LEGAL.md).

## What to contribute first

Per the blueprint, prioritize **unknowns**, **hypotheses**, **cross-domain bridges**, and **reproducible stubs** over bulk text. When in doubt, open a small PR or issue and reference the relevant blueprint section.

## Metadata ingest (tooling)

The **arXiv OAI-PMH metadata** pilot lives under [`packages/ingest`](packages/ingest) (`usdr-ingest`). Read [`packages/ingest/README.md`](packages/ingest/README.md), [docs/DATA_PLAN.md](docs/DATA_PLAN.md), and [docs/UAT_INGEST.md](docs/UAT_INGEST.md) before changing harvest behavior, envelopes, or CI. **No PDFs** — [LEGAL.md](LEGAL.md).

## AI use

If you use AI tools, follow [cursorrules](cursorrules) and human-validate citations, legal posture, and factual claims before merging.

## Questions

Use repository issues once GitHub hosting is set up; until then, coordinate with maintainers per [GOVERNANCE.md](GOVERNANCE.md).
