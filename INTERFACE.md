# USDR Interface Program

## Purpose

This document is the canonical plan for UX, static site, and the future "Discovery OS" interface.
The interface is always a **view** of the repository — git remains the source of truth.

Interface development runs as a **separate workstream** from discipline content; we do not block
content growth on UI polish, and we do not sacrifice content quality for UI features.

---

## Current State (May 2026)

### What's Live (Phase 0 — Static Site)
- **Dashboard**: `dashboard/index.html` — dark-themed, responsive
  - Live stats (bridges, unknowns, hypotheses, graph nodes)
  - D3.js interactive force-directed knowledge graph (1000+ nodes, zoom/pan, click-to-detail)
  - Lunr.js full-text search across all bridges and unknowns
  - Pioneers section (13 cards with core contributions)
  - Breakthrough Gaps section (11 entries with TRL ratings)
  - AI Co-pilot section with live bridge proposal counts
  - 1000-node milestone banner
- **Domain landing pages**: `dashboard/domains/` — 41 auto-generated pages, one per discipline
- **Explainer pages**: `dashboard/explainers/` — long-form scientific explainers for key bridges
- **Static JSON API**: `api/v1/` — bridges, unknowns, hypotheses, graph, meta, proposals endpoints
- **Knowledge graph**: `docs/knowledge_graph.json` — 1042 nodes, 964 edges (578KB)
- **GitHub Pages deployment**: `https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/`

---

## Phase 1: Trust & Accessibility (2027)

**Goal**: Make USDR usable by researchers who don't know GitHub or YAML.

### P1.1 — Custom Domain
- Register `usdr.science` or equivalent
- Configure GitHub Pages CNAME
- Update all links, preprint, outreach materials
- **Effort**: 1 day | **Impact**: High (professional credibility)

### P1.2 — Submission Portal
- Web form for submitting bridge proposals without YAML knowledge
- Fields map to schema fields
- Generates a GitHub Issue with [BRIDGE] template pre-filled
- **Technology**: Static HTML form + GitHub API
- **Effort**: 1 week | **Impact**: High (opens contribution to non-technical researchers)

### P1.3 — Enhanced Search
- Semantic search (beyond Lunr.js keyword matching)
- Filter by domain, status, catalog type
- "Related bridges" suggestions on each entry page
- **Technology**: Algolia DocSearch (free for open source) or Meilisearch
- **Effort**: 1 week | **Impact**: High (core discovery tool)

### P1.4 — Individual Entry Pages
- Permanent URLs for every bridge, unknown, pioneer, breakthrough gap
- `usdr.science/bridge/percolation-ecology`
- Auto-generated from YAML via CI
- Social sharing cards (OpenGraph)
- **Effort**: 2 weeks | **Impact**: High (linkable, citeable entries)

### P1.5 — Contributor Dashboard
- GitHub-authenticated contributor profiles
- Contribution history and impact metrics
- "Top contributors" leaderboard
- **Technology**: GitHub OAuth + Pages
- **Effort**: 2 weeks | **Impact**: Medium (community motivation)

---

## Phase 2: Interactive Discovery (2028-2029)

**Goal**: The interface becomes an active discovery tool, not just a browser.

### P2.1 — AI Co-pilot Integration
- Chat interface grounded in the USDR knowledge graph
- "Find bridges connecting [domain] to [domain]"
- "What are the open unknowns in [field]?"
- "What breakthrough gap is closest to resolution?"
- **Technology**: RAG over the YAML catalog + LLM API
- **Effort**: 4-8 weeks | **Impact**: Transformative

### P2.2 — Real-time Literature Integration
- Daily arXiv OAI-PMH harvest → flag papers that cite USDR bridges
- Auto-suggest new bridges from abstract analysis
- "New paper found that may resolve unknown X"
- **Technology**: Existing `usdr-ingest` + NLP pipeline
- **Effort**: 2-4 weeks | **Impact**: High

### P2.3 — Cross-domain Discovery Engine
- Interactive "what connects [domain A] to [domain B]?" query
- Path-finding in the knowledge graph (shortest bridge path)
- Visualize all bridges between two selected domains
- **Technology**: D3.js + graph algorithms on existing JSON
- **Effort**: 2 weeks | **Impact**: High

### P2.4 — Collaborative Annotation
- Comment threads on individual entries (GitHub Discussions integration)
- "I tested this bridge in my lab" verification markers
- Expert endorsement system
- **Effort**: 2-4 weeks | **Impact**: High (community trust)

---

## Phase 3: Discovery OS (2030+)

**Goal**: USDR becomes the interface through which researchers interact with all of science.

- Experiment planner: "Design an experiment to test this bridge"
- Simulation integration: run models directly from hypothesis entries
- Federated network: other institutions run USDR mirrors
- AI lab integration: models trained with USDR discovery grounding
- On-chain contribution reputation (optional)
- Physical Discovery Labs running experiments from USDR hypotheses

---

## Design Principles

1. **Progressive enhancement** — works without JavaScript (static HTML baseline)
2. **Mobile first** — researchers use phones; the dashboard must work on mobile
3. **Accessibility** — WCAG 2.1 AA minimum
4. **Speed** — knowledge graph loads in < 3 seconds on 4G
5. **Openness** — no paywalls, no accounts required to browse
6. **Git as truth** — the interface is always derived from the YAML catalog, never the reverse

---

## Technical Stack (Current)

| Layer | Technology | Notes |
|---|---|---|
| Content | YAML (schema-validated) | Git-tracked, CI-validated |
| Build | Python scripts | validate, graph, API, dashboard stats, domain pages, explainers |
| CI/CD | GitHub Actions | validate.yml, build-graph.yml, pages.yml |
| Frontend | Vanilla HTML/CSS/JS | D3.js v7, Lunr.js |
| Hosting | GitHub Pages | Free, CDN-backed |
| API | Static JSON | `api/v1/` directory |
| Search | Lunr.js (client-side) | Phase 1 → Algolia |

## Roadmap Alignment

| Roadmap Phase | Interface Deliverable |
|---|---|
| Phase 0 (2026) | Static dashboard, domain pages, API, knowledge graph — **COMPLETE** |
| Phase 1 (2027-2028) | Custom domain, submission portal, semantic search, entry permalinks |
| Phase 2 (2029-2031) | AI co-pilot, literature integration, discovery engine, collaborative annotation |
| Phase 3 (2032+) | Discovery OS, federated network, experiment planner |
