# USDR Unknowns Hackathon — June 2026 (Virtual)

**"What does science not yet know? Let's map it."**

## Overview

The first Universal Science Discovery Repository Hackathon is a 48-hour virtual event
where researchers, students, and curious minds contribute to mapping humanity's open
scientific questions.

**Dates:** June 14–15, 2026 (48 hours, async-friendly)
**Format:** Virtual, async-first (no required live sessions)
**Platform:** GitHub + Discord (to be set up)

## Goals

By the end of the hackathon, we aim to:

- Add 200+ new unknowns across all domains
- Create 10+ new cross-domain bridges with mathematical translation tables
- Connect 50+ existing orphan unknowns to bridges or hypotheses
- Welcome 20+ first-time contributors to the repo

## Tracks

### Track 1: Domain Expert (Any level)

**What:** Add unknowns from your field that the repository is missing
**How:** Fork → add `unknowns-catalog/{your-domain}/u-{slug}.yaml` → PR
**Time:** 30 minutes per unknown
**Difficulty:** Beginner-friendly

### Track 2: Bridge Builder (Intermediate)

**What:** Formalize a mathematical connection between two fields
**How:** Write a `cross-domain/{d1}-{d2}/b-{slug}.yaml` with translation table
**Time:** 2-4 hours per bridge
**Difficulty:** Intermediate — requires cross-domain knowledge

### Track 3: Orphan Adopter (Any level)

**What:** Find orphan unknowns (see `docs/orphan_unknowns.md`) and write a hypothesis or bridge for them
**How:** Create `hypotheses/active/h-{slug}.yaml` referencing the unknown
**Time:** 1-2 hours per hypothesis
**Difficulty:** Beginner-friendly

### Track 4: Co-pilot Extension (Advanced)

**What:** Improve the AI co-pilot scripts or add new analysis tools
**How:** Contribute to `scripts/` — new analysis, better bridge scoring, visualization
**Time:** Half-day to full day
**Difficulty:** Advanced — Python required

## Prizes / Recognition

- **All contributors:** listed in CONTRIBUTORS.md and a special "Hackathon 2026" badge in their PR
- **Top bridge:** featured on the dashboard "Discovery Engines" section
- **Top unknown cluster:** written up in the next X.com thread
- **Most domains covered:** special mention in the CHANGELOG

## How to Participate

1. Star and fork the repo: <https://github.com/KR8ZYSHO3/Universal-Science-Discovery>
2. Join Discord: [link TBD]
3. Pick a track and an issue from the Issues tab (filter by `good first issue`)
4. Submit PRs — maintainers will review within 24 hours during the event
5. Share your contribution on X.com with **#USciDR**

## Judging Criteria

- **Scientific accuracy** — is the unknown real? is the bridge rigorous?
- **Novelty** — new connections, new domains
- **Quality of writing** — is the question well-formed? does the translation table hold?
- **Bridges over unknowns** — bridges are harder, more valuable

## Schedule

| Date | Milestone |
|------|-----------|
| **June 1** (T-2 weeks) | Announce on X.com, arXiv mailing lists, Reddit r/science, r/MachineLearning, r/Physics |
| **June 7** (T-1 week) | Discord opens, pre-registration, Q&A session |
| **June 14 00:00 UTC** | Hackathon begins — start submitting PRs |
| **June 15 23:59 UTC** | Hackathon ends — no new PRs after this |
| **June 16–17** | Judging, winner announcement, blog post |

## Outreach Targets

- **arXiv mailing lists:** cond-mat, q-bio, cs.AI, physics
- **Reddit:** r/science, r/MachineLearning, r/Physics, r/Biology, r/math
- **X.com:** science communicators, academic Twitter
- **Research groups:** cold email 10 labs whose work maps onto existing bridges
- **Hackathon aggregators:** Devpost, MLH, hackathon calendars

## Resources for Participants

- [CONTRIBUTING.md](../../CONTRIBUTING.md)
- [Schema docs](../../schemas/)
- [Live dashboard](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/)
- [Orphan unknowns (contribution targets)](../orphan_unknowns.md)
- [Bridge proposals from AI co-pilot](../bridge_proposals.json)
