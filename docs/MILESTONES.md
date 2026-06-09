# USDR GitHub Milestones

This document defines the official GitHub milestones for the project. These should be created via the GitHub UI or `gh` CLI and then used to track issues and PRs (e.g. assign PR #267 to the launch sprint milestone).

**How to create them:**
After running `gh auth login`, execute the commands below (or create manually at https://github.com/KR8ZYSHO3/Universal-Science-Discovery/milestones).

## Creation Commands (copy-paste after `gh auth login`)

```bash
# 1. Launch Sprint June 2026
gh api repos/KR8ZYSHO3/Universal-Science-Discovery/milestones \
  --method POST \
  -f title="Launch Sprint June 2026" \
  -f description="Complete the initial public launch of USDR. Includes stats refresh, institutional prospectus, dashboard updates (hero, Launch Sprint banner, institutional framing), stewards call, contributor activation, preprint submission, and initial outreach wave. Success criteria: PR #267 merged, first 5+ external engagements, stewards group seeded, custom domain prep complete. All E1-E6 items from LAUNCH_EXECUTION_CHECKLIST.md." \
  -f due_on="2026-07-15T00:00:00Z" \
  -f state="open"

# 2. Custom Domain & Public Infrastructure
gh api repos/KR8ZYSHO3/Universal-Science-Discovery/milestones \
  --method POST \
  -f title="Custom Domain & Public Infrastructure (usdr.science)" \
  -f description="Register and configure usdr.science. Update all links, GitHub Pages, API base URLs, and docs. Enforce HTTPS. Drive measurable traffic from the custom domain." \
  -f due_on="2026-08-31T00:00:00Z" \
  -f state="open"

# 3. Preprint & Academic Visibility
gh api repos/KR8ZYSHO3/Universal-Science-Discovery/milestones \
  --method POST \
  -f title="Preprint & arXiv Submission (v1.2 Launch Edition)" \
  -f description="Finalize and submit the v1.2 preprint to arXiv (cs.DL primary + cross-lists). Obtain DOI. Promote widely. Update all outreach, README, and dashboard with the DOI and citation." \
  -f due_on="2026-07-31T00:00:00Z" \
  -f state="open"

# 4. Contributor Sprint & Early Ownership
gh api repos/KR8ZYSHO3/Universal-Science-Discovery/milestones \
  --method POST \
  -f title="Contributor Sprint & Early Ownership (M4/M8)" \
  -f description="Publish and promote the 20-40 min guide. Bulk-activate and label good-first-issues with launch-sprint. Post and pin the Stewards / Advisors call. Seed the first 5-8 external stewards/advisors. Target: 10-25 external contributors by end of sprint." \
  -f due_on="2026-09-30T00:00:00Z" \
  -f state="open"

# 5. 1,000+ Bridges & Community Momentum
gh api repos/KR8ZYSHO3/Universal-Science-Discovery/milestones \
  --method POST \
  -f title="1,000+ Bridges & 25+ Contributors (90-Day Momentum)" \
  -f description="Reach 1,000+ cross-domain bridges. Grow to 25+ external contributors (issues, PRs, discussions). Form initial domain working groups or recurring rituals. At least one high-quality external contribution merged. Custom domain + preprint driving traffic. Initial Stewards/Advisors group active (3-6 people)." \
  -f due_on="2026-09-30T00:00:00Z" \
  -f state="open"

# 6. Institutional Partnerships Pilot
gh api repos/KR8ZYSHO3/Universal-Science-Discovery/milestones \
  --method POST \
  -f title="Institutional Partnerships Pilot" \
  -f description="Engage 1-2 founding institutional partners (e.g. local Ohio colleges/universities). Run pilot contributions from faculty/students. Shape governance and roadmap with partners. Secure initial support (cash or in-kind). Align with university priorities (research excellence, open science, interdisciplinary, student success)." \
  -f due_on="2026-12-31T00:00:00Z" \
  -f state="open"

# 7. v1.0 Stable Infrastructure
gh api repos/KR8ZYSHO3/Universal-Science-Discovery/milestones \
  --method POST \
  -f title="v1.0 Stable Infrastructure & 10k+ Entries" \
  -f description="Reach v1.0: stable schemas, mature governance (light advisory circle or stewards model), full multi-institutional support model. Target 10,000+ entries with strong coverage across disciplines. AI Co-Pilot v1 in production. Multiple recurring external contributors with domain ownership." \
  -f due_on="2027-06-30T00:00:00Z" \
  -f state="open"

## Usage
- Assign this PR #267 and related issues to the "Launch Sprint June 2026" milestone.
- Update LAUNCH_MILESTONES.md and .planning/STATE.md when a GitHub milestone is closed or progress is made.
- Run `python scripts/sync-dashboard-from-state.py` after changes.

See also: LAUNCH_MILESTONES.md, ROADMAP.md, .planning/STATE.md