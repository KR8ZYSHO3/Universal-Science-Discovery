# USDR Workstreams — how development is organised

**This is where you pick up work.** Each workstream is an independent area of the project. Find one that matches your skills, claim an open issue, and start. You do not need to contribute everywhere — owning one area well is more valuable than spreading thin.

## How to claim a workstream task

1. **Browse open issues** filtered by area label (links below).
2. **Comment on the issue**: "I'd like to work on this." A maintainer will assign it to you.
3. **Branch** from `main`: `git checkout -b feat/<area>/<short-slug>` or `fix/<area>/<short-slug>`.
4. **Open a draft PR** early — this signals to others what you are working on and prevents duplicate effort.
5. **Mark ready for review** when done. At least one maintainer review is required before merge.
6. **One person per issue** at a time. If an issue has had no activity for 14 days, it is considered unowned and can be claimed.

No issue for what you want to do? **Open one first**, describe the change, and wait for a thumbs-up from a maintainer before investing significant time. This avoids wasted effort.

---

## The workstreams

### WS-1 · Physics content
**Label:** `area:physics`
**What:** Add, review, and improve entries in `disciplines/physics/`, `unknowns-catalog/`, and `hypotheses/active/` that relate to physics.
**Starter tasks:** seed a new `u-…` unknown using the template; link an existing unknown to a `h-…` hypothesis.
**Key files:** `disciplines/physics/README.md`, `schemas/unknown.yaml`, `schemas/hypothesis.yaml`, `templates/`
**Browse issues:** https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3Aarea%3Aphysics
**Required reading:** `docs/METHODOLOGY.md`, `docs/VISION_AND_SCOPE.md`, `LEGAL.md`

---

### WS-2 · Biology content
**Label:** `area:biology`
**What:** Seed and review entries covering biology, medicine, and related life sciences.
**Starter tasks:** seed a new unknown in aging, oncology, or ecology; add a cross-link to an existing physics unknown.
**Key files:** `disciplines/biology/README.md`, `unknowns-catalog/`, `hypotheses/active/`
**Browse issues:** https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3Aarea%3Abiology
**Required reading:** `docs/METHODOLOGY.md`, `ETHICS.md`, `LEGAL.md`

---

### WS-3 · Computer Science content
**Label:** `area:computer-science`
**What:** Seed CS unknowns (algorithmic, AI/ML, formal methods) and propose cross-domain links to physics and biology.
**Starter tasks:** add the first `u-…` CS unknown; add a `h-…` hypothesis about discovery algorithms or graph traversal.
**Key files:** `disciplines/computer-science/README.md`, `cross-domain/`
**Browse issues:** https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3Aarea%3Acomputer-science

---

### WS-4 · New disciplines
**Label:** `area:new-discipline`
**What:** Propose and scaffold a new discipline not yet in the repo (Chemistry, Climate Science, Neuroscience, Mathematics, etc.).
**How to propose:** open an issue with the discipline name, 2–3 seed unknowns to validate it, and a draft `README.md`.
**Required:** maintainer approval before scaffolding. Quality bar: a new discipline needs at least 3 seed entries to be accepted.
**Browse issues:** https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3Aarea%3Anew-discipline

---

### WS-5 · Ingest pipeline
**Label:** `area:ingest`
**What:** The `packages/ingest` Python package that harvests metadata from arXiv (OAI-PMH) and future sources. Extend harvesters, add new sources, improve the envelope schema, write tests.
**Skill needed:** Python, HTTP/REST APIs, XML parsing, pytest.
**Key files:** `packages/ingest/src/usdr_ingest/`, `packages/ingest/tests/`, `schemas/ingestion-envelope-1.0.0.json`, `docs/DATA_PLAN.md`, `docs/UAT_INGEST.md`
**Browse issues:** https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3Aarea%3Aingest
**Constraint:** no full-text papers — metadata only. See `LEGAL.md`.

---

### WS-6 · Schema & validation
**Label:** `area:schema`
**What:** The YAML schemas (`schemas/`) and `scripts/validate_schemas.py`. Improve existing schemas, add new ones (e.g. a `method.yaml`, `dataset.yaml` extension), tighten CI validation.
**Skill needed:** YAML, JSON Schema, Python.
**Key files:** `schemas/`, `scripts/validate_schemas.py`, `.github/workflows/validate-schemas.yml`
**Browse issues:** https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3Aarea%3Aschema

---

### WS-7 · Knowledge graph
**Label:** `area:knowledge-graph`
**What:** The Phase 1+ knowledge graph layer — scripts to build a graph from existing YAML entries, query it, and export it (RDF/JSON-LD/Neo4j). This is exploratory; coordinate with maintainers before starting.
**Skill needed:** Python, graph databases or RDF, NetworkX or similar.
**Key files:** `cross-domain/`, `hypotheses/`, `unknowns-catalog/` (these are the nodes), `ARCHITECTURE.md`
**Browse issues:** https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3Aarea%3Aknowledge-graph
**Note:** Core catalog → graph export is **foundation-complete**. Heavy federation / new graph backends align with **Phase 2 — Momentum (2027+)**; coordinate with maintainers before large scopes.

---

### WS-8 · Dashboard & docs site
**Label:** `area:dashboard`
**What:** The `dashboard/index.html` contributor hub and the MkDocs documentation site (`mkdocs.yml`, `docs/`). Improve UX, fix broken links, add new sections, maintain accuracy.
**Skill needed:** HTML/CSS/JS (vanilla), Markdown, MkDocs Material.
**Key files:** `dashboard/`, `docs/`, `mkdocs.yml`, `.github/workflows/mkdocs-build.yml`
**Browse issues:** https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3Aarea%3Adashboard
**Rule:** the hub must always accurately reflect the repo. Ship hub changes in the same PR as the docs change that motivated them.

---

### WS-9 · Infrastructure & CI
**Label:** `area:infrastructure`
**What:** GitHub Actions workflows, branch protection, dependabot, link checking, and the repo's CI health.
**Skill needed:** GitHub Actions YAML, bash/PowerShell, CI debugging.
**Key files:** `.github/workflows/`, `.github/dependabot.yml`, `.markdown-link-check.json`
**Browse issues:** https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3Aarea%3Ainfrastructure

---

### WS-10 · Documentation & governance
**Label:** `area:docs`
**What:** Improve policy documents, onboarding guides, methodology, and governance. Translate docs. Fix inconsistencies across the doc set.
**Skill needed:** Technical writing, Markdown, understanding of open science norms.
**Key files:** `docs/`, `AGENTS.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `ROADMAP.md`
**Browse issues:** https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3Aarea%3Adocs

---

## Issue labels quick reference

| Label | Meaning |
|---|---|
| `area:physics` / `area:biology` / … | Which workstream |
| `type:content` | Adding or editing scientific entries (unknowns, hypotheses) |
| `type:tooling` | Code, scripts, or CI |
| `type:docs` | Documentation only |
| `type:bug` | Something broken |
| `difficulty:starter` | Good for a first contribution; < 2h estimated |
| `difficulty:intermediate` | Requires understanding the codebase; 2–8h |
| `difficulty:advanced` | Design decisions involved; coordinate first |
| `status:needs-owner` | Open and unclaimed — pick it up |
| `status:in-progress` | Assigned; contact the assignee if you want to help |
| `status:blocked` | Waiting on external decision or dependency |

**First-time contributors:** filter by `difficulty:starter` + `status:needs-owner`. These are scoped tasks specifically chosen to be completable in a single PR without deep context.

---

## Collaboration rules (short version)

1. **One issue → one branch → one PR.** Keep PRs small. A reviewer should be able to fully understand the change in 15 minutes.
2. **Comment before you start.** If there is no issue, open one. If there is an issue, comment that you are starting. This prevents two people doing the same work.
3. **Draft PRs are free.** Open a draft PR as soon as you have any code to show — it makes your intent visible and lets maintainers give early feedback.
4. **`main` is always stable.** Never push directly to `main`. Branch protection enforces this — your push will be rejected.
5. **Failing CI = do not merge.** Fix the CI before requesting review. The workflows that must pass: `validate-schemas`, `markdown-link-check`, `mkdocs-build`, and `ingest tests` (if you changed `packages/ingest/`).
6. **Scientific claims need evidence.** New unknowns and hypotheses must follow `docs/METHODOLOGY.md`. If you are not sure whether a claim meets the bar, open a discussion issue before writing the YAML.

---

## Licensing note for contributors

Your contributions to **code and scripts** are covered by the **MIT License** — anyone who redistributes must include the copyright notice and license text. Attribution is legally required.

Your contributions to **content** (YAML entries, Markdown notes, structured data) are currently under **CC0 1.0** (public domain). This means anyone can reuse the content *without attribution*. If you want your scientific contributions to require credit, note this preference in your PR and a maintainer will discuss options. The project is evaluating whether to move content to **CC-BY 4.0** (attribution required) in a future governance decision.

**Bottom line:** nobody can claim they wrote code you wrote (MIT requires your name to stay in the license). But under CC0, a third party could reproduce the catalog without crediting USDR — we are aware of this trade-off.

---

## Setting up your environment

```bash
# Clone
git clone https://github.com/KR8ZYSHO3/Universal-Science-Discovery.git
cd Universal-Science-Discovery

# Python environment (for validation and ingest)
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux
pip install -r scripts/requirements-validate.txt
pip install -e packages/ingest

# Run all local checks before every push
python scripts/validate_schemas.py
python -m pytest packages/ingest/tests
python -m mkdocs build --strict

# Open the contributor hub (dashboard/index.html — local URL in dashboard/README.md)
python -m http.server 8765
```

See `docs/OPERATING_RHYTHM.md` for the full daily workflow and CI gate details.
