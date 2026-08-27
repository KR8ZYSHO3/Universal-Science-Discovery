# Path to success — ops appendix (not the product roadmap)

**Canonical product path:** [ROADMAP.md](../ROADMAP.md) (repo root).

This file is **not** a second strategy. Near-term Reddit / LinkedIn / custom domain / “submit arXiv this week” stacks from May 2026 are **parked** (see ROADMAP **Parked — Public launch**). Do not execute them as current work.

**Still valid here:** PR-sized catalog waves (below).

---

## Content wave kickoff (maintainers + contributors)

Large catalog batches (for example **12 bridges + paired unknowns/hypotheses**) should land as **reviewable PRs**, not silent bulk commits, so schema validation, speculation labeling, and graph rebuild steps stay visible in CI.

**Before opening a content PR**

- [ ] Pick or file a scoped issue (or use [good first issue](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/issues?q=is%3Aopen+label%3A%22good+first+issue%22) when `gh` is authenticated locally).
- [ ] Run `python scripts/validate_schemas.py` (or rely on PR CI).
- [ ] For hub-visible counts, run `python scripts/build_graph.py` (or the graph rebuild workflow) so `docs/knowledge_graph.json` meta stays truthful; align README / hub stats if those numbers change.
- [ ] Regenerate domain pages or API slices when the playbook says so — see [DEV_DASHBOARD.md](DEV_DASHBOARD.md).

**Wave Factory bot output**

- [ ] Merge the bot PR when green; paste the successful workflow run URL into the maintainer handoff or issue for traceability.

---

## Historical May 2026 notes (parked)

The previous long form of this page listed: arXiv PDF + upload, r/OpenScience, `usdr.science`, LinkedIn, GitHub Discussions, external contributor DMs, hackathon, arXiv Labs. Those remain in git history and in [LAUNCH_PLAYBOOK.md](../LAUNCH_PLAYBOOK.md). They are **not** the v1.3 engineering slice.

The long-term *goal* (canonical open infrastructure, cited, used, contributed to) is unchanged; the **order of work** is: university-ready product → then citation/launch when the owner un-parks it.
