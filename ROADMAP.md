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

### Phase 0: Foundation (2026)

**Goal:** Launch a credible, high-quality seed that proves the concept and attracts the first wave of serious contributors.

**Key Milestones**

- Public launch with 2–3 seeded disciplines (Physics, Biology, Computer Science)
- 500+ high-quality structured entries (knowns, unknowns, hypotheses)
- Core governance, legal, and ethics framework live
- First 50 contributors (including domain experts)
- Basic knowledge graph + search working
- First “Unknowns Hackathon” (virtual)

**Success Metric:**  
The project is recognized as “the most ambitious open science infrastructure project since the Human Genome Project.”

---

**Phase 0 Status (May 2026): SUBSTANTIALLY COMPLETE**

| Milestone | Status |
|---|---|
| Seeded disciplines (Physics, Biology, CS, + 38 more) | 41 domains |
| 500+ high-quality structured entries | 1,957 total (458 bridges + 814 unknowns + 681 hypotheses) — waves 32 & 33 complete |
| Core governance + legal framework | CC BY 4.0 + MIT, CONTRIBUTING.md, CODE_OF_CONDUCT.md |
| Knowledge graph + search | 1042 nodes, Lunr full-text search, D3.js visualization |
| Basic contributor infrastructure | Issue templates, PR template, GitHub Discussions |
| First Unknowns Hackathon | Planned June 2026 (docs/events/hackathon-2026-06.md) |
| First 50 contributors | Pending public launch |

**Transitioning to Phase 1 work: custom domain, submission portal, arXiv preprint.**

---

## Phase 0 Progress (as of 2026-05-07)

### Current counts

| Metric | Phase 0 Target | Current (2026-05-07) | Status |
|--------|---------------|----------------------|--------|
| Cross-domain bridges | 500+ | **470** | 94% — 30 to go |
| Unknowns | 500+ | **817** | ✅ Exceeded |
| Hypotheses | 300+ | **681** | ✅ Exceeded |
| Pioneers | — | **13** | On track |
| Breakthrough gaps | — | **12** | Expanding |
| Knowledge graph nodes | 1,000+ | **1,982** | ✅ Exceeded |
| Knowledge graph edges | — | **2,069** | — |
| Scientific domains | 15+ | **55+** | ✅ Exceeded |
| Orphan unknowns | 0 | **0** | ✅ Clean |
| Schema errors | 0 | **0** | ✅ Clean |

### Milestones achieved this session (overnight build, Waves 17–35)

- **300-bridge milestone** — Wave 20 (2026-05-06)
- **350-bridge milestone** — Wave 24 (2026-05-06)
- **400-bridge milestone** — Wave 29 (2026-05-06)
- **1,000 graph nodes** — Wave 10 (2026-05-06)
- **2,000 graph nodes** — Wave 32+ (2026-05-07)
- **Zero orphan unknowns** — maintained throughout
- **Lyme disease breakthrough-gap cluster** added
- **13 pioneer profiles** complete
- **Dashboard** updated with 400-bridge gold milestone banner

### Phase 0 vs. milestones

| Phase 0 Milestone | Status |
|---|---|
| Seeded disciplines (Physics, Biology, CS, + more) | ✅ 55+ domains |
| 500+ high-quality structured entries | ✅ 1,968 total (470 bridges + 817 unknowns + 681 hypotheses) |
| Core governance + legal framework | ✅ CC BY 4.0 + MIT, CONTRIBUTING.md, CODE_OF_CONDUCT.md |
| Knowledge graph + search | ✅ 1,982 nodes, 2,069 edges; Lunr full-text search; D3.js visualization |
| Basic contributor infrastructure | ✅ Issue templates, PR template, GitHub Discussions |
| First Unknowns Hackathon | Planned June 2026 |
| First 50 contributors | Pending public launch |

### Estimated timeline to Phase 1 readiness

| Task | ETA |
|------|-----|
| 500 bridges reached | ~1–2 build sessions (days) |
| arXiv preprint submitted | 1–2 weeks (PDF conversion + submission) |
| D3 graph working on GitHub Pages | 1–3 days (debug session) |
| Custom domain live | 1 week |
| First public announcement + community launch | ~June 2026 |

**Phase 1 readiness estimated: June–July 2026**, contingent on arXiv submission and first public community push.

---

## Data Source Integration Roadmap

### Active
- **arXiv** (OAI-PMH) — physics, CS, math, biology preprints

### 90-Day Plan (Phase 0 completion)
- **OpenAlex** ✅ harvester built (`scripts/harvesters/harvest_openalex.py`) — cross-domain concept pair scanning
- **PubMed/NCBI** — biomedical literature for medicine/neuroscience bridges
- **Semantic Scholar** — AI-extracted concept tagging at scale
- **CrossRef** — DOI verification and reference list extraction

### Phase 1 Targets
- **NASA ADS** — astronomy/astrophysics
- **INSPIRE-HEP** — high-energy physics
- **Wikidata** — structured concept facts for translation tables

See `docs/DATA_SOURCES.md` for full integration architecture.

---

### Interface development (cross-cutting; see INTERFACE.md)

The **canonical plan for UX, static site, and the future “Discovery OS”** is [INTERFACE.md](INTERFACE.md). That document is **longer-term** than most Phase 0 tasks: we do **not** block governance, legal clarity, or seeded content on a polished UI. Git stays the source of truth; the interface is always a **view** of the repo.


| USDR roadmap (this file) | Interface program ([INTERFACE.md](INTERFACE.md))                                                                                                    |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Phase 0**              | Lock assumptions in INTERFACE.md; when seed content exists, ship a **minimal static site** (docs navigation, contribute links, search placeholder). |
| **Phase 1**              | Execute INTERFACE.md “Phase 1: Trust & Accessibility” in full; prototype early “Phase 2” features only where they accelerate adoption.              |
| **Phase 2+**             | INTERFACE.md “Phase 2–3” — interactive graph, co-pilot grounded in the graph, contributor dashboards — as the knowledge graph and community scale.  |


Track interface milestones in issues/PRs as a **separate workstream** from discipline content.

---

### Phase 1: Momentum (2027–2028)

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

### Phase 2: Acceleration (2029–2031)

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

### Phase 3: Transformation (2032–2035+)

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

### Guiding Principles Across All Phases

- **Discovery First** — Every feature must increase the speed or quality of actual scientific breakthroughs
- **Radical Openness** — Maximum transparency, maximum accessibility, minimum gatekeeping
- **Quality Over Quantity** — We would rather have 10,000 gold-standard entries than 1 million mediocre ones
- **Human + AI Symbiosis** — AI amplifies human discovery; humans remain the final arbiters of truth and ethics
- **Long-term Thinking** — We are building infrastructure for the next 50–100 years, not the next funding cycle

---

### How You Can Help Shape This Future

Right now we are in **Phase 0**. The most valuable thing you can do is:

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
