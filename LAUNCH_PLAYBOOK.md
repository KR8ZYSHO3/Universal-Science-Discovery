# USDR Launch Playbook — 30-Day Takeoff Sequence (June 2026)

**Owner:** Brandon Shoemaker (primary driver, high capacity window open)
**Goal:** Make USDR findable, citable, and attractive to the first wave of serious external contributors.
**Primary Vector:** Launch + Early Ownership (as defined in STRATEGIC_DIRECTIONS_2026.md)
**Secondary Parallel:** Begin light community ownership scaffolding so the project doesn't stay 100% founder-dependent.

This playbook turns the strategic direction into **specific, sequenced, low-ambiguity tasks**. Every item has an owner, estimated effort, and a clear "done" definition. Where possible, I (Grok) can draft, script, or execute large pieces.

**Current Verified Snapshot** (as of latest local checks + `verify_dashboard_consistency.py`):
- 1,124 cross-domain bridges
- 1,409 open unknowns (0 orphans)
- 1,275 falsifiable hypotheses
- 3,861 knowledge graph nodes / 4,522 edges
- 55+ disciplines
- 24 breakthrough gaps, 18 pioneers, 11 phenomenology
- All schemas clean, automation live (Wave Factory Mon+Thu, auto graph rebuilds)

**Success Metrics for 30 Days**
- Preprint submitted with DOI
- Custom domain live (`usdr.science` preferred)
- Dashboard feels like a professional destination (updated messaging + CTAs)
- First 5–10 external people have engaged (issues claimed, PRs opened, or direct outreach replies)
- At least one "Launch Announcement" thread live on a major platform

---

## Phase 0: Preparation (Days 1–3) — Remove Friction

### 0.1 Refresh All Public Numbers (Critical — do this first)
**Why:** Outreach materials and preprint are stale (still reference ~600 entries). This kills credibility on launch.

**Tasks:**
- Run `python scripts/verify_dashboard_consistency.py` locally and capture exact numbers.
- Run `python scripts/update_dashboard_stats.py --apply` (this patches the hub).
- Run `python scripts/build_graph.py` if needed for fresh `docs/knowledge_graph.json` meta.
- Manually or via script update:
  - README.md table + headline text
  - docs/preprint/usdr_preprint.md (abstract + any early numbers)
  - docs/outreach/*.md (all of them)
  - dashboard/index.html OpenGraph + hero stats (via the update script + manual hero polish)
  - STRATEGIC_DIRECTIONS_2026.md and this playbook if they hard-code numbers
- Commit as one "chore: refresh all public metrics for launch" PR.

**I can do:** Draft a small Python helper that pulls the authoritative counts from the verifier + graph meta and generates the Markdown snippets for all the above files.

**Owner:** Brandon (or delegate the run + review)
**Done when:** All public-facing numbers match the verified snapshot and the dashboard shows the fresh stats.

### 0.2 Domain Setup (Already 60% Ready — Finish This Week)
From `docs/CUSTOM_DOMAIN_SETUP.md`:
- CNAME file already committed for `usdr.science`
- DNS instructions are written

**Tasks:**
1. Register `usdr.science` (Namecheap / Cloudflare / Google — ~$12–15/yr). Do this today if not done.
2. Add the exact DNS records listed in the doc (CNAME for www + 4 A records for apex).
3. In GitHub Settings → Pages → Custom domain: enter `usdr.science` + Enforce HTTPS.
4. Update the files listed in the doc (README, preprint, outreach, dashboard og:url, api/v1/meta.json).
5. Add a small "launched on" banner or trust signal once live.

**I can do:** Provide the exact updated text blocks for every file that needs the new domain.

**Owner:** Brandon
**Done when:** https://usdr.science/dashboard/ (or equivalent) resolves with HTTPS and shows the project.

### 0.3 Preprint Polish Pass (Days 2–4)
Current preprint is solid in structure and tone. Needs:
- Number refresh (from 0.1)
- Minor wording updates for current scale ("~4,850+ entries" → exact current total)
- Confirm suggested categories (cs.DL primary + q-bio.QM + physics.soc-ph) still feel right
- Add any new "what's new since v1.1" paragraph if you want to position the scale achievement

**I can do:** Produce a fully refreshed version of the abstract + a clean submission cover letter + recommended cross-list strategy.

**Owner:** Brandon (final review + submission)
**Done when:** You have a submission-ready PDF + metadata ready to upload to arXiv.

---

## Phase 1: Activate the Assets You Already Built (Days 4–10)

### 1.1 Good-First-Issue Activation Wave
You already created ~46 excellent, scoped good-first-issues on May 7 (bridge stubs, unknowns in quantum advantage, tipping cascades, PTLDS, room-temp superconductivity, One Health, etc.). They are high quality.

**Tasks:**
- Review the top 10–12 most attractive ones (I can help rank by "easiest for a domain expert to complete in <1 hour").
- Add clear "estimated time", "skills needed", and "why this matters" to each.
- Pin or label a "Launch Sprint — First Contributions Welcome" set.
- Write one short "Make your first USDR contribution in 20–40 minutes" guide (link from dashboard hero, README, and the issues themselves).
- Post in the issues themselves: "This is now part of our public launch — first external contributors will be highlighted in our announcement."

**I can do:** 
- Produce the ranked top-10 list with suggested edits for each issue.
- Draft the 20–40 minute contribution guide.
- Draft the exact comment template to post on the activated issues.

### 1.2 Dashboard "Launch-Ready" Polish (Parallel with 1.1)
Current strengths: Beautiful dark theme, D3 graph, Lunr search, xref hygiene panel, orphan explorer (recent work), freshness banner.

For external researchers (not just repo insiders):
- Hero section needs stronger researcher-facing messaging ("Map what science doesn't know yet").
- Clear primary CTA: "Start Contributing" (links to the new 20-min guide + good first issues).
- Secondary CTAs: "Read the Preprint", "Explore the Graph", "Join the Launch Sprint".
- Add a small "Recently Merged" or "Highlighted Bridges" carousel/section (even static for v1).
- Update title from "Developer Dashboard" to something warmer like "USDR — Map the Unknowns" or keep both with clear tabs.

**I can do:** Provide the exact HTML/JS diff or new hero block + suggested section additions.

### 1.3 Outreach Material Refresh (After 0.1 numbers are locked)
All files in `docs/outreach/` are valuable but stale on numbers.

**I can do:** Produce refreshed versions of:
- `researcher_pitch.md` (template + 3–4 filled examples for high-leverage domains)
- `reddit_openscience_post.md`
- `linkedin_post.md`
- `twitter_threads.md` (thread + single-post versions)
- Short email template for direct outreach to 20–30 researchers

---

## Phase 2: Coordinated Public Launch (Days 8–18)

### Suggested Sequence (adjust based on your energy)
- **Day 8–10:** Preprint submitted (or at least the PDF + metadata finalized and arXiv account ready).
- **Day 11:** Custom domain live + dashboard updated.
- **Day 12:** Quiet "soft launch" to a small list of people you already know (domain experts in the catalog + previous collaborators) with a personal note + the researcher pitch.
- **Day 13–14:** Coordinated public push:
  - Reddit r/OpenScience (your draft exists)
  - LinkedIn + personal network
  - Twitter/X thread
  - Direct emails to 15–25 researchers (use the personalized pitch)
  - Post in relevant Discord/Slack communities (complex systems, open science, specific disciplines)
- **Day 15+:** Monitor, reply to every comment, thank every new contributor publicly, and feed the best new issues/PRs back into the hub.

**I can do:** Full calendar with exact post drafts, suggested timing, and a "response templates" doc for common questions.

---

## Phase 3: First Ownership Scaffolding (Parallel — Start Day 5)

While the launch is happening, plant the seeds for distribution:

- Create a new GitHub Discussion category: "Stewards & Governance" or "Working Groups".
- Draft a short "USDR Stewards — Call for Early Advisors" post (I can write this).
- Identify 5–8 people from the pioneer list + people whose work is heavily represented in bridges. Send personal notes after the soft launch.
- Document the current "operating rhythm" more visibly (link heavily from the new contribution guide).

Goal by Day 30: At least 2–3 people have said "yes, I can help steward [domain X] or review bridges in my field."

---

## Decision Points & Checkpoints

- **Day 5 Checkpoint:** Numbers refreshed? Domain registered? If not, what is blocking?
- **Day 10 Checkpoint:** Preprint package ready? Top 8 good-first-issues polished and labeled?
- **Day 15 Checkpoint:** First external engagement happened? Dashboard feels launch-worthy to a stranger?
- **Day 25 Checkpoint:** What did we learn from the first outreach wave? Adjust the 90-day plan accordingly.

If any checkpoint is missed, we de-scope ruthlessly (e.g., "launch without custom domain" or "launch with preprint as the main artifact").

---

## Milestone Tracking & Progress Visibility (Non-Negotiable)

This launch will **not** create new sources of complexity or drift.

All launch progress is tracked using the project's existing canonical systems:

- **Primary source of truth:** [.planning/STATE.md](.planning/STATE.md) — every meaningful launch ship must get a concise entry (especially under the new "Launch Execution (June 2026+)" section).
- **Dedicated launch tracker:** [LAUNCH_MILESTONES.md](LAUNCH_MILESTONES.md) — 30/90/180-day checkpoints, current focus, blocked, and next actions (max 5). Update this in parallel with STATE.
- **Visual propagation:** After editing STATE.md, always run:
  ```bash
  python scripts/sync-dashboard-from-state.py
  ```
  This updates `canvases/Progress.canvas.tsx` (and by extension the embedded snapshot visible in Cursor and the contributor hub where relevant).
- **Hub & dashboard honesty:** Use the existing maintainer playbook in [docs/DEV_DASHBOARD.md](docs/DEV_DASHBOARD.md). Run `verify_dashboard_consistency.py` + relevant refresh scripts on any content that touches public counts or the hub.

**Rule:** No major launch artifact ships without a corresponding update to STATE.md + LAUNCH_MILESTONES.md + running the sync script (when applicable).

This keeps the launch execution aggressive while staying 100% native to how the project has successfully managed complexity so far.

## How We Work Together on This

Because the project is complex and you want to trust me on scope:

- I will produce **draft artifacts** (text, code snippets, issue comments, PR descriptions) that you can review/edit/paste.
- You stay the final decider on tone, timing, and what gets shipped.
- We can do focused "execution sessions" where I prepare 3–5 concrete pieces and you choose what to review next.
- All parallel subagent work is coordinated through the orchestration layer and tied back to the milestone system above.

---

**Next Immediate Action (pick one or tell me your preference):**

A. I draft the full refreshed numbers + generate the exact text blocks needed for README, preprint, outreach, and dashboard.
B. I produce the complete "Make your first contribution in 20–40 minutes" guide + ranked top-10 issues with suggested edits.
C. I create the full Launch Calendar + all outreach post drafts (refreshed with current numbers).
D. I prepare the preprint submission package (refreshed abstract + cover letter + cross-list rationale).
E. Something else you want first (tell me).

Just reply with the letter (or describe) and we start executing immediately. No more planning paralysis — we now have a map and a driver.

You built the engine. Let's take off.