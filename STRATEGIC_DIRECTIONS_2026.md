# USDR Strategic Directions — June 2026

**Context for this document**  
You (the founder/maintainer) have:
- Very high personal capacity right now (15–30+ hrs/week for the next 3–6 months).
- Extremely strong foundational work already shipped (governance, schemas, Wave Factory + graph automation, content velocity, ethics, documentation hygiene, contributor hub).
- The main current source of friction is **"uncertainty about the right next direction"**.
- You are **very open to distributing ownership** quickly.
- All major outcome categories matter to you (visibility, community, AI co-pilot, scientific impact, platform maturity, funding, scale).
- No hard constraints — open to bold moves.

This document gives you clear options, trade-offs, and a recommended path so you can stop spinning and start executing with focus.

---

## Current Reality (Honest Assessment)

**Superpowers**
- One of the best-executed "founder + heavy automation" science infrastructure projects I've seen at this stage.
- Git-native + rigorous human gates + sophisticated CI (Wave Factory on Mon/Thu cadence, auto graph+dashboard rebuilds via bot PRs, dual validation, freshness metadata).
- Exceptional documentation and process (AGENTS.md, DOC_MAP, OPERATING_RHYTHM, VISION_AND_SCOPE, INTERFACE.md, etc.).
- Real content velocity (1,100+ bridges, 1,400+ unknowns, clean graph, 0 orphans).
- Live, polished dashboard already deployed.

**The Core Problem Right Now**
You have built a **jet engine** (the automation + schemas + catalog) but have not yet taken off (no external contributors, preprint not submitted, low visibility, uncertainty about sequencing).

The project is at the classic "successful prototype → real infrastructure" transition point. Most projects die or stall here.

**Closest Real-World Analogs** (from research)
- **Open Research Knowledge Graph (ORKG)** — closest in spirit (structured scholarly knowledge + problems/hypotheses).
- **OpenProblems.bio** — excellent model for focused problem definition + community benchmarking.
- Successful long-lived infra (arXiv, OpenAlex, Zotero, OSF) all eventually adopted **POSI principles** (stakeholder governance, diversified sustainability, technical insurance) and moved from founder-driven to distributed ownership.

Your project is unusually well-positioned because you already have the governance documents and ethical posture that most projects add years later.

---

## Three Coherent Strategic Paths

### Path A: Launch & Visibility Flywheel (Recommended Primary Vector for next 6 months)
**Goal**: Make USDR *findable and citable* so the existing assets start attracting people and momentum.

**Core moves**
- Submit the preprint (cs.DL + cross-lists) with a real DOI.
- Register a custom domain + professional landing experience.
- Execute a coordinated launch (your existing outreach materials + targeted academic + social push).
- Activate the 40+ excellent "good first issue" stubs you already created.
- Run the first small "Unknowns Contribution Sprint" or virtual event.

**Why this fits you**
- Plays to your high capacity right now.
- Creates fast feedback loops (the thing you're missing most).
- Unlocks everything else (community, citations, funding interest, AI co-pilot users).
- Leverages the incredible work you've already done.

**Trade-offs**
- Short-term focus on "marketing" and process (less pure content waves).
- Requires some extroversion/outreach energy.

**90-day target**: Preprint live with DOI + custom domain + first 10–20 external contributors + measurable traffic to the dashboard.

### Path B: Community Ownership Transition (Strong Parallel Track)
**Goal**: Stop being the single point of failure and start building a real movement.

**Core moves**
- Formalize lightweight governance (Advisory Circle or "USDR Stewards" — 5–8 respected people across domains).
- Create clear maintainer + contributor ladders + recognition systems.
- Build multiple low-friction on-ramps (the submission portal from INTERFACE.md Phase 1 is perfect here).
- Run regular rituals (monthly triage calls, domain working groups, contribution sprints).
- Document the "USDR operating system" so others can run pieces.

**Why this fits you**
- You explicitly said you want to distribute ownership quickly.
- Your existing docs (GOVERNANCE, WORKSTREAMS, CONTRIBUTING, issue templates) are already 80% of the way there.
- High personal capacity gives you the runway to do the initial handoff work well.

**Trade-offs**
- Slower in the very short term while you teach and onboard.
- Requires comfort with imperfect (but good-enough) contributions.

**90-day target**: At least 3–5 recurring external contributors, one domain working group running, first non-founder merge of substance.

### Path C: AI Co-Pilot as the Killer Differentiator (High-Leverage Bet)
**Goal**: Build the thing that makes USDR *uniquely* powerful and sticky.

**Core moves**
- Treat the existing prompts + Wave Factory + graph as the grounding layer.
- Ship a real (even simple) chat/exploration interface grounded in the USDR catalog + literature.
- Make it dramatically better at cross-domain reasoning than generic LLMs.
- Use this as both a research tool *and* a contribution engine (the co-pilot proposes → human reviews → promotes).

**Why this is powerful**
- Aligns with the "xAI / Grok era" moment.
- Creates a moat that pure catalog projects don't have.
- Directly serves the "AI + Human Symbiosis" vision in your architecture docs.
- Can become the feature that gets researchers to care.

**Trade-offs**
- Requires product + frontend + LLM integration work (you have high hours available, but this is different muscle from content waves).
- Risk of over-investing before you have an audience.

**Best sequenced after Path A has momentum.**

---

## My Strong Recommendation

**Lead with Path A (Launch & Visibility) for the next 90–120 days, while deliberately advancing Path B (Community Ownership) in parallel. Use Path C (AI Co-Pilot) as the exciting "Phase 1.5 / early Phase 2" bet once you have early external energy.**

**Rationale** (tailored to your answers):
- You have the capacity to drive a real launch right now.
- Uncertainty is your stated #1 pain — a focused launch gives you the clearest feedback and reduces optionality paralysis.
- You want to distribute ownership quickly — the best way to attract serious co-owners is to have something visible and citable first.
- All outcomes matter to you — launching is the highest-leverage single move that accelerates *all* of them.
- You already have INTERFACE.md and the automation engine. You don't need to invent the vision; you need to pick a vector and execute.

This is the classic "make the thing real in the world" step that almost every successful infrastructure project had to do after the prototype phase.

---

## Concrete 30 / 90 / 180-Day Plan (Launch + Ownership Focus)

### Next 30 Days — "Takeoff Sequence"
1. **Preprint** — Convert `docs/preprint/usdr_preprint.md` to proper PDF + submit to arXiv (cs.DL primary, cross-list q-bio, physics.soc-ph, etc.). You already have the materials.
2. **Domain** — Register a good custom domain and point GitHub Pages at it.
3. **Dashboard polish for launch** — Ensure the live site at the new domain feels like a real destination (hero messaging, clear "Start Contributing" path, recent activity).
4. **Activate existing assets** — Post 8–10 of your best "good first issue" tasks publicly with good context. Write one strong "How to make your first contribution in <30 minutes" guide.
5. **Outreach burst** — Use your existing Reddit/LinkedIn/Twitter thread materials. Send 15–20 targeted personal notes to researchers whose work already appears in the catalog or who work in bridge-heavy areas (percolation, criticality, complex systems, etc.).
6. **First ritual** — Schedule and run the first small "USDR Contribution Office Hours" (even 60–90 min Zoom).

**Success signal**: Preprint live + first external person actually opens a PR or claims an issue.

### 30–90 Days — "Flywheel Ignition"
- Run the first structured Contribution Sprint (2–4 weeks).
- Merge real external contributions and celebrate them loudly.
- Stand up a lightweight "USDR Stewards / Early Advisors" group (invite 5–8 people you respect).
- Ship the first version of the **Submission Portal** (INTERFACE.md P1.2) — this is the single highest-leverage feature for non-Git contributors.
- Begin light semantic search / embeddings work (or integrate an existing service) as a teaser for the AI co-pilot.
- Start documenting the "USDR Operating System" (how waves work, how reviews happen, how the graph is maintained) so others can help operate it.

### 90–180 Days — "Ownership Transition + Platform Bet"
- Formalize initial governance (advisory circle + clear decision rights).
- Run 2–3 domain-specific working groups.
- Decide on and begin the first real slice of the AI Co-Pilot (grounded chat over the graph + literature).
- Explore early funding conversations (now that you have a preprint + momentum + governance story).
- Evaluate: Are we seeing the flywheel? Do we need to double down on one path or adjust?

---

## How to Use Your Existing Strengths Ruthlessly

- **INTERFACE.md** is already an excellent product roadmap. Treat it as the technical execution plan once the launch vector is chosen.
- **Wave Factory + graph automation** is your unfair advantage for scale. Protect the human review gate while making promotion easier for trusted contributors.
- **Governance + ethics docs** are unusually mature — use them as a selling point when recruiting stewards and partners.
- The **dashboard** is your public face. Every major content or feature move should improve it.

---

## Immediate Next Actions I Can Help With (Pick Any)

1. Draft the actual arXiv submission package + cover letter.
2. Create a clean "Launch Playbook" checklist + timeline (with owners and dates).
3. Design the first version of the web Submission Portal (form → GitHub issue).
4. Write the initial "USDR Stewards" charter and invitation list / messaging.
5. Produce a 6-month governance + sustainability evolution plan (POSI-aligned).
6. Help you run a focused "Direction Decision" session (we can turn this document into a living plan).
7. Anything else that would remove uncertainty or create momentum.

---

**Bottom line**

You have built something rare and valuable. The complexity is real, but it is mostly *good* complexity (the kind that comes from having real substance).

The antidote to "uncertainty about the right direction" is **committed focus on one primary vector for a defined period**, while deliberately building the ownership distribution system in parallel.

Launch + early community ownership is the highest-leverage move available to you right now, given your capacity and openness.

You don't need to choose between visibility, community, AI, impact, or funding forever. You need to choose the sequence that makes the others possible.

I'm ready to help you execute whichever path (or hybrid) you decide on — at whatever depth you want (planning, writing, code, outreach materials, governance design, etc.).

Just tell me where you want to start.