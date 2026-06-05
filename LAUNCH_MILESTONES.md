# USDR Launch Execution Milestones — June 2026 Onward

**Purpose:** This file tracks the public launch and early ownership transition as a first-class, visible milestone stream. It lives alongside (and feeds) the canonical [.planning/STATE.md](.planning/STATE.md).

**Philosophy (matching existing project discipline):**
- Milestones are updated after meaningful progress (merged PRs, shipped artifacts, or major external signals).
- Narrative "Last updated" + clear checklists.
- Progress is reflected in the Cursor Canvas (`canvases/Progress.canvas.tsx`) and contributor hub where appropriate.
- Human review gate remains sacred.

**How to update this file + propagate:**
1. Edit this file (narrative + checklists).
2. Add a concise entry to the top of `.planning/STATE.md` under a "Launch Execution" section.
3. Run `python scripts/sync-dashboard-from-state.py` (updates the Canvas snapshot).
4. Run relevant dashboard refresh scripts if numbers or hub content changed.
5. Update this file's "Last updated" and link back to the PR or artifact.

---

## Last Updated

**2026-06-XX — Dashboard Launch Polish + Institutional Framing Complete (M7 / E1)**  
Major public-facing upgrade to dashboard: prominent Launch Sprint banner with researcher + institutional CTAs (graph, preprint, prospectus), new dual-audience value block ("For researchers" + "For institutions & funding partners"), strengthened hero lead and institutional eyebrow, updated pills + trust signals, graph edge count alignment (4,517). This is the first visible step toward fundable institutional presence. OG/Twitter meta already carried launch numbers. Preparation artifacts (prospectus, etc.) now prominently surfaced.

**2026-06-XX — ALL LAUNCH PREPARATION WORKSTREAMS COMPLETE**  
All five parallel preparation streams delivered by specialized agents:

- **A — Numbers & Stats Refresh (M1)**: Complete, verified blocks for every public surface (README, preprint, outreach, dashboard). Fresh scripts confirmed: schemas clean, 0 orphans.
- **B — Contributor Activation**: Full "20–40 min first contribution" guide + ranked Top 10–12 good-first-issues with polished bodies + ready-to-post activation comments.
- **C — Outreach & Launch Calendar**: 30-day detailed calendar + full refreshed posts/templates for Reddit, LinkedIn, X/Twitter, researcher emails + response playbook.
- **D — Preprint Submission Package (M3 prep)**: usdr_preprint.md v1.2 (Launch Edition) + complete ARXIV_SUBMISSION_GUIDE.md (cover letter, recommendations, full checklist) + concise printable checklist.
- **E — Domain + Dashboard + Stewards**: Enhanced CUSTOM_DOMAIN_SETUP.md (zero-ambiguity checklist), dashboard/index.html researcher-facing launch upgrades (hero, CTAs, trust signals), three ready-to-post versions of the Early Stewards / Advisors call.

**Current status**: Launch preparation phase complete. Execution Phase active. High-impact public improvements applied (README badges + banner; dashboard hero rewrite + prominent Launch Sprint banner with CTAs to graph/preprint/prospectus + new researcher/institutional value block). Core institutional funding artifact (INSTITUTIONAL_PARTNERSHIP_PROSPECTUS.md) now directly linked from the live dashboard. This is the first visible step making the project look like serious, fundable research infrastructure for university visits.

**Brutal Reality Check (June 2026)**:
- Preparation quality: Excellent (top 10% of open source launches I've seen).
- Execution momentum: Weak / early. Most artifacts still sitting in files, not live.
- Public face of project: Still mostly pre-launch.
- Ownership distribution: Zero progress so far.
- Risk level: Medium-high of beautiful internal work that doesn't translate to external traction if we don't ship fast in the next 2-3 weeks.

**New Strategic Focus (per your direction)**: Elevate USDR to the point where universities (research offices, libraries, deans, interdisciplinary centers) would genuinely consider **funding or formally supporting** it as strategic infrastructure. This is a higher bar than impressing individual faculty — it requires clear institutional value, a credible partnership model, and positioning around research strategy, open science leadership, and return on investment for the university. Local visits (Hocking College, Ohio University) become early relationship-building steps toward potential institutional support.

---

## EXECUTION PHASE NOW ACTIVE (June 2026)

We have transitioned from "Preparation" → **Execution**.

All foundational artifacts from the five parallel workstreams are delivered and ready to apply.

### Execution Phase Priorities (Next 30 Days)

1. **Apply the Stats Refresh** (highest immediate visual impact)
2. **Post the Stewards / Advisors call** (advances ownership distribution)
3. **Register and configure the custom domain**
4. **Publish the Contributor Guide + activate good-first-issues**
5. **Complete final preprint polish and submit to arXiv**
6. **Execute the coordinated outreach wave**

### Current Execution Milestones

| # | Milestone | Owner | Status | Notes |
|---|-----------|-------|--------|-------|
| E1 | Apply Numbers/Stats blocks to README + dashboard + outreach | Orchestrator + Brandon | **Partial complete** (README fully updated; dashboard hero + Launch Sprint banner + institutional CTA block + trust signals complete; outreach pending) | Highest leverage first step — dashboard now signals serious research infrastructure |
| E2 | Post Early Stewards call (GitHub Discussion + social) | Brandon | In Progress (text finalized in docs/outreach/early_stewards_call.md, ready to post) | Use Version 2 from Subagent E + PR #267 ref |
| E3 | Register `usdr.science` + complete DNS + GitHub Pages | Brandon | Ready | Full checklist in CUSTOM_DOMAIN_SETUP.md |
| E4 | Publish "20-40 min" Contributor Guide + bulk-activate issues | Orchestrator | In Progress (guide in PR; launch comments being added to top GFIs) | Guide already written |
| E5 | Final preprint review + actual arXiv submission | Brandon | Ready (package complete) | Use ARXIV_SUBMISSION_GUIDE.md |
| E6 | Fire coordinated outreach (Reddit / LinkedIn / X) | Brandon + Orchestrator | Ready | Calendar + posts delivered |
| E7 | First 5+ external engagements + public thank-yous | Brandon | Not started | Success signal |

Canvas and STATE.md will be updated after every major E-milestone ship.

---

Canvas + STATE.md synced after this update. All future ships will continue updating these milestone artifacts.

**2026-06-XX — Launch Playbook + Parallel Execution Activated**  
Full launch plan locked in `LAUNCH_PLAYBOOK.md` and `STRATEGIC_DIRECTIONS_2026.md`. Five specialized agents spun up in parallel...

---

## 30-Day Launch Takeoff Milestones (Primary Focus)

**Success Definition:** Preprint submitted with DOI + custom domain live + first external contributors engaged + dashboard feels like a professional destination.

| Milestone | Target | Owner | Status | Artifacts / Links |
|-----------|--------|-------|--------|-------------------|
| **M1: Numbers & Public Stats Refresh** | All public counts accurate and consistent across README, preprint, outreach, dashboard | Orchestrator + Subagent A | **Delivered** (artifacts + verification) | `LAUNCH_STATS_REFRESHED.md` + subagent output; fresh scripts run: schemas OK, 1,408 unknowns, 0 orphans |
| **M2: Domain Live** | `usdr.science` (or equivalent) resolving with HTTPS + all links updated | Brandon | Not Started | `docs/CUSTOM_DOMAIN_SETUP.md` + DNS + GitHub Pages config |
| **M3: Preprint Submission Package Delivered** | Full v1.2 preprint (Launch Edition), ARXIV_SUBMISSION_GUIDE.md (cover letter + detailed checklist + recommendations), concise SUBMISSION_CHECKLIST.md, "What's new" positioning block | Subagent D + Orchestrator | **Delivered** (ready for maintainer upload) | docs/preprint/usdr_preprint.md (v1.2), ARXIV_SUBMISSION_GUIDE.md, SUBMISSION_CHECKLIST.md |
| **M4: Contributor Sprint Activated** | Top 8–12 good-first-issues polished + "20–40 min guide" published + labeled for launch | Orchestrator + Subagent B | In Progress (guide shipped in PR #267; bulk activation comments in progress on GFIs) | `docs/QUICK_START_LAUNCH_SPRINT.md` (shipped); updated issues |
| **M5: Coordinated Public Push** | Reddit, LinkedIn, Twitter, targeted researcher outreach live | Orchestrator + Subagent C | Not Started | Full calendar + refreshed posts |
| **M6: First External Signals** | ≥5 external engagements (issues claimed, PRs opened, or meaningful replies) | Brandon + community | Not Started | GitHub activity + thank-you posts |
| **M7: Dashboard Launch Polish** | Hero/CTA updated for researchers, launch sprint visibility added, trust signals prominent, institutional framing live | Orchestrator + Subagent E | **Complete** (in PR #267: banner + dual-audience block + prospectus link + hero rewrite + link/nav CI fixes) | dashboard/index.html + mkdocs.yml + .markdown-link-check.json |
| **M8: Early Ownership Seeds** | Stewards / Advisors invitation drafted and sent to first 5–8 candidates | Subagent E | In Progress | Stewards charter + personal notes |

**Checkpoint (Day 10):** M1 + M4 + M7 at least partially shipped. Go/no-go on full public push timing.

**Checkpoint (Day 18):** M2 + M3 + M5 complete or very close. First external signals appearing.

---

## 90-Day Momentum Milestones

- 25+ external contributors (issues/PRs/discussions)
- First domain working group or recurring ritual active
- At least one high-quality external contribution merged and highlighted
- AI Co-Pilot scoping document or thin prototype started (if energy allows)
- Custom domain + preprint driving measurable traffic to dashboard
- Initial Stewards/Advisors group formed (3–6 people with clear roles)

---

## 180-Day Ownership Transition Milestones

- Multiple recurring external contributors with domain ownership
- Governance evolution (light advisory circle or stewards model) documented and operating
- Sustainable cadence for Wave Factory + graph automation with distributed review
- First measurable scientific signal (citation, collaboration, or "this hypothesis came from USDR")

---

## Current Focus (Launch Window)

- Execute the five parallel workstreams (Numbers, Contributors, Outreach, Preprint, Domain/Dashboard/Stewards)
- Keep `.planning/STATE.md` and this file in sync after every meaningful ship
- Surface launch progress visibly in the contributor hub and Cursor Canvas
- Protect the existing quality bar and human review gates while accelerating external intake

---

## Blocked / Needs Human

- None (as of last update). Domain registration and preprint submission are the two items that require the maintainer's direct action on accounts/registrars.

---

## Next Actions (Max 5 — Prioritized)

1. Monitor the five running subagents and merge their highest-quality outputs into reviewable artifacts/files.
2. Update `.planning/STATE.md` with a concise "Launch Execution" narrative block (link to this file).
3. Run `python scripts/sync-dashboard-from-state.py` after STATE update.
4. Complete M1 (Numbers refresh) and land the first batch of updated public text.
5. Ship the Contributor Activation guide (`docs/QUICK_START_LAUNCH_SPRINT.md`) and activate the first wave of good-first-issues.

---

**This file is the visible contract for the launch phase.** Treat updates to it with the same rigor as catalog waves: validate, document, sync the Canvas, and keep the hub honest.