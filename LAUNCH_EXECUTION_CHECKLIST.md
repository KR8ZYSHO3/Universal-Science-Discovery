# USDR Launch Execution Checklist — Execution Phase (June 2026+)

**Purpose:** This is the living, checkable execution checklist for the public launch and early ownership transition. It turns the milestones in `LAUNCH_MILESTONES.md` into actionable, prioritized tasks.

**How to use:**
- Update the Status column as you go.
- After any meaningful progress, add a line to `.planning/STATE.md` and run `python scripts/sync-dashboard-from-state.py`.
- Keep this file in sync with `LAUNCH_MILESTONES.md`.

**Current Phase:** EXECUTION (Preparation complete — all five workstreams delivered)

---

## Phase 1: Immediate High-Impact Application (Next 3–7 Days)

### E1 — Apply Core Stats Refresh (Highest leverage first step)
- [x] Update README.md badges + launch banner (applied)
- [x] Update `dashboard/index.html` hero pills, stat IDs, OG/Twitter meta, Launch Sprint banner + CTAs, researcher/institutional value block, trust signals (complete)
- [x] Update all 5 files in `docs/outreach/` with refreshed numbers and launch language (all done: reddit, linkedin, researcher_pitch, arxiv_abstract, twitter_threads; early stewards call ready + in nav)
- [x] Update `docs/preprint/usdr_preprint.md` to v1.2 Launch Edition + full submission package (complete)
- [ ] Create ready-to-post Stewards / Advisors call (complete — see docs/outreach/early_stewards_call.md)
- [ ] Run full verification + commit batch
- Status: **E1 dashboard + core artifacts in PR #267; outreach refresh started (2/5 + stewards call); link + mkdocs CI fixes landed**

### E2 — Post Early Stewards / Advisors Call (Ownership distribution)
- [ ] Post Version 2 (GitHub Discussion) in the repo Discussions tab
- [ ] Share Version 1 on X/LinkedIn/personal channels
- [ ] Pin the Discussion
- [ ] Add link to dashboard hero and README
- Status: **Ready** (three versions delivered by Subagent E)

### E3 — Domain Finalization
- [ ] Register `usdr.science` (or chosen domain)
- [ ] Add DNS records (A + AAAA + CNAME) — full list in `docs/CUSTOM_DOMAIN_SETUP.md`
- [ ] Configure in GitHub Pages + Enforce HTTPS
- [ ] Update all files listed in the domain checklist (dashboard, README, preprint, API, generators, etc.)
- [ ] Regenerate domain/explainer pages
- Status: **Ready** (zero-ambiguity checklist exists)

---

## Phase 2: Contributor & Visibility Activation (Parallel with Phase 1)

### E4 — Activate Contributor Pipeline
- [ ] Publish `docs/QUICK_START_LAUNCH_SPRINT.md` (or integrate into CONTRIBUTING.md)
- [ ] Bulk-apply improvements + activation comments to the Top 10–12 good-first-issues (prepared by Subagent B)
- [ ] Add `launch-sprint` and `easy-win` labels
- [ ] Update dashboard hero with direct link to the new guide + activated issues
- Status: **Guide written, issues ranked + comments prepared**

### E5 — Preprint Submission
- [ ] Final review of `docs/preprint/usdr_preprint.md` v1.2 (Launch Edition)
- [ ] Generate PDF
- [ ] Submit to arXiv (use `ARXIV_SUBMISSION_GUIDE.md` + `SUBMISSION_CHECKLIST.md`)
- [ ] Post submission announcement (using outreach templates)
- Status: **Package complete and ready**

---

## Phase 3: Public Launch Wave (Coordinated Push)

### E6 — Execute Outreach Calendar
- [ ] Fire coordinated posts per the 30-day calendar (Reddit flagship, LinkedIn long post, X thread, email blast)
- [ ] Use refreshed content from Subagent C
- [ ] Daily engagement using the Response Playbook
- [ ] Public contributor spotlights as first PRs/issues land
- Status: **Calendar + all content ready**

---

## Ongoing / Tracking (Non-Negotiable)

- [ ] After every meaningful ship: Update `.planning/STATE.md` + `LAUNCH_MILESTONES.md` + run `python scripts/sync-dashboard-from-state.py`
- [ ] Update this checklist with status and dates
- [ ] Maintain visible progress in the contributor hub and Cursor Canvas
- [ ] Track first external engagements (issues/PRs/DMs/replies) publicly

---

**Last major update:** 2026-06-XX — All preparation complete, Execution Phase activated. E1 in progress. INSTITUTIONAL_PARTNERSHIP_PROSPECTUS.md created as the flagship artifact for university funding conversations. Most application work still pending.

**Brutal Note (added 2026-06-XX):** Preparation is now excellent. Execution is still weak. We have beautiful artifacts but almost zero public shipping. The next 10-14 days will decide if this launch actually gains traction or stays as high-quality internal work.

**New Focus (per your input):** Higher ambition — position USDR as something universities (research offices, libraries, deans, centers) would actively consider **funding or formally supporting** as strategic infrastructure. This requires developing a clear institutional value proposition, partnership models, and materials aimed at administrators and research leadership, not just individual faculty. Local visits become relationship-building steps toward potential institutional investment.

**Owner:** Brandon (primary) + Orchestration support available for drafting, applying blocks, and coordination.

This checklist will be the single place to see "what's next" at a glance. Keep it brutally honest and up to date.