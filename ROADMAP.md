# USDR Roadmap

## The Open-Source Engine That Will Redefine Scientific Discovery

**"We are building the operating system for humanity’s next century of discovery."**

---

### The Vision (North Star)

By 2035, the **Universal Science Discovery Repository (USDR)** will be the single most important piece of scientific infrastructure on Earth — a living, version-controlled, globally governed knowledge engine that:

- Surfaces the most important unknowns in science in real time
- Turns every researcher, citizen scientist, and AI into a co-discoverer
- Makes groundbreaking breakthroughs dramatically faster, more collaborative, and more reproducible
- Becomes the trusted source where the world’s greatest minds come to find what’s *not yet known* — and work together to solve it

This is not another database.  
This is not another wiki.  
This is the **global brain of science** — open, versioned, and built for discovery.

---

### Phase 0: Foundation (2026) — **COMPLETE**

**Goal:** Ship a credible, schema-backed seed — governance, tooling, automation, and enough structured content — so the project can scale without rewriting fundamentals.

**Foundation deliverables (closed)**

- Core governance, legal, and ethics framework (dual license, CONTRIBUTING, Code of Conduct)
- Hypothesis / unknown / bridge schemas + CI validation on every PR
- MkDocs site + contributor hub (`dashboard/`) + static JSON API
- Seeded disciplines far beyond the original three (55+ domains)
- 500+ high-quality structured entries — **exceeded** (bridges + unknowns + hypotheses at scale)
- Knowledge graph build + Lunr search + interactive dashboard graph
- arXiv OAI-PMH ingest package (Phase B) and OpenAlex automation pipeline
- GitHub Pages deployment live

**Success metric (foundation):** The repo behaves like serious infrastructure — reproducible builds, honest labeling of speculation, and a catalog that compounds.

Calendar-dependent outcomes (first waves of contributors, citations, hackathon attendance, coordinated public launch) are tracked under **Phase 1 — Discovery & adoption** so they do not block declaring foundation work complete.

---

**Foundation closure checklist (May 2026)**

| Milestone | Status |
|---|---|
| Seeded disciplines (Physics, Biology, CS, + more) | ✅ 55+ domains |
| 500+ high-quality structured entries | ✅ Exceeded |
| Core governance + legal framework | ✅ CC BY 4.0 + MIT, CONTRIBUTING.md, CODE_OF_CONDUCT.md |
| Knowledge graph + search | ✅ Built graph + Lunr + D3 visualization |
| Basic contributor infrastructure | ✅ Issue templates, PR template, GitHub Discussions |
| OpenAlex automation pipeline | ✅ Weekly cron job live |
| Pioneer lineage system | ✅ Growing |
| Breakthrough gaps catalog | ✅ Live |

**Ongoing engineering (not gated on Phase 1):** bridge promotion toward 1,000+, dashboard reliability, harvesters, and tooling — see `docs/PATH_TO_SUCCESS.md`.

---

### Phase 1: Discovery & adoption (2026–2027) — **ACTIVE**

**Goal:** Earn discoverability and trust on human timelines — preprint, outreach, first external contributors, and community rituals — while engineering continues in parallel.

**Key milestones**

- arXiv preprint submitted with a citable DOI (`docs/preprint/usdr_preprint.md`)
- Coordinated public launch (announcement + researcher-facing outreach)
- Custom domain and stable public URLs for credibility (overlaps `INTERFACE.md` P1.1)
- Stream A first-contributor happy path validated (`docs/HAPPY_PATH_FIRST_RECORDS.md`)
- First 50 contributors (including domain experts)
- First “Unknowns Hackathon” (virtual; see `docs/events/` when scheduled)
- First external citation or equivalent academic signal

**Success metric:** USDR is findable as infrastructure — not only as a repository insiders already track.

---

### Integrated development priorities (2026 reevaluation)

Recent work surfaced cross-cutting needs (dashboard truthfulness, CI visibility, domain browse pages, breakthrough gaps UX). **These run in parallel with Phase 1** — they are not waiting on mass adoption, and adoption is not waiting on perfect tooling.

| Track | What | Primary artifacts / scripts |
|-------|------|-----------------------------|
| **A — Discovery & adoption** | Human-calendar milestones | Preprint, outreach, contributors, hackathon — `docs/PATH_TO_SUCCESS.md` |
| **B — Trust surfaces** | Anything a newcomer sees must match git | `dashboard/index.html` + `update_dashboard_stats.py`; `dashboard/domains/` + `generate_domain_pages.py` + `verify_domain_pages.py`; CI panel in hub; `mkdocs build --strict` after doc edits |
| **C — Breakthrough gaps** | World-scale problems ↔ blocking bridges | `breakthrough-gaps/*.yaml`, hub grid via `render_breakthrough_gaps_hub.py`, API `api/v1/breakthrough_gaps.json`, steward guide `docs/BREAKTHROUGH_GAPS.md` |
| **D — Catalog depth** | Waves, stubs, harvesters | `cross-domain/`, `drafts/`, OpenAlex cadence, graph rebuild |

**Rule of thumb:** merge-worthy batches that touch **content visible on the hub** should ship **regenerated dashboard fragments + docs** in the same PR or an immediate follow-up (see `.cursor/rules/documentation-and-dashboard.mdc`).

### Audit backlog (2026-05)

Structured findings and evidence: **[May 2026 full audit report](.planning/reports/USDR_FULL_AUDIT_2026-05.md)**.

- Refresh **ROADMAP** foundation snapshot numbers whenever README/graph meta step forward (avoid frozen “868 bridge” era leaking into narrative).
- Keep **`.planning/STATE.md` catalog table** aligned with README after each merge-worthy wave (bridges / unknowns / hypotheses / breakthrough gaps).
- Soften or qualify **README** “every entry DOI-linked” language against actual schema minimums per record type. *(Done 2026-05-10 — README wording.)*
- Document **dual validation workflows** (`validate.yml` path-filtered vs `validate-schemas.yml`) for contributors and branch-protection expectations. *(Done 2026-05-10 — `docs/OPERATING_RHYTHM.md`.)*
- Add **incremental pytest smoke tests** for critical `scripts/` entry points. *(Done 2026-05-10 — `tests/repo_smoke` includes validate, domain pages, dashboard consistency, and **`build_graph.py --report-orphans`** (informational only; strict fail-on-orphan xref mode not enabled).)*
- Drive **Discovery Engines** metrics from data or drop static unknown counts in `dashboard/index.html` to prevent silent drift. *(Partially done 2026-05-10 — removed misleading static unknown counts; bridge spotlight counts remain curated lists.)*
- Continue **GitHub Pages graph reliability** work with captured console/network traces per incident.

---

## Foundation achievement snapshot (as of 2026-05-10)

### Current counts

| Metric | Foundation target | Current (2026-05-10) | Status |
|--------|---------------|----------------------|--------|
| Cross-domain bridges | 500+ | **1,123** | ✅ Exceeded (next: ongoing catalog growth) |
| Unknowns | 500+ | **1,408** | ✅ Exceeded |
| Hypotheses | 300+ | **1,274** | ✅ Exceeded |
| Pioneers | — | **18** | ✅ Growing |
| Breakthrough gaps | — | **24** | Living catalog (`breakthrough-gaps/`) |
| Knowledge graph nodes | 1,000+ | **3,857** | ✅ Exceeded |
| Knowledge graph edges | — | **4,517** | — |
| Scientific domains | 15+ | **55+** | ✅ Exceeded |
| Orphan unknowns | 0 | **0** | ✅ Clean |
| Schema errors | 0 | **0** | ✅ Clean |

### Milestones achieved (Waves 1–67 + OA-1)

- [x] **100-bridge milestone** — Wave 7 (2026-05-05)
- [x] **250-bridge milestone** — Wave 17 (2026-05-06)
- [x] **300-bridge milestone** — Wave 20 (2026-05-06)
- [x] **350-bridge milestone** — Wave 24 (2026-05-06)
- [x] **400-bridge milestone** — Wave 29 (2026-05-06)
- [x] **500-bridge milestone** — Wave 36 (2026-05-07)
- [x] **600-bridge milestone** — Wave 45 (2026-05-07)
- [x] **700-bridge milestone** — Wave 54 (2026-05-07)
- [x] **800-bridge milestone** — Wave 62 (2026-05-07)
- [x] **1,000 graph nodes** — Wave 10 (2026-05-06)
- [x] **3,000 graph nodes** — Wave 65 (2026-05-07)
- [x] **1,000 hypotheses** — Wave 66/67 (2026-05-07)
- [x] **OpenAlex automation pipeline** — weekly cron job live (2026-05-07)
- [x] **Pioneer lineage system** — 18 pioneers (2026-05-07)
- [x] **Breakthrough gaps catalog** — expanded set in `breakthrough-gaps/` (hub + API stay synced via `render_breakthrough_gaps_hub.py`)
- [x] **Zero orphan unknowns** — maintained throughout all waves
- [x] **1,000+ bridges** — crossed (see README / graph meta for live total)
- [ ] arXiv preprint submission (Phase 1 — author: Brandon Shoemaker)
- [ ] First external citation / contributor (Phase 1)

### Foundation vs. original gate checklist

| Foundation gate | Status |
|---|---|
| Seeded disciplines (Physics, Biology, CS, + more) | ✅ 55+ domains |
| 500+ high-quality structured entries | ✅ 4,805+ total (1,123 bridges + 1,408 unknowns + 1,274 hypotheses + 10 phenomenology — see README; headline counts match `verify_dashboard_consistency.py` + graph meta) |
| Core governance + legal framework | ✅ CC BY 4.0 + MIT, CONTRIBUTING.md, CODE_OF_CONDUCT.md |
| Knowledge graph + search | ✅ 3,857 nodes, 4,517 edges; Lunr full-text search; D3.js visualization |
| Basic contributor infrastructure | ✅ Issue templates, PR template, GitHub Discussions |

### Phase 1 (Discovery) — still open

| Milestone | Status |
|---|---|
| First Unknowns Hackathon | Planned (see `docs/events/` when scheduled) |
| First 50 contributors | Pending broader discoverability |

### Phase 2 (Momentum) prerequisites

Momentum starts once Discovery & adoption has produced a **citable anchor** (typically arXiv DOI) and repeatable contributor intake. Tracking tasks:

| Task | Status | ETA |
|------|--------|-----|
| 1,000 bridges | ✅ Exceeded — continued depth in catalog + `drafts/bridges/` | Ongoing engineering |
| arXiv preprint submitted | Ready to convert + submit | 1–2 weeks |
| D3 graph working on GitHub Pages | Reliability ongoing | Rolling |
| Custom domain live | Not started | ~1 week |
| First public announcement + community launch | Pending arXiv DOI | ~June 2026 |

**Phase 2 (Momentum) readiness estimated: June–July 2026**, contingent on arXiv submission and first external contributors — **not** on pausing catalog or tooling work.

---

## Data Source Integration Roadmap

### Active
- **arXiv** (OAI-PMH) — physics, CS, math, biology preprints

### Foundation-era integration plan (complete / sustaining)
- **OpenAlex** ✅ harvester built (`scripts/harvesters/harvest_openalex.py`) — cross-domain concept pair scanning
- **PubMed/NCBI** — biomedical literature for medicine/neuroscience bridges
- **Semantic Scholar** — AI-extracted concept tagging at scale
- **CrossRef** — DOI verification and reference list extraction

### Phase 2 Targets
- **NASA ADS** — astronomy/astrophysics
- **INSPIRE-HEP** — high-energy physics
- **Wikidata** — structured concept facts for translation tables

See `docs/DATA_SOURCES.md` for full integration architecture.

---

### Interface development (cross-cutting; see INTERFACE.md)

The **canonical plan for UX, static site, and the future “Discovery OS”** is [INTERFACE.md](INTERFACE.md). INTERFACE.md uses its **own** Phase 1/2/3 labels for the interface program; map them to **this** roadmap’s phases using the table below. Git stays the source of truth; the interface is always a **view** of the repo.


| USDR roadmap (this file) | Interface program ([INTERFACE.md](INTERFACE.md))                                                                                                    |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Phase 0 — Foundation** | Static dashboard, domain pages, API, knowledge graph — **COMPLETE** (see INTERFACE.md “Current State”).                                           |
| **Phase 1 — Discovery & adoption** | Credibility + outreach work (preprint, launch, custom domain when ready); optional early INTERFACE tasks where they reduce friction.                |
| **Phase 2 — Momentum** | Execute INTERFACE.md **“Phase 1: Trust & Accessibility”** in full; prototype early INTERFACE “Phase 2” features only where they accelerate adoption. |
| **Phase 3+ (Acceleration / Transformation)** | INTERFACE.md **Phase 2–3** — interactive discovery UX, co-pilot grounded in the graph, contributor dashboards — as the catalog and community scale. |


Track interface milestones in issues/PRs as a **separate workstream** from discipline content.

---

### Phase 2: Momentum (2027–2028)

**Goal:** Become the default place where serious researchers go to find open problems and collaborate on breakthroughs.

**Key Milestones**

- 10,000+ structured entries across 15+ disciplines
- First major institutional partners (universities, research institutes, arXiv, OpenAlex)
- AI co-pilot (open weights) trained on the repo that can propose novel hypotheses
- 500+ active contributors
- First peer-reviewed papers that cite USDR as the source of the core hypothesis
- Cross-domain “Discovery Engines” (e.g. Quantum-Biology, Climate-AI, Consciousness)

**Success Metric:**  
At least 10 high-impact scientific papers or patents trace their origin to hypotheses first surfaced in USDR.

---

### Phase 3: Acceleration (2029–2031)

**Goal:** Turn USDR into a self-sustaining discovery machine that actively accelerates the pace of science.

**Key Milestones**

- 100,000+ entries + full knowledge graph with semantic search
- Federated model (other repos can plug into USDR)
- Autonomous “Discovery Agents” that continuously scan literature and propose new connections
- Global network of physical “Discovery Labs” that run experiments based on USDR hypotheses
- First Nobel-level or equivalent breakthrough directly attributed to USDR collaboration
- Sustainable funding model (grants + sponsorship + institutional membership)

**Success Metric:**  
USDR is widely regarded as one of the top 5 most important scientific infrastructure projects in the world.

---

### Phase 4: Transformation (2032–2035+)

**Goal:** Become the foundational layer of 21st-century science — the “Linux of Discovery.”

**Visionary Milestones**

- USDR becomes the default interface through which most researchers interact with the global scientific literature and open problems
- Integration with major AI labs (models are trained with explicit “discovery grounding” from USDR)
- Decentralized governance + on-chain contribution reputation (optional future evolution)
- “Discovery OS” — a full suite of tools (agents, simulators, experiment planners) built on top of USDR
- Every major research institution has a USDR mirror + local working group
- Humanity’s collective scientific unknowns are tracked, prioritized, and attacked in a coordinated, open way for the first time in history

**Ultimate Success Metric:**  
The rate of major scientific breakthroughs increases measurably because of USDR.  
Future historians write:  

> “The creation of the Universal Science Discovery Repository marked the beginning of the Acceleration Age of Science.”

---

### Guiding principles across all phases

- **Discovery First** — Every feature must increase the speed or quality of actual scientific breakthroughs
- **Radical Openness** — Maximum transparency, maximum accessibility, minimum gatekeeping
- **Quality Over Quantity** — We would rather have 10,000 gold-standard entries than 1 million mediocre ones
- **Human + AI Symbiosis** — AI amplifies human discovery; humans remain the final arbiters of truth and ethics
- **Long-term Thinking** — We are building infrastructure for the next 50–100 years, not the next funding cycle

---

### How You Can Help Shape This Future

Foundation (**Phase 0**) is **complete**. The active roadmap track for visibility is **Phase 1 — Discovery & adoption**; catalog and tooling work continues in parallel. The most valuable things you can do now are:

1. Contribute high-quality unknowns and hypotheses in your field
2. Help build the core tooling and knowledge graph
3. Spread the vision to colleagues and institutions
4. Join the governance working groups

**This is not a side project.**  
This is one of the most important open-source initiatives humanity can build right now.

The question is no longer *whether* science needs this.  
The question is: **Who will build it?**

We are building it — openly, together.

**Join us.**  
The future of discovery is open source.
