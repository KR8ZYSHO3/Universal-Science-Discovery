# Quality bar — keeping USDR from going sloppy

USDR fails when structure looks serious but **records, evidence, and review** drift into hand-waving. This page names the failure modes and the **mitigations** already wired (or to tighten) in the repo.

## What “sloppy” looks like here

| Failure mode | Why it hurts |
|--------------|--------------|
| **YAML shape without substance** | `u-` / `h-` files that validate but say nothing falsifiable or well-scoped. |
| **Citation theater** | Lists of links without *why* they matter, or unverified AI-suggested DOIs/URLs. |
| **Bypassing checks** | Merging when `validate_schemas` / agreed CI is red, or “we’ll fix in follow-up” forever. |
| **Scope churn** | Rewriting schemas, paths, or happy path weekly so contributors never learn a stable loop. |
| **Drive-by docs** | README / hub / Stream A doc wrong versus what CI and schemas actually enforce. |
| **No reviewer lane** | Everything becomes “LGTM” aesthetic edits; nobody owns science integrity on content PRs. |

## Mitigations (use together)

### 1) Automated gates (objective)

- **Schema validation:** `python scripts/validate_schemas.py` on `unknowns-catalog/**` and `hypotheses/**` — failures are non-negotiable before merge.
- **CI on `main` PRs:** markdown links, MkDocs strict build, schemas — keep required checks meaningful (see [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md)).
- **Ingest / tooling:** separate path-filtered jobs — don’t block content PRs with optional infra checks, but don’t skip **`python -m pytest packages/ingest/tests`** when ingest changes.

### 2) Human gates (subjective but structured)

- **Two-lane review (default posture):**  
  - **Lane A — Shape:** IDs, schema, LEGAL-safe links, file placement (fast, strict).  
  - **Lane B — Science:** wording, falsifiability, evidence adequacy per [METHODOLOGY.md](METHODOLOGY.md) (slower).  
  Both can be one person on a tiny team, but **call out which lane** in review comments.
- **PR template:** checklist is useless unless reviewers **verify** it; treat unchecked methodology/ethics boxes as **needs discussion**, not silent approval.
- **Small PRs:** prefer one unknown **or** one hypothesis **or** one doc fix — not all three unless tightly coupled.

### 3) Stable “happy path”

- **[HAPPY_PATH_FIRST_RECORDS.md](HAPPY_PATH_FIRST_RECORDS.md)** is the **single** narrative for first records. Parallel work (Stream B, C, …) should not fork competing instructions; update the happy path when schemas or seed examples change.

### 4) Gold-standard exemplars (Stream B mental model)

- Treat [unknowns-catalog/high-priority/u-dark-matter-microphysics.yaml](../unknowns-catalog/high-priority/u-dark-matter-microphysics.yaml) and linked hypotheses as **style references** — not perfect science, but **honest structure** to imitate.
- When a new record is *better* than seeds, consider adding a maintainer note or follow-up PR to align examples (avoid silent drift).

### 5) Doc / hub discipline

- Milestones or hub-affecting edits: follow `.cursor/rules/documentation-and-dashboard.mdc` — **CHANGELOG**, **STATE**, **dashboard** check at **`http://localhost:8765/dashboard/`** when links are touched.
- **DOC_MAP.md** / **REPOSITORY_MANIFEST.md** track “this file governs X”; if behavior changes, update traceability in the **same PR**.

### 6) Cadence and triage

- [OPERATING_RHYTHM.md](OPERATING_RHYTHM.md): weekly triage, monthly doc reality-check — prevents slow rot.
- Labels and milestones: [LABELS_AND_MILESTONES.md](LABELS_AND_MILESTONES.md) so “needs-evidence” and “blocked” mean something.

## Definition of “done” for a content PR

Minimum before merge:

1. `python scripts/validate_schemas.py` exits **0** (or CI green equivalent).
2. Links in the YAML comply with [LEGAL.md](../LEGAL.md) (metadata / open access posture — no hosted paywalled full text).
3. At least one review comment addresses **Lane B** if the PR makes or tightens scientific claims.
4. If the PR changes contributor instructions or schemas, **Stream A** / templates / hub updated in the **same** merge bundle.

## Where to go deeper

- [METHODOLOGY.md](METHODOLOGY.md) — evidence bar, claims discipline.  
- [COLLABORATION_AND_REVIEWS.md](COLLABORATION_AND_REVIEWS.md) — review expectations.  
- [ETHICS_REPRODUCIBILITY_AND_DATA.md](ETHICS_REPRODUCIBILITY_AND_DATA.md) — data classes and integrity.  
- [CONTRIBUTING.md](../CONTRIBUTING.md) — mechanics + AI use.

**Bottom line:** sloppiness is managed by **objective CI + explicit review lanes + small PRs + stable happy path + living traceability docs** — not by more ambition in `ROADMAP.md` alone.
