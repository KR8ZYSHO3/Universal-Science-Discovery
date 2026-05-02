# Spec-driven execution with GSD (Get Shit Done)

This repository’s **policy and content** stay canonical in the docs you already have (`VISION_AND_SCOPE`, `METHODOLOGY`, `ETHICS_REPRODUCIBILITY_AND_DATA`, `AGENTS.md`, Cursor rules).  
**[GSD](https://github.com/gsd-build/get-shit-done)** is an optional **execution layer**: structured phases, multi-agent planning, and verified steps inside Cursor (and other supported clients).

Use it when you want **repeatable, milestone-sized delivery**—for example: first static site from [INTERFACE.md](../INTERFACE.md), schema validation CI, or a seeded discipline tree.

## Install (Cursor)

From a terminal (Node.js required):

```bash
npx get-shit-done-cc@latest --cursor --global
```

For **this repo only**:

```bash
cd /path/to/Universal-Science-Discovery
npx get-shit-done-cc@latest --cursor --local
```

Non-interactive or constrained environments often use `--minimal` (core loop only); see the [upstream README](https://github.com/gsd-build/get-shit-done/blob/main/README.md).

After install, **restart Cursor** so new slash commands and skills load.

## Bootstrap GSD on an existing USDR clone

Suggested order (matches upstream guidance for brownfield repos):

1. **Map the codebase** — run `/gsd-map-codebase` so GSD understands what is already here (schemas, `docs/`, `.github/`, content roots).
2. **Initialize or merge planning** — either `/gsd-new-project` (fresh planning tree) or `/gsd-ingest-docs` with a path to this repo if you are consolidating scattered notes into `.planning/`.

Treat **ROADMAP.md** and **universal-science-discovery-repo-blueprint.md** as inputs to GSD’s roadmap and requirements, not replacements for them: GSD generates **working** artifacts under `.planning/`; those root files stay the **public** north star.

## How GSD maps to USDR (keep both honest)

| USDR source of truth | GSD artifact role |
|----------------------|-------------------|
| [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md), [README.md](../README.md) | Feed **project vision** in `PROJECT.md` / discovery phase; do not narrow scope silently. |
| [METHODOLOGY.md](METHODOLOGY.md), [AGENTS.md](../AGENTS.md) | Every plan and verification step must respect **hypothesis vs finding**, citations discipline, and data classes. |
| [ROADMAP.md](../ROADMAP.md), blueprint | Phase **priorities** and milestone boundaries—noticed by `/gsd-plan-milestone-gaps` style workflows when you use them. |
| [CONTRIBUTING.md](../CONTRIBUTING.md), PR templates | **Ship** GSD-driven code/docs via normal PRs; link issue bullets to `.planning/` commits when useful. |
| [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) | Block any task that implies committing restricted data or full copyrighted papers; use metadata and links only. |

If GSD output conflicts with a governing doc, **the governing doc wins**; fix the plan and continue.

## Multitasking and Cursor

- GSD’s **parallel planners / executors** and **wave** scheduling align well with Cursor’s **multi-agent** sessions: one coherent roadmap, many short-lived sub-contexts.
- Prefer **feature branches** for milestones that touch `.planning/` and product paths together, so review stays one PR narrative upstream can follow.
- For **parallel workstreams** (e.g. “Interface” vs “Content seeding”), use GSD **workstreams** (`/gsd-workstreams`) as documented upstream so state does not collide.

## Git and `.planning/`

- **Default:** Commit `.planning/` with the same care as `docs/`—it is provenance for **why** changes landed.
- If your team decides planning drafts are private, keep them out of git **only** by team agreement; do not ignore `.planning/` in this repo without maintainer approval.

## When not to use GSD

- **Small doc fixes** or single-template edits: normal edit + PR is faster.
- **Purely scientific thread** (debating a hypothesis): use issue templates and [prompts/](prompts/); GSD is for **building and verifying** deliverables.

## Reference

- Upstream repository: [https://github.com/gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done)
- User guide in that repo: `docs/USER-GUIDE.md` (end-to-end walkthrough from `/gsd-new-project` through `/gsd-verify-work`).
