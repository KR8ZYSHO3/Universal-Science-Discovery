# Path to Success — USDR Strategic Roadmap

**Last updated:** 2026-05-07 (post Waves 57-67 + OA-1 — full audit)

**Roadmap framing:** **Phase 0 — Foundation** is **complete** (governance, tooling, seeded catalog, graph, automation). Discoverability, outreach, and first-external-contributor milestones sit in **Phase 1 — Discovery & adoption** — see [ROADMAP.md](../ROADMAP.md). Engineering (bridges, harvesters, dashboard) continues in parallel and is not paused waiting on Phase 1.

---

## Where We Are (May 2026)

The Universal Science Discovery Repository has completed a major content-build sprint (Waves 1–67). The infrastructure is mature and the automation pipeline is live:

**Catalog (Waves 57-67 complete — verified 2026-05-07):**
- **868** cross-domain mathematical bridges with translation tables and DOI references
- **1,151** open unknowns across 55+ scientific domains (0 orphans)
- **1,019** testable hypotheses linked to unknowns (crossed 1,000-hypothesis milestone)
- **18** pioneer profiles seeding further bridges
- **12** breakthrough gaps tracking the most important unsolved cross-domain problems
- **4** pre-formal observations in the phenomenology catalog
- **3,072-node** knowledge graph (3,259 edges) — crossed 3,000-node milestone

**Infrastructure:**
- Schema validation CI on every PR (0 errors, 0 warnings — verified 2026-05-07)
- Static JSON API at `api/v1/` (unknowns, bridges, hypotheses, domains, graph)
- Interactive D3 graph dashboard with Lunr.js full-text search
- 55+ domain landing pages auto-generated from catalog
- Bridge explainer HTML pages for featured bridges
- Pioneer profiles section and breakthrough gaps tracker
- arXiv preprint ready (`docs/preprint/usdr_preprint.md`)
- Dual licensing: CC BY 4.0 (content) + MIT (code)
- **OpenAlex weekly harvest cron job** — automation continuous growth pipeline live
- **PubMed + Semantic Scholar harvesters** — built and operational
- **9 draft bridge stubs** in `drafts/bridges/` from OpenAlex harvest, awaiting promotion

**Strategic shift — bridge count is no longer the bottleneck:**
The automation pipeline (OpenAlex cron + harvesters) ensures continuous bridge growth. The new bottlenecks are:
1. **Discoverability** — arXiv preprint, Reddit/LinkedIn post, domain expert outreach
2. **Contributor on-ramp** — good-first-issues, QUICK_START_CONTRIBUTING.md, submission portal

**What we still do NOT have:**
- Any external contributors
- An arXiv DOI / academic citation
- A custom domain
- More than ~0 GitHub stars from people we didn't tell about it
- Any researcher outreach completed

---

## The Goal

USDR aims to become the **canonical open infrastructure for cross-domain scientific knowledge** — the place researchers, educators, and AI systems go to find mathematical bridges between disciplines.

Success looks like:
- Cited in peer-reviewed literature
- Used by researchers as a discovery tool
- Contributed to by domain experts across fields
- Referenced by arXiv Labs and similar science infrastructure
- Stable enough to outlast any single contributor

---

## Current Priority Stack (Updated 2026-05-10)

Bridge count is no longer the only bottleneck — automation handles continuous growth. Priorities are **parallel tracks** (see [ROADMAP.md](../ROADMAP.md) § “Integrated development priorities”):

1. **Discoverability & adoption (Phase 1)** — arXiv preprint DOI, coordinated outreach, first external contributors, hackathon.
2. **Trust surfaces** — contributor hub, `/domains` pages, CI status widget, and static API must reflect git (`update_dashboard_stats.py`, `generate_domain_pages.py`, `verify_domain_pages.py`, `render_breakthrough_gaps_hub.py`, `generate_api.py`); run **`mkdocs build --strict`** when docs change.
3. **Breakthrough gaps maturity** — steward `breakthrough-gaps/bg-*.yaml`: accurate TRL, blocking gaps, **`required_bridges`** mapped to real `b-*` IDs; hub cards generated from YAML ([BREAKTHROUGH_GAPS.md](BREAKTHROUGH_GAPS.md)).
4. **Catalog depth** — promote `drafts/bridges/` stubs; waves; harvesters; graph rebuild cadence.
5. **Dashboard reliability** — D3 interactive graph must load on GitHub Pages consistently.

---

## Near-Term Actions (Next 2 weeks)

### Priority 1: arXiv Preprint Submission

**Why:** Establishes academic priority, makes the project findable via academic search, enables citation by others.

**How:**
- Convert `docs/preprint/usdr_preprint.md` to PDF (use Pandoc with a LaTeX template or Overleaf)
- Create an arXiv account at [arxiv.org/user/register](https://arxiv.org/user/register)
- Submit to **cs.DL** (Digital Libraries) with cross-lists to `q-bio.QM`, `physics.soc-ph`
- Include the GitHub URL and live dashboard URL in the abstract
- Expected outcome: indexed within 24–48 hours, citable within 1 week

**Resources:**
- Preprint file: `docs/preprint/usdr_preprint.md`
- Pandoc command: `pandoc docs/preprint/usdr_preprint.md -o usdr_preprint.pdf --pdf-engine=xelatex`

---

### Priority 2: Reddit r/OpenScience Post

**Why:** First public exposure to the exact right audience — open science researchers who feel the cross-domain problem acutely.

**How:**
- Post is ready at `docs/outreach/reddit_openscience_post.md`
- Post time: Tuesday–Thursday, 9–11am EST (peak r/OpenScience engagement)
- Engage with every comment in the first 2 hours — this is the critical window
- Cross-post to r/dataisbeautiful (graph visualization angle), r/science (epistemology angle)

**Expected outcome:** 50–500 upvotes, 5–50 GitHub stars, 1–5 researcher contacts

---

### Priority 3: Custom Domain

**Why:** Professional credibility before major outreach. A GitHub Pages URL looks like a hobby project; a custom domain signals seriousness.

**How:**
- Check availability: `usdr.science`, `crossdomainscience.org`, `sciencebridges.org`
- Register at Namecheap or Google Domains ($12–15/year)
- Configure GitHub Pages custom domain:
  1. Add a `CNAME` file to the repo root containing your domain
  2. In GitHub repo settings → Pages → Custom domain, enter the domain
  3. Add DNS A records pointing to GitHub Pages IPs (listed in GitHub docs)
- Update all links in README, preprint, and outreach materials
- Expected outcome: 1 day setup, permanent professional URL

---

### Priority 4: LinkedIn Post

**Why:** Reaches researchers, data scientists, science communicators — a different audience than Reddit.

**Post:** Ready at `docs/outreach/linkedin_post.md` (if this file doesn't exist, draft it from the Reddit post with professional framing).

**Angle:** "I cataloged 180 mathematical bridges between scientific disciplines and built an open knowledge graph. Here's what I found..." — personal, data-forward, shows the tool.

---

### Priority 5: Enable GitHub Discussions

**Why:** Community infrastructure for async collaboration. Issues are for specific tasks; Discussions are for open conversation.

**How:**
- Repo Settings → Features → Discussions → Enable
- Create seed posts:
  - "Introduce yourself — what domain are you from?"
  - "Bridge proposals — what cross-domain connections do you suspect exist?"
  - "Open questions — which unknowns matter most in your field?"

---

## Medium-Term (1–3 months)

### Get 3 External Contributors

**Why:** External contributions are the legitimacy signal that transforms a solo project into a community resource. A single external PR is worth more than 100 internal bridges.

**Target profiles:**
- 1 physicist who works in cross-domain applications (biophysics, econophysics, network science)
- 1 biologist who uses mathematical models (computational biology, systems biology)
- 1 computer scientist interested in science infrastructure (knowledge graphs, semantic web, AI for science)

**How:**
- Use `docs/outreach/researcher_pitch.md` as the email template
- Find targets: corresponding authors of cross-domain papers on arXiv (search "biology physics mathematical bridge" or similar)
- LinkedIn / Twitter/X DMs to researchers with cross-domain work visible in their profiles
- The bar to contribute is deliberately low: editing a YAML file is all that's required, and CONTRIBUTING.md walks through it step by step

---

### arXiv Labs Application

**URL:** [labs.arxiv.org](https://labs.arxiv.org)

**Pitch:** "Open cross-domain bridge catalog seeded from arXiv OAI-PMH. 180+ bridges, 1,000-node knowledge graph, JSON API. Candidate for Labs listing as a science discovery tool."

**Timing:** After the preprint is submitted and has an arXiv ID.

**Why it matters:** arXiv Labs is curated and widely seen by researchers. A listing there would be permanent, credible discoverability.

---

### First Hackathon

**Plan:** Propose a one-day virtual hackathon: "Bridge Sprint — map 10 new cross-domain connections in one day."

**How:**
- Announce in GitHub Discussions
- Post to r/OpenScience and science Twitter
- Provide: a list of 20 high-priority orphan unknowns from `docs/orphan_unknowns.md`, the CONTRIBUTING.md workflow, and a judge panel (you + 2 willing researchers)
- Prize: a named credit in the arXiv preprint's acknowledgments section

---

### Semantic Scholar API Integration

**Why:** Auto-link bridges to papers, surface the actual citation network, validate that DOIs are real.

**How:**
- Use the [Semantic Scholar Open Data Platform API](https://api.semanticscholar.org/api-docs/)
- Write a script that takes DOIs from bridge YAML files and fetches paper metadata (title, abstract, citation count, related papers)
- Add a `validated_doi` flag to bridge YAML when a DOI resolves
- Surface citation counts on bridge explainer pages

---

## Long-Term (3–12 months)

### Custom Web Application

The current dashboard is a static HTML file. A proper web application would enable:

- **Full-text search** with relevance ranking (Algolia, Meilisearch, or self-hosted Typesense)
- **Submission portal** — a web form for proposing bridges without needing to know YAML
- **User accounts** and contribution tracking
- **Peer review workflow** for proposed bridges (vote, comment, flag concerns)
- **API authentication** for programmatic access

**Tech stack recommendation:** Next.js (static export for GitHub Pages compatibility) + Supabase (auth + database for submissions) + existing static JSON API for data.

---

### Integration Targets

| Service | What to build | Priority |
|---------|--------------|---------|
| Semantic Scholar API | Auto-link bridges to papers, validate DOIs, surface h-index of cited authors | High |
| OpenAlex | Citation network overlays on the knowledge graph | Medium |
| Wikidata | Link bridge entities (concepts, pioneers) to structured knowledge | Medium |
| arXiv OAI-PMH | Continue automated harvesting to seed new unknowns | Ongoing |
| arXiv Labs | Official listing in the Labs directory | High (after preprint) |

---

### Funding

The preprint + community traction is the prerequisite for any grant application.

**Targets:**
- **NSF EAGER** — "EArly-concept Grants for Exploratory Research" — designed for high-risk, high-reward early-stage projects. Cross-domain science infrastructure fits well.
- **Sloan Foundation** — explicitly funds open science infrastructure. Has funded similar knowledge-graph projects.
- **HELIOS / SPARC** — open access and open science advocacy funds.
- **NIH Open Science Prize** — if biomedical bridge content is developed further.

**What to build before applying:**
1. arXiv preprint with a DOI
2. 3+ external contributors (shows community)
3. 500+ GitHub stars (shows adoption)
4. Dashboard visitor data (Google Analytics or Plausible — add to dashboard now)

---

## Quality Standards Going Forward

Every new bridge must have:
- [ ] Real DOI citations (no fabricated references — verified against Semantic Scholar or doi.org)
- [ ] Mathematical translation table (≥3 rows)
- [ ] `status` field honestly set (established / proposed / speculative)
- [ ] Linked unknown and hypothesis
- [ ] Schema validation passing (`python scripts/validate_schemas.py`)

Every contribution must pass CI before merge.

**Run this before any content PR:**
```bash
python scripts/validate_schemas.py   # must exit 0
python scripts/audit_quality.py      # review any WARN items
```

---

## Metrics to Track

| Metric | Current (2026-05-07) | 3-month target | 12-month target |
|--------|--------------------|----------------|-----------------|
| Cross-domain bridges | **868** | 1,000 | 2,000 |
| External contributors | 0 | 3 | 20 |
| GitHub stars | ~0 public | 100 | 500 |
| arXiv citations | 0 | 1 (self) | 10 |
| Monthly dashboard visitors | unknown | 500 | 5,000 |
| Breakthrough gaps with active research linked | 0 | 2 | 5 |
| Domains with ≥5 bridges | ~20 | 30 | 50 |
| Orphan unknowns (no connections) | **0** | 0 | 0 |
| Hypotheses | **1,019** | 1,200 | 2,500 |
| Unknowns | **1,151** | 1,400 | 3,000 |

---

## What Would Make This Project Fail

Being honest about failure modes:

1. **Fabricated citations** — one discovered fake DOI would destroy credibility permanently. Every reference must resolve at doi.org or arxiv.org.
2. **No external contributors** — a solo project with 1,000 entries is a dataset; a community project with 10 contributors is an institution.
3. **Scope creep** — adding non-mathematical "bridges" (vague analogies, hand-wavy connections) dilutes the value. The translation table requirement is the quality gate.
4. **Abandonment** — the biggest risk. The outreach steps are the insurance: an arXiv DOI, a Reddit post, and 3 researchers who know about it make the project much harder to forget.
5. **Stale dashboard** — if CI breaks and stats drift from catalog truth, trust erodes. The `validate.yml` and `update_dashboard_stats.py` actions are the safeguard; keep them green.

---

## The Single Most Important Next Action

**Submit the arXiv preprint.**

Everything else (outreach, contributors, funding, integrations) flows from having an academic citation. Without it, USDR is a GitHub repo. With it, USDR is a citable open science infrastructure project.

The preprint is written and ready (`docs/preprint/usdr_preprint.md`). The only thing required is converting it to PDF and creating an arXiv account.

**Do this first.**
