# USDR Roadmap

**This is the only product-path document.** Other “strategy” files are appendices or GSD execution notes. If they disagree with this file, this file wins.

| You want | Read |
|----------|------|
| **How to use the repo** (look / add / run) | [`docs/USE.md`](docs/USE.md) |
| Where the project is going | **This file** |
| How we execute the *current* engineering slice | [`.planning/ROADMAP.md`](.planning/ROADMAP.md) (GSD phases) |
| Hub / UX program (later) | [`INTERFACE.md`](INTERFACE.md) |
| Parked public launch (arXiv submit, outreach, DNS) | [`LAUNCH_PLAYBOOK.md`](LAUNCH_PLAYBOOK.md) |
| Catalog PR-sized waves (ops checklist) | [`docs/PATH_TO_SUCCESS.md`](docs/PATH_TO_SUCCESS.md) |

---

## The Open-Source Engine That Will Redefine Scientific Discovery

By 2035, the **Universal Science Discovery Repository (USDR)** aims to be trusted scientific infrastructure: a living, version-controlled catalog of unknowns, hypotheses, and cross-domain bridges, with **Crosscheck** — runnable experiments that falsify bridge claims.

This is not another database. Git is the source of truth. The hub is a view of git.

**Owner constraint (2026-08-26):** Do **not** market, post, or cold-email until the product is impressive to a serious researcher in the room. Then present it at a university for testing. **arXiv submit** is important for a DOI at that point — not a substitute for finishing the product.

---

## Now — University-ready robustness (v1.3)

**Goal:** One person can run the repo honestly; a first visit to the hub holds up; Crosscheck is a closed loop; **the flow is three doors, not eight start-here docs.**

Utilization model: [`docs/USE.md`](docs/USE.md) — **Try it** · **Add a question** · **Keep it honest**. Plain language on the front door; GitHub words stay in the contributor guide.

| ID | Work | Why a researcher cares |
|----|------|------------------------|
| **FLOW-01** | Hub and docs present the three doors; extra “start here” pages defer to USE.md | They should not have to pick among ONBOARDING, launch sprint, and five-step cards |
| **WORK-01** | Crosscheck `RESULT:` writes through to catalog/hub status | They run an experiment and the site still looks unchanged |
| **UI-01** | Hub first-visit audit (counts, links, Crosscheck, no broken loads) | Ten-minute bounce or stay |
| **ROBUST-01** | One ordered maintainer command list | A student can operate it without tribal knowledge |
| **WORK-02** | Catalog batch = one documented local run | Not a scavenger hunt |

Execution: GSD **v1.3**, phases starting at **6** — [`.planning/ROADMAP.md`](.planning/ROADMAP.md).

**Not in v1.3:** Reddit, LinkedIn, DMs, hackathon, custom domain, arXiv **upload**.

---

## Shipped

### Phase 0 — Foundation (2026) — complete

Governance, schemas + CI, hub + API + graph, seeded catalog at scale, harvesters. Calendar outcomes (stars, first 50 contributors) were never the foundation gate.

### v1.1 — Core Development (GSD phases 1–5) — shipped 2026-08-26 (PR #308)

- 4/4 seed Crosscheck protocols CI-gated `RESULT: CONFIRMED` (epidemic = volume ν̄=3, not chemical ν=1)
- Generate → human-promote → repro path (`p-b-percolation-oncology-gcc`, honest `INCONCLUSIVE`)
- CONFIRMED-gate inventory + generate/GCC smokes in `tests/repo_smoke`
- Hub `#recommendations` (undirected degree; **contributor tooling, not a scientific ranking**)

Archive: [`.planning/milestones/v1.1-ROADMAP.md`](.planning/milestones/v1.1-ROADMAP.md)

---

## Parked — Public launch (labeled v1.2)

Outreach, `usdr.science`, arXiv **submit**, researcher DMs — [`LAUNCH_PLAYBOOK.md`](LAUNCH_PLAYBOOK.md). Owner parked 2026-06-23; reaffirmed 2026-08-26.

When un-parked: convert [`docs/preprint/usdr_preprint.md`](docs/preprint/usdr_preprint.md), then submit. Do not treat the May 2026 “arXiv this week / Reddit / domain” stack in old notes as current.

Preprint, coordinated launch, first 50 contributors, hackathon, and custom domain stay on this parked track — not the next engineering slice.

---

## Later — after the product is the argument

**Momentum / acceleration / transformation** (2027–2035): institutional partners, citeable papers, richer interface ([`INTERFACE.md`](INTERFACE.md) program), “Discovery OS.” Do not pull those into v1.3.

INTERFACE.md uses its **own** Phase 1/2/3 labels for UX. Map:

| This file | INTERFACE.md |
|-----------|----------------|
| Foundation | Static hub — live |
| University-ready (now) | Trust surfaces on the **existing** hub; no custom domain yet |
| Parked launch | P1.1 domain + outreach |
| Momentum+ | INTERFACE “Trust & Accessibility” and later |

---

## Engineering tracks (run without adoption)

| Track | What | Notes |
|-------|------|--------|
| **B — Trust surfaces** | Hub/API/docs match git | `verify_dashboard_consistency.py`, domain pages, `mkdocs build --strict` |
| **C — Breakthrough gaps** | World-scale problems ↔ bridges | `breakthrough-gaps/`, hub grid |
| **D — Catalog depth** | Waves, stubs, harvesters | Human review gate; PR-sized batches |

**Rule:** Hub-visible content ships with regenerated dashboard/docs in the same PR or an immediate follow-up.

Catalog wave **ops** checklist (not a second strategy): [`docs/PATH_TO_SUCCESS.md`](docs/PATH_TO_SUCCESS.md).

---

## Snapshot (hub-consistent; re-verify with `python scripts/verify_dashboard_consistency.py`)

| Metric | Approx. (2026-05-10 table; live numbers on the hub) |
|--------|------------------------------------------------------|
| Bridges | 1,124+ |
| Unknowns | 1,409+ |
| Hypotheses | 1,275+ |
| Graph | 3,861 nodes / 4,522 edges |
| Domains | 55+ |

---

## Guiding principles

- **Discovery first** — features must help someone find or test what is not yet known
- **Honesty** — no fabricated `RESULT: CONFIRMED`; GSD artifacts are process metadata, not science
- **Python canonical** — browser/Colab are demo tier
- **Quality over vanity metrics** — stars and posts wait until the demo is real
- **Git is the source of truth** — the hub is a view

Foundation is complete. **Next build is university-ready robustness**, not a public campaign.
