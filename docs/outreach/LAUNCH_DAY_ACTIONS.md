# Launch day actions — human steps (June 2026)

Items that require your account credentials or registrar access. Estimated total time: **2–3 hours** spread across 2 days.

---

## 1. Pin Early Stewards discussion (5 min) — E2

1. Open [Discussion #286](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/discussions/286)
2. Click **Pin discussion** (owner-only; top-right or `...` menu)
3. Verify the pinned comment with correct stewards copy is visible (added 2026-06-21)

**Post short version on X/LinkedIn** — copy from [early_stewards_call.md](early_stewards_call.md) lines 76–88. Link to Discussion #286.

---

## 2. Register `usdr.science` (20–45 min + propagation) — E3

**Status:** Domain does not resolve yet (checked 2026-06-21).

1. Register at Namecheap, Cloudflare, or Google Domains (~$12–15/yr)
2. Add DNS per [CUSTOM_DOMAIN_SETUP.md](../CUSTOM_DOMAIN_SETUP.md):
   - CNAME `www` → `kr8zysho3.github.io`
   - A records `@` → GitHub Pages IPs (4 listed in doc)
3. GitHub → Settings → Pages → Custom domain: `usdr.science` → Enforce HTTPS
4. Wait 10–30 min; verify `https://usdr.science/dashboard/`

---

## 3. Submit preprint v1.2 (45–90 min) — E5

Follow [ARXIV_SUBMISSION_GUIDE.md](../preprint/ARXIV_SUBMISSION_GUIDE.md) and [SUBMISSION_CHECKLIST.md](../preprint/SUBMISSION_CHECKLIST.md).

- Primary: **cs.DL**
- Cross-lists: **q-bio.QM**, **physics.soc-ph**, **cs.IR**
- Upload PDF from `docs/preprint/usdr_preprint.md` (or existing `.html` → PDF)
- After acceptance: update README + dashboard with arXiv ID; announce using [twitter_threads.md](twitter_threads.md)

---

## 4. Fire outreach wave (30–60 min) — E6

**Day 1 order:**

| Step | Asset | Link |
|------|-------|------|
| Stewards short post | [early_stewards_call.md](early_stewards_call.md) | X + LinkedIn |
| Crosscheck story | [CROSSCHECK_LAUNCH_STORY.md](CROSSCHECK_LAUNCH_STORY.md) | Lead with this on Reddit/LinkedIn |
| Reddit flagship | [reddit post in calendar package](launch_posting_calendar.md) | r/OpenScience — **update counts** to 1124/1409/1275 |
| X thread | [twitter_threads.md](twitter_threads.md) | After Reddit |

**Lead narrative:** Crosscheck demo, not catalog size.

- [percolation explainer](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/explainers/b-habitat-percolation-ecology.html#crosscheck)
- [repro landing page](https://kr8zysho3.github.io/Universal-Science-Discovery/repro/p-b-habitat-percolation-ecology-fss/index.html) (fixed PR #291)
- **Copy-paste posts:** [READY_TO_POST.md](READY_TO_POST.md)

---

## 5. Personal outreach (ongoing) — E7

Send **5 DMs/emails** to authors cited in:

- `b-habitat-percolation-ecology`
- `b-ising-social-dynamics`
- `b-tipping-points-phase-transitions`

Template:

> Hi [Name] — I built USDR, an open git-native map of scientific unknowns and cross-domain bridges. Your work on [topic] is cited in our [bridge ID] entry. We just ran the first Crosscheck repro for the percolation↔ecology bridge (runnable script in-repo). Would you be open to a 10-min look, or claiming a 20-min launch-sprint issue? [link]

Track replies in a private sheet.

---

## Done when

- [x] Discussion #286 pinned + shared on LinkedIn (2026-06-22)
- [ ] `usdr.science` resolves with HTTPS
- [ ] arXiv preprint submitted (ID recorded in STATE.md)
- [x] At least one public post live (LinkedIn) with Crosscheck story
- [ ] Reddit r/OpenScience post (READY_TO_POST §3)
- [ ] LinkedIn §1b in-browser follow-up (optional)
- [ ] 5 personal outreach messages sent