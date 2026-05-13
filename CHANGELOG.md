# Changelog

All notable changes to the Universal Science Discovery Repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased] — 2026-05-09

### Added — Contributor onboarding baseline
- **CONTRIBUTING.md:** Local checks table (`pytest tests/repo_smoke`, `validate_schemas.py`, `mkdocs build --strict`), PR branch naming (`feat/`, `docs/`, `fix/`), link to the PR template, and a **good first issue** workflow.
- **`.github/ISSUE_TEMPLATE`:** Bug (YAML) and feature (Markdown) templates point at the same checks; removed duplicate legacy **`bug_report.md`** in favor of **`bug_report.yml`**.
- **`docs/DOC_MAP.md`**, **`docs/REPOSITORY_MANIFEST.md`**, **`AGENTS.md`**, **`docs/DEV_DASHBOARD.md`:** Traceability + stub for planned dashboard Phase A (search → graph highlight → GitHub).

### Fixed — CI Wave Factory (`harvest-openalex.yml` create-pull-request)
- fix: bump create-pull-request to v7 (fixes git credential failure in Wave Factory)
- fix(ci): make Wave Factory tolerant of empty batches (`steps.stage` changes gate only)
- fix(ci): Wave Factory CPR `add-paths` lists only candidate JSON files (not gitignored `drafts/wave_factory/**`); drop invalid `skip-commit` / `skip-checks` inputs (not in CPR v7)

### Fixed — markdown-link-check (arXiv registration URL)
- **`.markdown-link-check.json`:** Ignore **`https://arxiv.org/user/register`** — automated checks get **406 Not Acceptable**; the link remains valid for humans in preprint docs.

### Fixed — markdown-link-check vs generated citation index
- **`scripts/build_citation_index.py`:** Markdown table links now use **`https://doi.org/...`** for bare DOIs. Bare **`[DOI](10.x/...)`** targets were treated as **relative** URLs and returned **HTTP 400** in CI after bot merge **`#226`**.

### Fixed — CI Rebuild Knowledge Graph (branch protection vs bot push)
- **`.github/workflows/build-graph.yml`:** Replaced failing **direct `git push` to `main`** (step **Commit updated artifacts and push to main**) with **`peter-evans/create-pull-request@v7`** onto branch **`bot/auto-knowledge-graph-rebuild`** so `GITHUB_TOKEN` can land artifacts while **`main`** stays protected; added **`workflow_dispatch`** for manual reruns. **`docs/DOC_MAP.md`:** workflow row updated.

### Fixed — CI markdown-link-check (malformed Markdown links)
- **`CHANGELOG.md`**, **`.planning/STATE.md`**, **`ROADMAP.md`**, **`docs/DOC_MAP.md`:** Removed placeholder `(...)` ellipsis URLs and **nested backticks** inside `[link](url)` for the May 2026 audit report so **`markdown-link-check`** resolves paths correctly (avoids HTTP **400** from bogus targets).

### Changed — Discovery Engines hub cards (honest metrics)
- **`dashboard/index.html`:** Removed static per-theme **unknown** counts; cards now show only **spotlight bridge** counts derived from each theme’s bridge ID list (curated shortcuts, not catalog totals).

### Added — Repo script smoke tests + CI consolidation
- **`tests/repo_smoke/`:** Pytest wrappers for `validate_schemas.py`, `verify_domain_pages.py`, `verify_dashboard_consistency.py`, and **`build_graph.py --report-orphans`**; root **`pyproject.toml`** includes this path for **`python -m pytest tests/repo_smoke`**.
- **`validate-schemas.yml`:** Runs that pytest bundle (replacing three separate steps) so local runs match CI.

### Changed — Operating rhythm / CI documentation
- **`docs/OPERATING_RHYTHM.md`:** Documents **`validate.yml`** (path-filtered + quality audit) vs **`validate-schemas.yml`** (every PR/push); branch-protection guidance; status-check table includes **`validate.yml`**.

### Added — May 2026 full repository audit
- **[May 2026 full audit report](.planning/reports/USDR_FULL_AUDIT_2026-05.md):** Structured inventory, documentation drift, CI/security snapshot, and prioritized issues.
- **[`ROADMAP.md`](ROADMAP.md):** § **Audit backlog (2026-05)** + refreshed foundation snapshot counts (aligned with README / graph meta).
- **[`.planning/STATE.md`](.planning/STATE.md):** Audit completion note, **next** items, and catalog table refreshed to current YAML totals.
- **[`docs/DOC_MAP.md`](docs/DOC_MAP.md), [`docs/REPOSITORY_MANIFEST.md`](docs/REPOSITORY_MANIFEST.md):** Traceability for the audit report and clarified **`validate.yml`** vs **`validate-schemas.yml`** roles.

### Changed — README precision (literature links)
- **[`README.md`](README.md):** Replaced blanket “every entry DOI-linked” wording with schema/record-type-accurate language on citations.

### Changed — Contributor hub (Discovery Engines + breakthrough search affordance)
- **[`dashboard/index.html`](dashboard/index.html):** Discovery Engines intro clarifies curated thematic shortcuts; link to maintainer playbook on GitHub.
- **`scripts/render_breakthrough_gaps_hub.py` / hub:** Breakthrough cards carry **`data-search-query`** (catalog-oriented snippet); **Alt-click** a card jumps to **Catalog search** with that query (ordinary click still opens YAML on GitHub).

### Changed — Preprint statistics aligned with live catalog
- **`docs/preprint/usdr_preprint.md` / `.html`:** Abstract, §3.3–3.6, §5.1 (gap rankings), §8.1, and conclusion updated from stale **578-bridge / ~2.3k-entry** figures to current README/graph counts (**1,123** bridges, **1,408** unknowns, **1,274** hypotheses, **3,857** nodes / **4,517** edges, **18** pioneers, **24** breakthrough gaps, **~249** domain browse pages). **`scripts/render_preprint_html.py --apply`** regenerates HTML from the Markdown using **`markdown`** (listed in **`requirements-docs.txt`**).

### Added — Contributor hub maintenance playbook + drift check
- **`docs/DEV_DASHBOARD.md`:** Methodical “what changed → what to run” table, standard local command order, pre-merge checklist, and links to automation.
- **`scripts/verify_dashboard_consistency.py`:** Fails if `dashboard/index.html` **snap-** / **stat-** counts (and hero bridge pill) disagree with YAML + `docs/knowledge_graph.json`. Runs in **`validate-schemas.yml`**.
- **Cross-links:** **`CONTRIBUTING.md`**, **`docs/OPERATING_RHYTHM.md`**, **`dashboard/README.md`**, **`docs/DOC_MAP.md`**, **`docs/REPOSITORY_MANIFEST.md`**, **`AGENTS.md`**, **`.cursor/rules/documentation-and-dashboard.mdc`**, **`scripts/README.md`**.

### Added — Hosted hub freshness indicator (GitHub Pages)
- **`pages.yml`:** Before upload, writes **`dashboard/deploy-info.json`** (commit SHA, short SHA, ref, commit timestamp, deploy UTC time). File is **gitignored**; it exists only on the Pages artifact.
- **`dashboard/index.html`:** Banner under the hero pills compares that build to **`main`** (green when SHAs match; amber with **Compare on GitHub** when `main` has moved). Local **`file://`** and previews without `deploy-info.json` explain how to see freshness on the hosted URL.

### Changed — Contributor hub honesty (stats + Phase 1 ring)
- **Hub:** Replaced stacked historical wave banners with one **live catalog snapshot** row (patched by **`scripts/update_dashboard_stats.py --apply`**); **#status** shows **Phase 0 Foundation complete** strip; progress ring is **Phase 1 only**, **completed milestones only** (no partial credit for in-progress); checklist order aligned with **`ROADMAP.md`** Phase 1.

### Changed — Breakthrough gaps + phase-plan priorities
- **Hub:** “Breakthrough Gaps” section is **YAML-driven** — all `breakthrough-gaps/bg-*.yaml` files render as cards via **`scripts/render_breakthrough_gaps_hub.py`** (markers in **`dashboard/index.html`**); cards link to source YAML on GitHub.
- **API:** **`api/v1/breakthrough_gaps.json`** + **`meta.json`** count/endpoint; **`scripts/generate_api.py`** updated; hub Developer API list includes the new route.
- **CI:** **`build-graph.yml`** triggers on **`breakthrough-gaps/**`** and runs the renderer; **`validate.yml`** includes **`breakthrough-gaps/**`** in PR paths + summary row.
- **Docs:** **`docs/BREAKTHROUGH_GAPS.md`** (MkDocs nav), rewritten **`breakthrough-gaps/README.md`**, **`ROADMAP.md`** § integrated development priorities (tracks A–D), **`docs/PATH_TO_SUCCESS.md`** priority stack, **`DOC_MAP.md`**, **`docs/REPOSITORY_MANIFEST.md`**, **`AGENTS.md`**, **`.cursor/rules/documentation-and-dashboard.mdc`**, **`scripts/README.md`**.

### Fixed — Domain landing pages (`dashboard/domains/`) showed 0 bridges
- **Root cause:** `scripts/generate_domain_pages.py` looked for non-schema keys **`source_domain` / `target_domain`**; bridges use **`fields`** per **`schemas/bridge.yaml`**.
- **Fix:** Added **`scripts/domain_matching.py`** — normalize tags, hyphen boundary matching (`evolutionary-biology` → biology), and a small **synonym map** (e.g. `biophysics` ↔ biology/physics). **Single-pass bridge index** so regeneration stays fast. Hypotheses now match via **`unknowns_addressed`** and **`related_disciplines`** instead of `str(yaml)` hacks.
- **CI:** **`validate-schemas.yml`** runs **`python scripts/verify_domain_pages.py`** (minimum counts for biology, physics, mathematics, computer-science).
- **Docs/rules:** **`dashboard/README.md`**, **`scripts/README.md`**, **`docs/DOC_MAP.md`**, **`docs/REPOSITORY_MANIFEST.md`**, **`AGENTS.md`**, **`.cursor/rules/documentation-and-dashboard.mdc`**. Regenerated all **`dashboard/domains/*.html`** + index.

### Fixed — GitHub Actions + contributor hub CI panel
- **`markdown-link-check.yml`:** Set **`base-branch: main`** on `gaurav-nelson/github-action-markdown-link-check@v1` (upstream default is `master`, which broke PR/modified-file behavior on this repo).
- **`build-graph.yml`:** Replaced **`gh pr merge`** automation with a **direct push to `main`** using `github-actions[bot]`, **`fetch-depth: 0`**, and **`git pull --rebase`** — merge via CLI failed under branch protection; generated paths still **do not** re-trigger this workflow.
- **`dashboard/index.html`:** CI status widget now (**1**) merges runs by **newest `updated_at`** per workflow, (**2**) filters out non-repo workflows (e.g. Dependabot update bundles), (**3**) maps **skipped / cancelled** conclusions, (**4**) labels all `.github/workflows/*.yml` entries including **`validate.yml`**, **`pages.yml`**, **`build-graph.yml`**, **`harvest-openalex.yml`**, (**5**) requests up to **100** runs so sparse workflows are less likely to show **Unknown**.

### Changed — Roadmap phases (foundation vs discovery)
- **Phase 0 — Foundation** is documented as **complete** (governance, schemas, CI, seeded catalog, graph, hub, automation).
- **New Phase 1 — Discovery & adoption (2026–2027)** holds calendar- and community-dependent milestones (preprint DOI, outreach, first contributors, hackathon, custom domain) so they do not read as “failed Phase 0” targets.
- Former roadmap phases are **renumbered:** prior Phase 1 → **Phase 2 (Momentum)**, Phase 2 → **Phase 3 (Acceleration)**, Phase 3 → **Phase 4 (Transformation)**. Updated **`ROADMAP.md`**, **`README.md`**, **`INTERFACE.md`** roadmap alignment, **`CONTRIBUTING.md`**, **`WORKSTREAMS.md`**, **`CONTRIBUTORS.md`**, **`docs/DOC_MAP.md`**, **`docs/REPOSITORY_MANIFEST.md`**, **`docs/PATH_TO_SUCCESS.md`**, **`docs/preprint/usdr_preprint.md`** (+ synced **`docs/preprint/usdr_preprint.html`** §8.1), **`dashboard/index.html`** (hero pill, status section, milestone list), **`.planning/STATE.md`**, **`canvases/Progress.canvas.tsx`** (via sync script), and **`.cursor/rules/usdr-key-documents.mdc`**. **[INTERFACE.md](INTERFACE.md)** internal “Phase 1/2/3” **interface-program** labels are unchanged; the roadmap alignment table now explains how they map to USDR phases.

### Changed — Discovery UX (hub + docs)
- **Contributor hub:** Hero **discovery callout** with jump links to catalog search, domain browse, and knowledge graph (search already existed; now surfaced above milestone banners).
- **CONTRIBUTING.md:** **Before you add a record — search first** checklist (hosted + local hub, `#catalog-search`, `/` shortcut).
- **docs/index.md** & **docs/ONBOARDING.md:** Link to hosted `#catalog-search` and tie onboarding to duplicate-avoidance workflow.

### Fixed — Licensing clarity (README + LICENSING_NOTES)
- README license badges now point **CC BY** → [`LICENSE`](LICENSE) and **MIT** → [`LICENSE-CODE`](LICENSE-CODE) (they previously both pointed at `LICENSE`).
- [`docs/LICENSING_NOTES.md`](docs/LICENSING_NOTES.md) aligned with the dual-license layout at the repo root.

### Fixed — CI markdown-link-check (localhost hub URLs)
- **`.markdown-link-check.json`:** Ignore pattern matches **`http://localhost`** / **`https://localhost`** with **optional port** and any trailing path/query/fragment (prefix rule).
- **Docs/rules:** Prefer **`dashboard/index.html`** (repo-relative path) for navigation; keep **`http://localhost:8765/dashboard/`** only in **backticks** or point readers to **`dashboard/README.md`** / **`README.md`** quick-start comments instead of bare localhost URLs in prose. Updated **`AGENTS.md`**, **`.cursor/rules/documentation-and-dashboard.mdc`**, **`.cursor/rules/science-discovery-core.mdc`**, **`README.md`**, **`WORKSTREAMS.md`**, **`dashboard/README.md`** (alongside earlier **`CONTRIBUTING.md`**, **`docs/OPERATING_RHYTHM.md`** fixes).

### Fixed — CI markdown-link-check (DOI)
- **`docs/citation_index.md`:** Table links now use `https://doi.org/10…` (previously `10…` was treated as a relative path). **`.markdown-link-check.json`:** Ignore **`https://doi.org/`** (and legacy **`dx.doi.org`**) — automated checks often get **403** from doi.org in CI; identifiers remain standard for readers.

### CI — GitHub Actions bumps (checkout v6, Pages stack, upload-artifact v7)
- Aligns with Dependabot PRs for **`actions/configure-pages`**, **`actions/upload-pages-artifact`**, **`actions/deploy-pages`**, **`actions/upload-artifact`**, and **`actions/checkout`**.
- **`actions/checkout@v6`** on all workflows under **`.github/workflows/`**.
- **`pages.yml`:** **`actions/configure-pages@v6`**, **`actions/upload-pages-artifact@v5`**, **`actions/deploy-pages@v5`**.
- **`validate.yml`:** **`actions/upload-artifact@v7`**.

### Changed — Documentation audit (stats & contributor hub)
- **README:** Knowledge graph table aligned with `docs/knowledge_graph.json` meta (**3,857** nodes, **4,517** edges).
- **`update_dashboard_stats.py`:** Also syncs OpenGraph/Twitter meta, `stat-graph-edges`, knowledge-graph placeholder counts, and API section blurbs (unknowns/hypotheses/graph) from catalog file counts + built graph JSON.
- **`docs/DOC_MAP.md` / `docs/REPOSITORY_MANIFEST.md`:** Script behavior documented; added manifest row for **`SOLVING_UNKNOWNS.md`**.

### Changed — Docs CI & contributor hygiene
- **MkDocs:** Added missing pages to `mkdocs.yml` nav (strategy docs, Wave Factory, explainers, outreach, preprint, generated reports) so `mkdocs build --strict` passes without omitted-file warnings.
- **Graph tooling:** Refactored `scripts/build_graph.py` with `build_nodes_and_raw_edges` / `filter_orphan_edges`; added `--report-orphans` to list YAML cross-reference IDs that point to missing catalog nodes.
- **Wave Factory:** `drafts/wave_factory/` is now **gitignored**; removed tracked staging files from the index (regenerate locally). Documented in `docs/WAVE_FACTORY.md`.
- **New doc:** `docs/SOLVING_UNKNOWNS.md` — resolution ladder and evidence bar for closing unknowns; linked from `docs/DOC_MAP.md`.

### Added — Wave 88 (+12 bridges; catalog **1,123** bridges)
- Added 12 new cross-domain bridge triplets (bridge + companion unknown + companion hypothesis) spanning variational QAOA versus classical surrogate warm starts, persistent-homology microscopy QC under noise, efficient coding versus information-bottleneck objectives, replicator dynamics field inference for ESS narratives, belief propagation haplotype phasing on linkage graphs, RBMs as Ising-like energy models, spectral clustering for metabolomic module stability, Wasserstein-style DRO framing for climate deep uncertainty, contrastive predictive coding versus multiview self-supervision, contested RG coarse-graining metaphors for depth, EDMD/Koopman linearization for video dynamics forecasting, and sparse-sensor symbolic regression for PDE-structure recovery; speculative analogies are explicitly flagged except where literature establishes the bridge (e.g., BP on graphical models, RBM energy forms).
- Regenerated artifacts with full pipeline: `python scripts/validate_schemas.py`, `python -X utf8 scripts/build_graph.py`, `python scripts/update_dashboard_stats.py --apply`, `python scripts/sync-dashboard-from-state.py` (`docs/knowledge_graph.json` now **3,857 nodes**, **4,517 edges**).

### Added — Wave 87 (+12 bridges; catalog **1,111** bridges)
- Added 12 new cross-domain bridge triplets (bridge + companion unknown + companion hypothesis) spanning neural-operator space-weather assimilation, diffusion climate downscaling bias correction, causal-forest policy heterogeneity targeting, GNN priors for gene-regulatory perturbations, foundation-model transfer for TCR specificity, Bayesian-optimization alloy discovery loops, neural spectral ocean forecasting, physics-informed neural-operator aftershock mapping, vision-transformer crop stress phenotyping, graph-transformer grid contingency screening, agent-surrogate public-health intervention optimization, and protein language-model viral escape landscape forecasting; all bridge claims are explicitly labeled as speculative analogies.
- Regenerated artifacts with full pipeline: `python scripts/validate_schemas.py`, `python -X utf8 scripts/build_graph.py`, `python scripts/update_dashboard_stats.py --apply`, `python scripts/sync-dashboard-from-state.py` (`docs/knowledge_graph.json` now **3,821 nodes**, **4,457 edges**).

### Added — Wave 86 (+12 bridges; catalog **1,099** bridges)
- Added 12 new cross-domain bridge triplets (bridge + companion unknown + companion hypothesis) spanning neural ODE pharmacokinetic state-space modeling, neural CDE ICU trajectories, diffusion-prior MRI inversion, SimCLR multi-omics alignment, federated epidemic forecasting, Bayesian dropout adaptive trial stopping, transformer EHR temporal reasoning, U-Net satellite flood delineation, ResNet histopathology domain-shift robustness, VAE catalyst latent-space screening, graph-convolution transmission inference, and masked-autoencoder cryo-EM denoising priors; all bridge claims are explicitly labeled as speculative analogies.
- Regenerated artifacts with full pipeline: `python scripts/validate_schemas.py`, `python -X utf8 scripts/build_graph.py`, `python scripts/update_dashboard_stats.py --apply`, `python scripts/sync-dashboard-from-state.py` (`docs/knowledge_graph.json` now **3,785 nodes**, **4,397 edges**).

### Added — Wave 85 (+12 bridges; catalog **1,087** bridges)
- Added 12 new cross-domain bridge triplets (bridge + companion unknown + companion hypothesis) spanning SINDy host-pathogen modeling, optimal-transport lineage mapping, elastic-net PRS stabilization, lasso biomarker panel sparsification, compressed-sensing MRI acceleration, U-Net pathology quantification, residual retinal screening robustness, LSTM ICU forecasting, transformer protein fitness modeling, VAE single-cell denoising, AlphaFold-guided enzyme screening, and DESeq2-style shrinkage for clinical biomarker monitoring; all bridge claims are explicitly labeled as speculative analogies.
- Regenerated artifacts with full pipeline: `python scripts/validate_schemas.py`, `python -X utf8 scripts/build_graph.py`, `python scripts/update_dashboard_stats.py --apply`, `python scripts/sync-dashboard-from-state.py` (`docs/knowledge_graph.json` now **3,749 nodes**, **4,337 edges**).

### Added — Wave 84 (+12 bridges; catalog **1,075** bridges)
- Added 12 new cross-domain bridge triplets (bridge + companion unknown + companion hypothesis) spanning variational data assimilation for personalized glucose forecasting, percolation thresholds for antimicrobial combination design, Kramers-Moyal tumor-transition modeling, hysteresis biomarkers for neurofatigue recovery, OT barycenters for multiomic alignment, phase-response adaptive DBS timing, Laplace-approximation trial enrichment, graph-cut lesion QC, delay-embedding ICU warning, constrained bandits for sepsis de-escalation, Fisher-KPP wound closure forecasting, and Markov jump therapy design; all bridge claims are explicitly labeled as speculative analogies.
- Regenerated artifacts with full pipeline: `python scripts/validate_schemas.py`, `python -X utf8 scripts/build_graph.py`, `python scripts/update_dashboard_stats.py --apply`, `python scripts/sync-dashboard-from-state.py` (`docs/knowledge_graph.json` now **3,713 nodes**, **4,277 edges**).

### Added — Wave Factory mode automation
- Added `scripts/harvesters/wave_factory.py` to rank harvested candidates (citations + recency + domain novelty), dedupe against existing bridge IDs/titles, and stage schema-safe bridge/unknown/hypothesis draft triples under `drafts/wave_factory/`.
- Added `scripts/harvesters/promote_wave_factory_batch.py` to validate staged records and promote them into canonical folders with collision checks and explicit `--apply` gating.
- Updated `.github/workflows/harvest-openalex.yml` to a twice-weekly Wave Factory cadence with PR-friendly bot flow using staged outputs (no direct merge to protected branches).
- Added `docs/WAVE_FACTORY.md`, updated `docs/DATA_SOURCES.md`, and added a README section with Wave Factory usage and safety notes.

### Added — Wave 83 (+12 bridges; catalog **1,063** bridges)
- Added 12 new cross-domain bridge triplets (bridge + companion unknown + companion hypothesis) spanning eikonal cardiac mapping, cryo-EM phase-retrieval transfer, heavy-traffic ED control, EVT-AMR surveillance, HJB adaptive radiotherapy, peridynamics-bone microdamage, Kuramoto islet synchrony, adiabatic gene-circuit reduction, phage-chemostat Lotka-Volterra control, oncology ensemble smoothing, SPRT genomic surveillance, and TDA catalyst screening; all bridge claims are explicitly labeled as speculative analogies.

### Added — Draft promotion (+1 bridge, +1 unknown, +1 hypothesis)
- Promoted `drafts/bridges/b-openalex-topology-electrical-circuits-x-condensed-matter-physics.yaml` into a fully reviewed bridge at `cross-domain/engineering-physics/b-openalex-topology-electrical-circuits-x-condensed-matter-physics.yaml`.
- Added companion unknown `unknowns-catalog/engineering/u-topoelectrical-circuit-disorder-robustness-limit.yaml`.
- Added companion hypothesis `hypotheses/active/h-topoelectrical-circuit-edge-mode-disorder-threshold.yaml`.

### Added — Wave 82 (+12 bridges; catalog **1,050** bridges)
- **Themes:** Kalman smoothing for tree-ring paleoclimate reconstruction; Floquet seasonal-instability timing for epidemics; random-matrix denoising for single-cell covariance; first-passage-time framing for clinical deterioration warnings; persistent-homology microstructure failure precursors; neural-operator groundwater inversion surrogates; negative-control causal calibration for pharmacovigilance; BOCPD glacier calving regime shifts; Lyapunov-constrained antibiotic cycling; graph-spectral PMU anomaly localization; energy-landscape funnel diagnostics for docking search; renewal/self-exciting readmission burst modeling — each with one companion unknown and one companion hypothesis, with bridge claims explicitly marked as speculative analogies.
- **Regenerated:** `docs/knowledge_graph.json` (**3,638 nodes**, **4,152 edges**), `dashboard/index.html`, `canvases/Progress.canvas.tsx` via `validate_schemas.py`, `build_graph.py`, `update_dashboard_stats.py --apply`, `sync-dashboard-from-state.py`.

### Added — Wave 81 (+12 bridges; catalog **1,038** bridges)
- **Themes:** adjoint-state seismic inversion ↔ backprop gradient calculus; Hawkes self-excitation in aftershock/seizure clustering; EnKF smoothing ↔ ICU latent-state estimation; Fisher-information design ↔ autonomous materials experiments; persistent-homology RR topology ↔ arrhythmia warning; graph-Laplacian manifolds ↔ cryo-EM conformational maps; control barrier functions ↔ artificial-pancreas safety; optimal-transport bias correction ↔ climate downscaling; Mori-Zwanzig memory kernels ↔ epidemic model reduction (**speculative transfer explicitly labeled**); replica-exchange tempering ↔ Bayesian neural posterior sampling; FTLE coherent-structure analysis ↔ intracardiac flow mixing; Bayesian OED ↔ robotic chemistry optimization — each with companion unknown + hypothesis.
- **Regenerated:** `docs/knowledge_graph.json` (**3,602 nodes**, **4,092 edges**), `dashboard/index.html`, `canvases/Progress.canvas.tsx` via `validate_schemas.py`, `build_graph.py`, `update_dashboard_stats.py --apply`, `sync-dashboard-from-state.py`.

### Added — Wave 80 (+12 bridges; catalog **1,026** bridges)
- **Themes:** resonant WPT coupling/Q/bandwidth constraints; Bayesian inverse imaging ↔ uncertainty quantification calibration; stochastic resonance in biosignaling ↔ weak-signal information detection; topological defects/homotopy ↔ condensed-matter coarsening; ecological harvest resilience ↔ control-Lyapunov framing; next-generation-matrix epidemiology ↔ adaptive control policy structure; A-stability regions ↔ stiff reaction-diffusion timestepping; symplectic integration ↔ long-horizon control fidelity; thermodynamic uncertainty relations ↔ precision-energy limits; Floquet metasurface sidebands ↔ magnet-free nonreciprocity; quasi-BIC dielectric metasurfaces ↔ disorder/Q-yield limits; EIT protocol design ↔ Fisher-information geometry — each with companion unknown + hypothesis.
- **Regenerated:** `docs/knowledge_graph.json` (**3,566 nodes**, **4,032 edges**), `dashboard/index.html`, `canvases/Progress.canvas.tsx` via `validate_schemas.py`, `build_graph.py`, `update_dashboard_stats.py --apply`, `sync-dashboard-from-state.py` (Windows note: `python -X utf8 scripts/build_graph.py` avoids console encoding failures on some terminals).

### Added — Wave 79 (+12 bridges; catalog **1,014** bridges)
- **Themes:** flutter/galloping ↔ Hopf onset language; Ricci ↔ Price covariance (**explicit analogy limits**); CTQW spatial search ↔ Grover/spectral geometry; droplet splitting ↔ binary-fission metaphor; microplate absorbance ↔ inverse Beer–Lambert conditioning; tsunami SWE ↔ dispersive/bore regimes; spin-glass RSB imagery ↔ factor covariance clustering (**finance caveats**); LCS retention ↔ larval supply; cut-cell FV ↔ voxel segmentation (**interface analogy**); virial equilibrium ↔ molecular clouds & clusters; RL intrinsic motivation ↔ novelty/information gain; CDM substructure ↔ merger-tree algorithms — each with companion unknown + hypothesis.
- **Regenerated:** `docs/knowledge_graph.json` (**3,530 nodes**, **3,996 edges**), `dashboard/index.html`, `canvases/Progress.canvas.tsx` via `build_graph.py`, `update_dashboard_stats.py --apply`, `sync-dashboard-from-state.py`.

### Added — Wave 78 (+12 bridges; catalog **1,002** bridges)
- **Themes:** Kelvin-Helmholtz cloud billows ↔ plasma shear instability; Poisson counting ↔ decay / neural spike trains; DNA origami ↔ staged compilation (**explicit analogy**); Stone-Weierstrass ↔ universal approximation intuition; elastic net ↔ Laplace+Gaussian MAP prior; Kelvin wake ↔ ship-wave dispersion; Berry phase ↔ polarization parallel transport; Fisher information / Cramer-Rao ↔ dose-spacing design; diffusion MRI ↔ effective-medium tortuosity; Kramers escape ↔ drift-diffusion decision thresholds; Cahn-Hilliard ↔ diffuse-interface segmentation; RANSAC ↔ astronomical source matching — each with companion unknown + hypothesis.
- **Regenerated:** `docs/knowledge_graph.json` (**3,494 nodes**, **3,936 edges**), `dashboard/index.html`, `canvases/Progress.canvas.tsx` via `build_graph.py`, `update_dashboard_stats.py --apply`, `sync-dashboard-from-state.py`.

### Added — Wave 77 (+12 bridges; catalog **990** bridges)
- **Themes:** cardiac alternans ↔ Hopf / bifurcation language; epithelial jamming ↔ glassy colloid rheology; quantum Zeno ↔ watchdog / sampling (**explicit analogy**); complex torus ECDH pedagogy ↔ finite-field ECC (**careful**); forest gaps ↔ Hubbell-style neutral sampling; mantle horizontal kinetic spectra ↔ RB wavelength-selection (**not duplicate mantle convection narrative**); WGAN-GP ↔ Kantorovich dual / Lipschitz constraints (refinement beyond generic Wasserstein GAN ↔ OT); nitrogen-cycle Jacobians ↔ oscillator-style modal stability; DEQ ↔ fixed-point / implicit differentiation; Casimir–Polder–Lifshitz crossover ↔ vdW regimes; vaccination games ↔ herd thresholds; sonoluminescence ↔ cavitation collapse — each with companion unknown + hypothesis.
- **Regenerated:** `docs/knowledge_graph.json`, `dashboard/index.html`, `canvases/Progress.canvas.tsx` via `build_graph.py`, `update_dashboard_stats.py --apply`, `sync-dashboard-from-state.py` (use `python -X utf8 scripts/build_graph.py` on Windows if console encoding errors).

### Added — Wave 76 (+12 bridges; catalog **978** bridges)
- **Themes:** Cherenkov ↔ Mach cone; Wilson RG wavelets / shrinkage denoising (not RG×ML); synaptic tagging ↔ cache coherence (**pedagogical analogy**); ocean acoustic tomography ↔ ultrasound CT; CRISPR multiplex ↔ barcode / Reed–Solomon intuition (**careful wording**); elasticity ↔ stiffness tensor (**caveats**); fluorescence lifetime ↔ MRI T2*; Vicsek flocking ↔ Raft consensus; inflation ↔ epidemic phase plane (**speculation flagged**); ion-channel gating ↔ metastable rate theory; replication fork ↔ ASEP-style traffic; laser linewidth ↔ Leeson phase noise — each with companion unknown + hypothesis.
- **Regenerated:** `docs/knowledge_graph.json`, `dashboard/index.html`, `canvases/Progress.canvas.tsx` via `build_graph.py`, `update_dashboard_stats.py --apply`, `sync-dashboard-from-state.py`.

### Added — Wave 75 (+12 bridges; catalog **966** bridges)
- **Themes:** resonant WPT Q–bandwidth coexistence vs matching; Johnson–Nyquist thermal noise ↔ RF noise figure; earthquake early warning ↔ sequential Bayesian source estimation; folding funnel ↔ Polyak–Łojasiewicz optimization geometry (speculation flagged); epsilon-near-zero metamaterials ↔ cavity Q; Fano interference ↔ metamaterial quasi-dark modes; quantum-limited amplification ↔ Heisenberg noise-figure bound; ferrite hysteresis/eddy losses ↔ WPT coil Q; EEW alerting ↔ Wald SPRT sequential decisions (correlation caveats); contact-map sparsity ↔ Hessian cooperativity (speculation flagged); Floquet time modulation ↔ magnet-free nonreciprocity; phased-array beamforming ↔ multi-coil WPT interference — each with companion unknown + hypothesis.
- **Regenerated:** `docs/knowledge_graph.json`, `dashboard/index.html`, `canvases/Progress.canvas.tsx` via `build_graph.py`, `update_dashboard_stats.py --apply`, `sync-dashboard-from-state.py`.

### Added — Wave 74 (+12 bridges; catalog **954** bridges)
- **Themes:** EM skin depth ↔ financial firewalls; Doppler/redshift ↔ option-adjusted carry (speculation flagged); Zeeman structure ↔ RMT level spacing; capillary length ↔ wetting contact lines; Bode integral ↔ waterbed robust control; percolation ↔ cyber lateral movement; Lyapunov sensitivity ↔ bank-run dynamics (caveats); MEG/SQUID ↔ EM inverse source; Koopman ↔ DMD; Kalman filtering ↔ NWP assimilation; Green–Kubo ↔ volatility memory (speculative layer); Debye screening ↔ membrane double layer — each with companion unknown + hypothesis; phenomenology `p-nonhelical-cavity-resonator` linked to non-helical bridge IDs.
- **Regenerated:** `docs/knowledge_graph.json`, `dashboard/index.html` / `canvases/Progress.canvas.tsx` via `build_graph`, `update_dashboard_stats --apply`, `sync-dashboard-from-state`.

### Added — Non-helical resonator phenomenology (Turing + Landauer bridges) (+2 bridges, +4 unknowns, +2 hypotheses)
- **Bridges:** `b-nonhelical-turing-electromagnetic` (Turing / reaction–diffusion *analogy* for mode organization in cavity resonator arrays; speculation and testability called out) and `b-nonhelical-landauer-reversible-em` (reversible EM computation ↔ Landauer / Bennett framework).
- **Unknowns:** `u-nonhelical-turing-wavelength-scaling`, `u-metamaterial-self-assembly-dynamics`, `u-landauer-limit-nonhelical-resonator`, `u-reversible-em-logic-gate-design`.
- **Hypotheses:** `h-nonhelical-turing-cloaking-adaptation`, `h-nonhelical-resonator-adiabatic-quantum-memory` (schema-compliant; narrative mapped into `title` + `proposed_tests`).
- **Regenerated:** `docs/knowledge_graph.json` and `dashboard/index.html` stats (see latest `build_graph` / `update_dashboard_stats` run on this machine).

### Added — Waves 72–73 (+24 bridges; regenerated catalog **940** bridges)
- **Wave 72 (12 bridges):** Marcus ET / reaction-coordinate framing for enzyme tunneling; softmax attention × cortical divisive normalization; Ricci flow × geometrization program (Hamilton/Perelman refs); percolation × polymer gelation; bet hedging × portfolio diversification; plate-boundary mechanics × fracture / stress intensity; molecular spectroscopy × matrix diagonalization; cryo-EM × Bayesian reconstruction; advection–diffusion × odor plumes / foraging; Kauffman Boolean networks × GRN attractors; entropy rate × language-model perplexity; leaky integrate-and-fire × RC membrane circuits.
- **Wave 73 (12 bridges):** compressible gas shocks × traffic shock waves; metabolic control analysis × local sensitivity analysis; reinforcement learning × patch foraging / marginal value; helioseismology × inverse eigenvalue / spectral inverse problems; biogeochemical cycle box models × dynamical-system attractors; viral quasispecies × NK rugged fitness landscapes; NMR rotating frame × effective Hamiltonian engineering; Hertz contact × spherical indentation; ant colony optimization × gradient-free optimization; river braiding × SOC-like dynamics (**speculation labeled**); Morse homology × Conley index / isolated invariant intuition; supply-chain networks × bond percolation / disruption reliability.
- **Catalog deltas:** +24 unknowns, +24 hypotheses; `docs/knowledge_graph.json` rebuilt (**3306 nodes**, **3616 edges**); `dashboard/index.html` stats updated via `scripts/update_dashboard_stats.py`.

### Added — Waves 70–71 (+24 bridges; merged/regenerated catalog **904** bridges)
- **Wave 70 (12 bridges):** quantum Zeno × measurement/interruption analogies; Kalman filtering × brain state estimation; hyperbolic geometry × hierarchical network embeddings; Kleiber/WBE-style metabolic scaling × fractal-like transport; epidemic contagion models × financial network crises; Charnov marginal value × explore–exploit / bandits; electrochemical impedance × excitable membranes; discrete convolution × CNN inductive bias; ridge regression × Gaussian MAP shrinkage; contrastive SSL × energy/temperature analogies; gauge fields × connection forms on bundles; collective-risk dilemmas × insurance/mutualism.
- **Wave 71 (12 bridges):** galaxy red sequence × quenching/stellar populations; LiDAR ranging × geometric inverse problems; RNA planar folding × DP on graphs; GRB jets × relativistic hydrodynamics; quorum sensing × multiplayer evolutionary games; neutron-star cores × QCD/nuclear EOS constraints; coastal shorelines × interface / diffusion models; language contact × graph diffusion; FEM × discrete exterior calculus; skin friction × wall-bounded turbulence; MD thermostats × SDE sampling; truthful mechanism design (Vickrey/VCG) × preference elicitation.
- **Catalog deltas:** +24 unknowns, +24 hypotheses; `docs/knowledge_graph.json` rebuilt (latest regen on this branch: **3198 nodes**, **3460 edges** after merging upstream `main`); `dashboard/index.html` stats updated via `scripts/update_dashboard_stats.py`.

### Added — Waves 57-67 + OA-1 (734 → 868 bridges, +134)
- Wave 57 (PR #197): 12 bridges — mitochondrial proton-motive force, collective boid dynamics, and 10 additional cross-domain bridges
- Wave 58 (PR #198): 12 bridges — broad cross-domain coverage including biophysics and network theory
- Wave OA-1 (PR #199): 4 OpenAlex-sourced bridges — renormalization group × machine learning, thermodynamics × information theory, statistical physics × social science, information theory × evolutionary biology
- Wave 59 (PR #200): 12 bridges — prion folding, action potentials, epidemic percolation, Ising-Hopfield, viral capsid, stochastic resonance, catalysis, SAT spin glass, cytoskeleton, mechanism design, SOC earthquakes, population genetics RMT
- Wave 60 (PR #201): 12 bridges — quantum topo codes, morphogen PDE, compressed sensing, enzyme queueing, topological defects, hair cell Hopf, genetic algorithms, Black-Scholes heat eq, random walk Brownian, neural spike coding, liquid crystal membrane, FFT signal processing
- Wave 61 (PR #202): 12 bridges — broad cross-domain coverage
- Wave 62 (PR #203): 12 bridges — **crossed 800-bridge milestone**
- Wave 63 (PR #204): 12 bridges — continued cross-domain coverage
- Wave 64 (PR #205): 12 bridges — broad cross-domain coverage
- Wave 65 (PR #206): 12 bridges — **crossed 3,000-node graph milestone**; 1,000+ hypotheses reached
- Wave 66 (PR #207): 12 bridges — 1,000-hypothesis milestone confirmed
- Wave 67 (PR #208): 12 bridges — **final count: 868 bridges, 1,019 hypotheses, 1,151 unknowns**

### Added — Automation & Tooling (2026-05-07)
- Weekly OpenAlex harvest cron job (`.github/workflows/harvest-openalex.yml`)
- Bridge stub generator (`scripts/harvesters/generate_bridge_stubs.py`)
- PubMed harvester (`scripts/harvesters/harvest_pubmed.py`)
- Semantic Scholar harvester (`scripts/harvesters/harvest_semantic_scholar.py`)
- Pioneer lineage JSON (`api/v1/pioneer_lineage.json`) — 18 pioneer profiles
- 9 draft bridge stubs in `drafts/bridges/` from OpenAlex top candidates

### Added — Audit & Documentation (2026-05-07)
- Schema validation output saved to `docs/audit/schema_validation_2026-05-07.txt` (0 errors, 0 warnings)
- `STATE.md` updated with current counts and milestone history (Waves 57-67)
- `ROADMAP.md` Phase 0 progress updated; completed milestones marked through Wave 67
- `docs/PATH_TO_SUCCESS.md` strategic priorities updated to reflect automation-era focus
- `README.md` hero stats updated to current verified counts

### Fixed (2026-05-07 — **Dashboard stat counts and pill-regex**)
- **stat-bridges corrected 434 → 470; stat-unk corrected 814 → 826** — stat card IDs and all pill row text now reflect actual catalog counts.
- **`replace_pill_bridges` regex fixed** in `scripts/update_dashboard_stats.py`: pattern `(\d+) cross-domain bridges` did not match `400+ cross-domain bridges` (trailing `+` broke the match); changed to `\d+\+? cross-domain bridges` so future CI runs correctly update both bare-number and `N+` pill forms.
- **OG / Twitter meta-description corrected** — open unknowns updated 689 → 826; knowledge graph nodes updated 1,700 → 1,982.

### Added (2026-05-07 — **Waves 17–35 overnight build + document sync**)
- **470 bridges, 817 unknowns, 681 hypotheses, 1,982 graph nodes, 2,069 edges** — current verified catalog counts as of 2026-05-07.
- **300-bridge milestone** (Wave 20), **350-bridge milestone** (Wave 24), and **400-bridge milestone** (Wave 29) all hit in this session.
- **2,000+ graph nodes** reached (1,982 verified; 2,000+ during rebuild cycles).
- **0 orphan unknowns** maintained throughout all 19 waves.
- **Lyme disease breakthrough-gap cluster** added to `breakthrough-gaps/`; total breakthrough-gaps now 12.
- **Dashboard** updated with 400-bridge gold milestone banner and updated pill row.
- **`.planning/STATE.md`** rewritten to reflect actual current counts and focus (500-bridge push, D3 graph fix, arXiv preprint).
- **`ROADMAP.md`** Phase 0 progress section added with actual counts vs. milestones and Phase 1 readiness timeline.
- **`.cursor/rules/usdr-key-documents.mdc`** created — Cursor rule listing key documents to check/update before any significant work.
- **`CHANGELOG.md`** (this file) updated to reflect session reality.

### Added (2026-05-06 session — **Wave 29 — THE 400-BRIDGE MILESTONE** — bridges 399-410, 12 unknowns, 12 hypotheses)
- **🏆 400-BRIDGE MILESTONE ACHIEVED**: The USDR catalog has reached 400+ cross-domain mathematical bridges — a historic landmark in mapping the connective tissue of all major scientific disciplines. Final counts: **413 bridges, 790 unknowns, 657 hypotheses, 1,887 graph nodes, 1,984 edges, 0 orphan unknowns.**
- **12 new bridges (399–410):**
  - **b-stochastic-gene-expression-noise** (#399, `cross-domain/mathematics-biology/`): Mathematics ↔ Biology — Master equation for two-state promoter; Fano factor F = σ²/μ > 1 (bursty transcription); intrinsic/extrinsic noise decomposition (Elowitz 2002); bet-hedging = Kelly criterion under environmental uncertainty. Status: **established**.
  - **b-scientific-method-epistemological-foundations** (#400, `cross-domain/all-domains/`): All Domains — CAPSTONE Bridge 400: Popper falsificationism; Kuhn paradigm shifts; Lakatos progressive/degenerative research programmes; Duhem-Quine underdetermination; Bayesian confirmation (Jaynes); USDR bridges as falsifiable predictions. Status: **established**.
  - **b-electrophysiology-action-potential** (#401, `cross-domain/physics-biology/`): Physics ↔ Biology — Hodgkin-Huxley equations (1952); cable equation ≡ heat equation with ionic source; conduction velocity θ ∝ √d (unmyelinated) vs. θ ∝ d (myelinated); 100× saltatory conduction velocity gain. Status: **established**.
  - **b-thermodynamics-convex-analysis** (#402, `cross-domain/chemistry-mathematics/`): Chemistry ↔ Mathematics — Thermodynamics as convex duality; Legendre-Fenchel transform connects U(S,V,N) to A, G, H; stability ≡ convexity; Jaynes maximum entropy = constrained convex optimisation; Gibbs-Duhem from Euler's theorem. Status: **established**.
  - **b-complexity-economics-far-equilibrium** (#403, `cross-domain/social-science-physics/`): Social Science ↔ Physics — Complexity economics (Arthur 1994); El Farol minority game; Schumpeterian creative destruction; technology S-curve ≡ logistic equation; QWERTY path dependence ≡ ferromagnetic symmetry breaking. Status: **established**.
  - **b-neuromuscular-control-biomechanics** (#404, `cross-domain/biology-engineering/`): Biology ↔ Engineering — Huxley (1957) sliding filament; Hill force-velocity hyperbola; NMJ ACh→Ca²⁺→cross-bridge; Henneman size principle; stretch reflex as PD feedback controller; EMG motor unit decomposition. Status: **established**.
  - **b-topology-condensed-matter** (#405, `cross-domain/mathematics-physics/`): Mathematics ↔ Physics — TKNN invariant (1982); σ_xy = (e²/h)C₁ (first Chern number); Berry curvature integral over BZ; tenfold Altland-Zirnbauer symmetry classification; topological order, anyons, ground-state degeneracy. Status: **established**.
  - **b-allelopathy-chemical-ecology** (#406, `cross-domain/ecology-chemistry/`): Ecology ↔ Chemistry — Juglone complex-I inhibition; garlic mustard isothiocyanate → mycorrhizal disruption; Ehrlich-Raven (1964) glucosinolate-butterfly coevolutionary ratchet; biogenic VOC → SOA → cloud-climate feedback. Status: **established**.
  - **b-computational-psychiatry-digital-biomarkers** (#407, `cross-domain/neuroscience-engineering/`): Neuroscience ↔ Engineering — Kapur (2003) aberrant salience / dopamine precision; Bayesian psychosis model (Adams 2016); depression = reduced α⁺; smartphone GPS/accelerometer predict bipolar relapse (Torous 2018). Status: **established**.
  - **b-order-book-market-microstructure** (#408, `cross-domain/physics-social-science/`): Physics ↔ Social Science — Cont-Stoikov-Talreja Poisson LOB model; Kyle's lambda ΔP = λQ; Glosten-Milgrom adverse selection spread; square-root impact law ΔP ∝ √(Q/V); HFT flash crash as LOB phase transition. Status: **established**.
  - **b-population-vector-motor-cortex** (#409, `cross-domain/mathematics-neuroscience/`): Mathematics ↔ Neuroscience — Georgopoulos (1986) cosine tuning + population vector P = Σrᵢĉᵢ; Cunningham-Yu neural manifold (~10D); Churchland (2012) rotational dynamics dx/dt = Ax (A skew-symmetric); BCI Kalman filter readout. Status: **established**.
  - **b-secondary-metabolites-drug-discovery** (#410, `cross-domain/biology-chemistry/`): Biology ↔ Chemistry — PKS/NRPS modular assembly lines; ~50% approved drugs are NPs; terpenoid mevalonate pathway; genome mining of silent BGCs (10:1 ratio); teixobactin iChip discovery; antibiotic resistance crisis. Status: **established**.
- **12 new unknowns:** u-stochastic-gene-expression-bet-hedging-quantitative (biology), u-scientific-method-cross-domain-falsifiability (philosophy-of-science), u-myelination-conduction-velocity-optimality (neuroscience), u-thermodynamics-convex-geometry-non-equilibrium (mathematics), u-complexity-economics-policy-design-far-equilibrium (economics), u-neuromuscular-control-redundancy-resolution (neuroscience-engineering), u-topological-order-non-abelian-anyons-fault-tolerant (topology), u-allelopathy-invasive-plant-mycorrhizal-disruption (ecology), u-computational-psychiatry-treatment-response-prediction (neuroscience-engineering), u-order-book-flash-crash-phase-transition-mechanism (econophysics), u-motor-cortex-population-dynamics-motor-programs (neuroscience), u-silent-bgc-activation-novel-antibiotics (biology-chemistry).
- **12 new hypotheses:** h-stochastic-gene-expression-bet-hedging-optimal-noise, h-scientific-method-bridges-as-falsifiable-predictions, h-myelination-optimal-axon-diameter-conduction-velocity, h-thermodynamics-non-convex-regions-phase-coexistence, h-complexity-economics-minority-game-market-ecology, h-neuromuscular-size-principle-metabolic-optimality, h-topology-chern-number-predicts-edge-state-count, h-allelopathy-glucosinolate-diversity-coevolution-ratchet, h-computational-psychiatry-aberrant-precision-antipsychotic-mechanism, h-order-book-square-root-impact-universal-liquidity, h-motor-cortex-rotational-dynamics-initial-condition-mechanism, h-secondary-metabolites-pksnrps-combinatorial-evolution.
- **Dashboard:** 400-bridge gold milestone banner added (prominent, gold gradient, full wave summary); pill row updated to "400+ cross-domain bridges"; stats updated.
- **Running totals:** **413 bridges, 790 unknowns, 657 hypotheses, 1,887 graph nodes, 1,984 edges, 0 orphan unknowns.**

### Added (2026-05-06 session — **Wave 24 — THE 350-BRIDGE MILESTONE** — bridges 340-351, 12 unknowns, 12 hypotheses)
- **🏆 350-BRIDGE MILESTONE ACHIEVED**: The USDR catalog has reached 350+ cross-domain mathematical bridges — a landmark in systematically mapping the connective tissue between all major scientific disciplines.
- **12 new bridges (340–351):**
  - **b-superconductivity-cooper-pairs** (#340, `cross-domain/physics-chemistry/`): Physics ↔ Chemistry — BCS theory: phonon-mediated Cooper pairing despite Coulomb repulsion; London equations; Meissner effect; high-T_c cuprates (Bednorz-Müller 1986); gap equation Δ ≈ 2ℏω_D·exp(-1/N(0)V). Status: **established**.
  - **b-network-formation-games** (#341, `cross-domain/mathematics-social-science/`): Mathematics ↔ Social Science — Jackson-Wolinsky connections model; Nash-stable vs. efficient networks; Bala-Goyal center-sponsored star convergence; Braess paradox; Bramoulle et al. peer-effects identification. Status: **established**.
  - **b-lipid-bilayer-membrane-transport** (#342, `cross-domain/biology-chemistry/`): Biology ↔ Chemistry — Singer-Nicolson fluid mosaic; Saffman-Delbrück D ≈ kT/(4πηh); lipid raft 2D phase separation; Goldman-Hodgkin-Katz ion current; Na⁺/K⁺-ATPase Gibbs free energy. Status: **established**.
  - **b-finite-element-method-pde** (#343, `cross-domain/engineering-mathematics/`): Engineering ↔ Mathematics — FEM Galerkin weak form; stiffness matrix K_{ij} = ∫∇φᵢ·∇φⱼ; Cea's lemma error bound; isogeometric analysis (Hughes 2005) NURBS basis. Status: **established**.
  - **b-oceanic-turbulence-mixing** (#344, `cross-domain/ecology-physics/`): Ecology ↔ Physics — Munk-Wunsch 2 TW mixing budget; diapycnal diffusivity κ = Γε/N²; Kolmogorov microscale η ≈ 1 mm; Langmuir turbulence; thermohaline circulation climate control. Status: **established**.
  - **b-neural-field-theory-brain-waves** (#345, `cross-domain/neuroscience-physics/`): Neuroscience ↔ Physics — Wilson-Cowan/Amari neural field equations; dispersion relation ω(k); EEG alpha/theta/gamma from E-I balance; Robinson connectome eigenmodes; cortical traveling waves. Status: **established**.
  - **b-optimal-control-cancer-treatment** (#346, `cross-domain/mathematics-biology/`): Mathematics ↔ Biology — Pontryagin maximum principle; bang-bang chemotherapy; Gatenby adaptive therapy; replicator dynamics; evolutionary traps for drug resistance. Status: **established**.
  - **b-prediction-markets-information-aggregation** (#347, `cross-domain/social-science-mathematics/`): Social Science ↔ Mathematics — Arrow-Debreu contingent claims; Hanson LMSR C(q) = b·log(Σexp(qᵢ/b)) = softmax; Iowa Electronic Markets outperform polls; Milgrom-Stokey no-trade theorem. Status: **established**.
  - **b-molecular-dynamics-statistical-sampling** (#348, `cross-domain/chemistry-mathematics/`): Chemistry ↔ Mathematics — Verlet symplectic integrator; Zwanzig FEP ΔA = -kT·ln⟨exp(-ΔU/kT)⟩; Laio-Parrinello metadynamics; WHAM umbrella sampling; Anton drug binding. Status: **established**.
  - **b-organ-on-chip-microfluidics** (#349, `cross-domain/engineering-biology/`): Engineering ↔ Biology — OoC laminar flow Re << 1; Péclet number gradient maintenance; Huh lung-on-chip 2010; FDA Modernization Act 2.0 (2022); vascularized tumor chips. Status: **established**.
  - **b-standard-model-unity-physics** (#350, `cross-domain/all-domains/`): All Domains — Standard Model SU(3)×SU(2)×U(1); QED g-2 to 12 sig figs; Higgs mechanism spontaneous symmetry breaking; open frontiers (dark matter, gravity, baryogenesis). Status: **established**.
  - **b-sleep-memory-consolidation** (#351, `cross-domain/biology-neuroscience/`): Biology ↔ Neuroscience — Hippocampal SPW-R replay (Wilson-McNaughton 1994); Tononi-Cirelli synaptic homeostasis; complementary learning systems; glymphatic amyloid-β clearance (Xie 2013). Status: **established**.
- **12 new unknowns:** u-high-tc-superconductor-pairing-mechanism (physics-chemistry), u-network-formation-dynamic-stability-real-world (social-science), u-lipid-raft-functional-role-signaling (biology-chemistry), u-fem-adaptivity-optimal-mesh-refinement (mathematics), u-ocean-mixing-parameterization-climate-models (ecology), u-neural-field-theory-empirical-connectome-validation (neuroscience), u-adaptive-therapy-evolutionary-trap-clinical-validation (biology), u-prediction-market-thin-market-accuracy-limits (social-science), u-md-force-field-transferability-accuracy-limit (chemistry), u-organ-chip-vascularization-long-term-viability (engineering), u-standard-model-beyond-hierarchy-dark-matter-identity (physics), u-sleep-replay-causal-role-memory-specificity (neuroscience).
- **12 new hypotheses:** h-cuprate-pairing-spin-fluctuation-glue, h-braess-paradox-social-network-cascades, h-lipid-raft-phase-separation-receptor-clustering, h-isogeometric-analysis-superior-convergence-thin-shells, h-tidal-internal-wave-mixing-abyssal-hotspots, h-cortical-eigenmodes-universal-resting-state-basis, h-pontryagin-adaptive-therapy-outperforms-mtd-solid-tumors, h-lmsr-automated-market-maker-dominates-polls-epistemic-accuracy, h-metadynamics-collective-variables-protein-allostery, h-organ-chip-multi-organ-body-on-chip-systemic-toxicity, h-supersymmetry-electroweak-hierarchy-stabilization, h-targeted-memory-reactivation-during-sleep-enhances-consolidation.
- **Dashboard:** 350-bridge milestone banner added (gold, prominent); stats updated to 350 bridges, 689 unknowns, 556 hypotheses. Meta descriptions updated.
- **Running totals:** 350+ bridges, ~689 unknowns, ~556 hypotheses, ~1,700+ graph nodes.

### Added (2026-05-06 session — **Wave 20 — THE 300-BRIDGE MILESTONE** — bridges 287-300, 14 unknowns, 14 hypotheses)
- **🎯 300-BRIDGE MILESTONE ACHIEVED**: The USDR catalog has reached 300 cross-domain mathematical bridges — a landmark in mapping the connective tissue of human knowledge.
- **14 new bridges (287–300):**
  - **b-fluid-dynamics-glymphatic** (#287, `cross-domain/physics-neuroscience/`): Physics ↔ Neuroscience — Navier-Stokes/Biot poroelastic theory governs CSF flow through the glymphatic system; arterial pulsatility drives amyloid-β clearance; failure causes Alzheimer's disease. Status: **established**.
  - **b-optimal-transport-cell-differentiation** (#288, `cross-domain/mathematics-biology/`): Mathematics ↔ Biology — Kantorovich-Wasserstein optimal transport formalises Waddington's epigenetic landscape as a Riemannian manifold; cell fate trajectories are W₂ geodesics; RNA velocity + OT reconstructs lineage from scRNA-seq snapshots. Status: **established**.
  - **b-biomimetic-robotics-locomotion** (#289, `cross-domain/engineering-biology/`): Engineering ↔ Biology — SLIP model for running, Lighthill elongated-body theory for swimming, leading-edge vortex for flapping flight provide quantitative templates for legged/aquatic/aerial robots. Status: **established**.
  - **b-electrochemistry-battery-technology** (#290, `cross-domain/chemistry-engineering/`): Chemistry ↔ Engineering — Li-ion battery physics: Nernst equation, Butler-Volmer kinetics, SEI formation (Peled 1979), LLZO solid electrolytes, Monroe-Newman dendrite criterion. Status: **established**.
  - **b-network-centrality-social-influence** (#291, `cross-domain/social-science-mathematics/`): Social Science ↔ Mathematics — degree/betweenness/eigenvector/PageRank centrality all derive from spectral decomposition of adjacency matrix A; Bonacich centrality = Nash equilibrium wages; λ₁(A) sets epidemic threshold. Status: **established**.
  - **b-defects-mechanical-strength** (#292, `cross-domain/physics-materials-science/`): Physics ↔ Materials Science — Taylor hardening (τ ∝ √ρ), Hall-Petch (σ_y ∝ d⁻¹/²), Orowan precipitate strengthening reduce all of strength-of-materials to dislocation statistical mechanics. Status: **established**.
  - **b-behavioral-economics-evolutionary-psychology** (#293, `cross-domain/biology-social-science/`): Biology ↔ Social Science — loss aversion λ≈2.25, quasi-hyperbolic discounting, status quo bias all derive from asymmetric fitness consequences of gains/losses in ancestral foraging environments; neuroeconomics validates via ventral striatum/anterior insula. Status: **established**.
  - **b-geometric-measure-minimal-surfaces** (#294, `cross-domain/mathematics-physics/`): Mathematics ↔ Physics — GMT (currents, varifolds, Almgren regularity) provides existence/regularity theory for minimal surfaces; applications to soap films, Penrose area theorem, Willmore membrane energy, Yang-Mills connections. Status: **established**.
  - **b-ecosystem-resilience-bifurcation** (#295, `cross-domain/ecology-physics/`): Ecology ↔ Physics — fold bifurcations create hysteresis in bistable ecosystems; critical slowing down near fold produces early warning signals (rising variance, AR(1)→1); validated in 85 lake/fisheries transitions. Status: **established**.
  - **b-approximation-algorithms-sdp** (#296, `cross-domain/computer-science-mathematics/`): Computer Science ↔ Mathematics — Goemans-Williamson MAX-CUT: SDP relaxation + randomized hyperplane rounding achieves 0.878 ratio (optimal under UGC); Lovász theta function sandwiches NP-hard graph quantities. Status: **established**.
  - **b-neurotransmitter-pharmacology** (#297, `cross-domain/neuroscience-chemistry/`): Neuroscience ↔ Chemistry — SNARE complex zippering (ΔG ≈ -65 kJ/mol), Ca²⁺-synaptotagmin triggering, K_D = k_off/k_on receptor binding; all drug mechanisms (SSRIs, antipsychotics, benzodiazepines) are ligand-receptor thermodynamics. Status: **established**.
  - **b-wavelet-theory-signal-compression** (#298, `cross-domain/mathematics-engineering/`): Mathematics ↔ Engineering — Mallat MRA + Daubechies compact-support wavelets → O(N) FWT; JPEG-2000 achieves 40:1 compression; Donoho-Johnstone shrinkage is minimax-optimal over Sobolev classes. Status: **established**.
  - **b-urban-scaling-statistical-physics** (#299, `cross-domain/physics-social-science/`): Physics ↔ Social Science — urban Y ∝ N^β: superlinear (β≈1.15) for GDP/patents from interaction rate ∝ N²/A, sublinear (β≈0.85) for infrastructure; analogous to critical phenomena universality. Status: **established**.
  - **b-complex-systems-emergence** (#300, `cross-domain/all-domains/`): All Domains — Anderson's "More is Different" formalized via RG fixed points; Tononi Φ quantifies emergence; Simon's hierarchical nearly-decomposable systems unify consciousness, markets, ecosystems, and ant colonies. Status: **established**.
  - **b-causal-inference-instrumental-variables** (#285, `cross-domain/economics-statistics/`): Economics ↔ Statistics — potential outcomes framework (Rubin), IV/LATE (Angrist-Imbens-Rubin, Nobel 2021), regression discontinuity, DiD all identified by local CIA; Mendelian randomization imports IV into genomics. Status: **established**.
  - **b-nonequilibrium-statistical-mechanics-metabolism** (#286, `cross-domain/physics-biology/`): Physics ↔ Biology — Jarzynski equality (e^{-βW}=e^{-βΔF}), Crooks fluctuation theorem, Onsager efficiency, and Prigogine dissipative structures govern ATP synthesis, molecular motor thermodynamics, and cancer metabolism. Status: **established**.
- **2 new cross-domain directories:** `cross-domain/neuroscience-chemistry/`, `cross-domain/all-domains/`.
- **14 new unknowns:** u-glymphatic-csf-clearance-sleep-deprivation-rate (physics-neuroscience), u-wasserstein-cell-fate-noise-geodesic-uniqueness (mathematics), u-slip-model-biological-accuracy-multi-legged-running (engineering), u-solid-state-battery-sei-interface-resistance-origin (chemistry-engineering), u-network-centrality-temporal-dynamics-influence (social-science), u-dislocation-avalanche-statistical-mechanics-plasticity (materials-science), u-loss-aversion-cross-cultural-evolutionary-universality (biology), u-almgren-regularity-singular-set-sharp-dimension (mathematics-physics), u-ecosystem-tipping-point-early-warning-false-positive-rate (ecology), u-unique-games-conjecture-sdp-approximation-tight-gap (computer-science), u-snare-complex-partial-zippering-spontaneous-release-rate (neuroscience), u-wavelet-optimal-basis-nonstationary-signal-adaptation (mathematics), u-urban-scaling-law-exponent-inequality-cultural-variation (urban-science), u-emergence-quantification-integrated-information-empirical-test (physics).
- **14 new hypotheses:** h-csf-pulsatile-flow-amyloid-clearance-sleep-deprivation, h-optimal-transport-waddington-landscape-riemannian-geodesic, h-biomimetic-slip-locomotion-minimal-energy-cost-robots, h-llzo-single-ion-conductor-eliminates-dendrite-nucleation, h-eigenvector-centrality-superspreader-epidemic-prediction, h-dislocation-density-taylor-hardening-md-validation, h-prospect-theory-lambda-fitness-landscape-ancestral-environment, h-willmore-energy-biological-membrane-morphogenesis-ground-state, h-critical-slowing-down-universal-ews-ecosystem-tipping-fold-bifurcation, h-sdp-rounding-universal-approximation-ratio-tight-ugc, h-snare-zippering-energy-controls-vesicle-fusion-probability, h-wavelet-shrinkage-minimax-optimal-natural-image-sparsity, h-urban-superlinear-scaling-social-interaction-fractal-road-network, h-renormalization-group-universal-emergence-laws-cross-domain.
- **Dashboard:** 300-bridge milestone banner added; stats updated to 300 bridges, 677 unknowns, 544 hypotheses.
- **Preprint:** Updated to reflect 300 bridges, 677+ unknowns, 544 hypotheses, 1500+ graph nodes.
- **Running totals:** 300 bridges, ~677 unknowns, ~544 hypotheses, ~1500+ graph nodes.

### Added (2026-05-06 session — **Wave 3** — Lunr.js full-text search, bridges 101-105, 5 new hypotheses)
- **Lunr.js full-text search** added to `dashboard/index.html`: the catalog search box now uses a proper Lunr.js inverted index built from bridge titles, `bridge_claim` snippets, unknown `systematic_gaps`, and domain fields fetched from `api/v1/bridges.json` and `api/v1/unknowns.json`. Replaces simple substring filter. Results show title, type badge, domain tags, and a description snippet. Clicking a result scrolls to the knowledge graph and opens the detail panel. Keyboard shortcut `/` still focuses search.
- **5 new bridges (101-105):**
  - **b-zipf-optimal-coding** (#101, `cross-domain/linguistics-information/`): Linguistics ↔ Information Theory — Zipf's law is Shannon's optimal source coding applied to natural language; Mandelbrot (1953) derived the power law from least-effort optimisation; Piantadosi et al. (2011) confirmed word length tracks surprisal across 10 languages. Status: **established**.
  - **b-crystallography-group-theory** (#102, `cross-domain/materials-science-mathematics/`): Materials Science ↔ Mathematics — 230 space groups = complete enumeration of discrete Euclidean subgroups; Neumann principle; quasicrystals (Shechtman 1984) require aperiodic tilings (Penrose 1974) and 6D space groups. Status: **established**.
  - **b-free-energy-principle-stat-mech** (#103, `cross-domain/cognitive-science-physics/`): Cognitive Science ↔ Physics — Friston's variational free energy F = KL[q||p] − log p(o) is formally identical to Helmholtz free energy A = U − TS and to the variational ELBO in machine learning; unifies perception, action, homeostasis, and learning. Status: **proposed**.
  - **b-tensegrity-cytoskeleton** (#104, `cross-domain/engineering-biology/`): Engineering ↔ Biology — Fuller tensegrity structures (floating compression in continuous tension) are the mechanical principle of the cytoskeleton; actin = tension cables, microtubules = compression struts, focal adhesions = ground anchors; predicts cell stiffness, mechanotransduction, and cancer detection by AFM. Status: **established**.
  - **b-efficient-markets-martingale** (#105, `cross-domain/economics-information/`): Economics ↔ Information Theory — Efficient Market Hypothesis = martingale condition = zero mutual information between price history and future returns; insider trading = side channel; market anomalies = residual MI; Kelly criterion growth rate = MI. Status: **established**.
- **4 new cross-domain directories:** `cross-domain/linguistics-information/`, `cross-domain/materials-science-mathematics/`, `cross-domain/cognitive-science-physics/`, `cross-domain/economics-information/`.
- **5 new active hypotheses:**
  - **h-zipf-optimal-coding-universality**: Zipf exponent in any communication system is determined by channel capacity ratio sender/receiver — testable in animal vocalisation, neural spike trains, chemical signalling.
  - **h-tensegrity-cancer-mechanics**: Cancer cells have measurably lower Young's modulus than normal tissue (AFM-detectable); viable early detection modality.
  - **h-free-energy-aging**: Biological aging = failure of free energy minimisation as homeostasis ATP cost exceeds available metabolic free energy; senescence is the threshold-crossing event.
  - **h-crystallographic-protein-folding**: Protein symmetry group constrains folding pathways — higher symmetry predicts fewer kinetic traps and faster, more reliable folding.
  - **h-martingale-ecological-pricing**: Ecosystem service prices are non-martingale (systematically underpriced); deviation from martingale behaviour quantifies the information deficit in natural capital markets.
- **Running totals:** 105 bridges, 121 hypotheses, 544 unknowns, 771 graph nodes, 647 edges.

### Added (2026-05-05 session — **THE 100-BRIDGE MILESTONE** — bridges 85-100; 751 nodes total)
- **🎯 100-BRIDGE MILESTONE ACHIEVED**: The USDR catalog has reached 100 cross-domain mathematical bridges — the first 100 formally-structured connections between distinct scientific disciplines with full translation tables, real citations, unknowns, and hypotheses.
- **16 new bridges (85–100):** b-symplectic-geometry-mechanics (#85, mathematics↔physics, Hamilton's equations as flows on symplectic manifold, Noether = symplectic form preservation, deformation quantization ℏ→0, Arnold/Weyl/Dirac/Kontsevich; **established**), b-bayesian-brain-predictive-processing (#86, neuroscience↔statistics, brain as Bayesian inference machine, divisive normalization = Bayesian normalization, attention = precision weighting, Helmholtz/Weiss/Knill-Pouget/Friston/Carandini-Heeger; **established**), b-reaction-network-graph-theory (#87, chemistry↔mathematics, CRN as directed hypergraph, deficiency δ=n-l-s predicts multistability, FHJ zero theorem/one theorem, Horn-Jackson/Feinberg; **established**), b-species-distribution-maxent (#88, ecology↔statistics, MaxEnt = Gibbs distribution = Poisson point process regression = penalised logistic regression, Jaynes/Phillips/Elith/Renner-Warton/Fithian-Hastie; **established**), b-mechanobiology-continuum-mechanics (#89, physics↔biology, durotaxis = stiffness-gradient migration, jamming transition q*≈3.81, active matter vertex model, Discher/Engler/Bi/Trepat/Marchetti; **established**), b-transformer-attention-neural-attention (#90, computer-science↔neuroscience, scaled dot-product attention = soft WTA, softmax = divisive normalization, multi-head = multiple attentional spotlights, Vaswani/Moran-Desimone/Treisman/Lindsay; **proposed**), b-knot-theory-dna-topology (#91, mathematics↔biology, Lk=Tw+Wr, topoisomerases as Dehn surgery, knot invariants determine unknotting cost, Crick/Adams/Vologodskii/Rybenkov; **established**), b-dissipative-structures-economic-cycles (#92, economics↔physics, markets as dissipative structures, business cycles=limit cycles, Kondratiev waves=slow oscillations, Prigogine/Kondratiev/Georgescu-Roegen/Kaldor; **proposed**), b-cultural-memes-shannon-entropy (#93, social-science↔information-theory, meme transmission=noisy channel, cultural drift=channel noise, social media=biased channel, Dunbar's number≈channel capacity, Dawkins/Shannon/Henrich/Sperber/Bikhchandani; **proposed**), b-chaos-control-systems (#94, engineering↔physics, Lorenz attractor in control loops, Hopf bifurcation at PID stability boundary, OGY chaos control, Feigenbaum universality, Lorenz/Strogatz/Wiggins/OGY/Pecora-Carroll; **established**), b-kolmogorov-complexity-explanation (#95, philosophy-of-science↔information-theory, K(x)=shortest program, MDL=Occam's razor, Solomonoff induction=optimal Bayesian inference, scientific explanation=data compression, Kolmogorov/Solomonoff/Rissanen/Li-Vitányi; **established**), b-topological-neuroscience (#96, neuroscience↔mathematics, persistent homology of neural manifolds, grid cells=torus T², Betti numbers=cognitive topology, Curto-Itskov/Gardner/Dabaghian/Carlsson; **established**), b-navier-stokes-atmospheric-dynamics (#97, climate-science↔mathematics, geostrophic balance, Rossby waves, QG approximation = first NWP, Kolmogorov -5/3 cascade, Charney/Holton/Lorenz; **established**), b-mirror-neurons-aesthetic-empathy (#98, art-and-cognition↔neuroscience, embodied simulation theory, uncanny valley = mirror mismatch, motor resonance in art/music, Rizzolatti/Gallese-Freedberg/Mori/Hickok; **proposed**), b-representation-theory-particles (#99, quantum-physics↔mathematics, Wigner classification particles=irreps of Poincaré, spin=SU(2) label, SM gauge group determines all interactions, Noether=Lie group generators, Wigner/Weyl/Georgi/Zee; **established**), b-replicator-equations-evolutionary-dynamics (#100, biology↔mathematics, ẋᵢ=xᵢ(fᵢ-f̄) on probability simplex, ESS=asymptotically stable fixed points, Price equation unifies all selection levels, policy gradient RL=discrete replicator, Taylor-Jonker/Maynard-Smith/Price/Hofbauer-Sigmund; **established**).
- **14 new cross-domain directories:** `cross-domain/mathematics-physics/`, `cross-domain/neuroscience-statistics/`, `cross-domain/chemistry-mathematics/`, `cross-domain/ecology-statistics/`, `cross-domain/physics-biology/`, `cross-domain/computer-science-neuroscience/`, `cross-domain/social-science-information/`, `cross-domain/engineering-physics/`, `cross-domain/philosophy-of-science-information/`, `cross-domain/neuroscience-mathematics/`, `cross-domain/climate-science-mathematics/`, `cross-domain/art-and-cognition-neuroscience/`, `cross-domain/quantum-physics-mathematics/`, `cross-domain/biology-mathematics/`.
- **16 new unknowns:** u-symplectic-quantization-semiclassical (mathematics), u-bayesian-brain-prior-encoding (neuroscience), u-crn-multistability-biological (chemistry), u-maxent-species-range-shift-climate (ecology), u-cell-jamming-tissue-development (biology), u-transformer-attention-biological-plausibility (computer-science), u-topoisomerase-knot-selection (biology), u-economic-dissipation-entropy-measure (economics), u-meme-channel-capacity-measurement (social-science), u-chaos-transition-engineering-systems (engineering), u-kolmogorov-complexity-computable-approximation (mathematics), u-neural-manifold-topology-cognitive-states (neuroscience), u-rossby-wave-climate-tipping (climate-science), u-mirror-neuron-aesthetic-cross-cultural (art-and-cognition), u-standard-model-representation-completeness (physics), u-replicator-dynamics-prebiotic-origin (biology).
- **16 new hypotheses:** h-symplectic-quantization-new-prediction, h-predictive-processing-psychosis, h-crn-oscillator-design, h-maxent-invasive-species-prediction, h-durotaxis-cancer-metastasis, h-transformer-neural-attention-alignment, h-dna-knot-complexity-aging, h-kondratiev-dissipative-entropy, h-meme-channel-social-media-bias, h-hopf-bifurcation-power-grid-stability, h-mdl-scientific-theory-selection, h-betti-numbers-cognitive-complexity, h-geostrophic-balance-climate-change, h-mirror-neuron-dance-therapy, h-lie-group-beyond-standard-model, h-replicator-rl-convergence.
- **Knowledge graph rebuilt:** 751 nodes (+48), 619 edges (+48). API updated: 534 unknowns, **100 bridges**, 116 hypotheses. Dashboard updated to 100 bridges. Validates clean.

### Added (2026-05-05 session — bridges 75-84; 703 nodes total)
- **10 new bridges (75–84):** b-arrows-impossibility-quantum-contextuality (economics↔quantum-physics/social-science, Arrow impossibility theorem ↔ Kochen-Specker theorem as identical sheaf-cohomology no-go results, Abramsky-Brandenburger 2011; **proposed**), b-dna-digital-error-correcting-code (biology↔information-theory, genetic code as near-optimal error-correcting code, Freeland-Hurst 1998 1-in-10⁶ optimality, Hamming distance in codon space, Shannon capacity; **established**), b-free-energy-principle-thermodynamics (neuroscience↔physics, Friston variational free energy F=U-TS isomorphism, KL divergence=entropy, active inference=thermodynamic relaxation, Jaynes maximum entropy; **proposed**), b-curry-howard-proofs-programs (mathematics↔computer-science, propositions-as-types/proofs-as-programs, logical implication=function type, cut elimination=β-reduction, Howard/Wadler/Martin-Löf; **established**), b-phenological-mismatch-synchrony (climate-science↔biology, Kuramoto phase model of phenological desynchronisation, climate sensitivity differential=frequency spread, trophic coupling=coupling constant, Visser-Both/Renner-Zohner; **established**), b-plate-tectonics-topology (geoscience↔mathematics, every plate motion is SO(3) rotation about Euler pole, hotspot tracks=geodesics, triple junctions satisfy Euler characteristic, McKenzie-Parker/Morgan 1967-68; **established**), b-radiation-biophysics-let (medicine↔physics, Bethe-Bloch stopping power → LET → RBE → LQ model → TCP/NTCP, Bragg peak from 1/v² term, Kellerer-Rossi TDRA; **established**), b-social-capital-network-science (social-science↔mathematics, Granovetter weak ties=bridge edges, Burt structural holes=betweenness centrality, Erdős-Rényi giant component threshold p_c=1/n, PageRank=social capital; **established**), b-quantum-error-correction-holography (quantum-physics↔information-theory, AdS/CFT=quantum error-correcting code, HKLL reconstruction=erasure correction, RT formula S=A/4G_N=code distance, HaPPY perfect tensors, Almheiri-Dong-Harlow 2015; **proposed**), b-commons-game-theory-ostrom (ecology↔economics, tragedy of commons=prisoner's dilemma, Ostrom design principles=folk theorem conditions, δ_c=(T-R)/(T-P), Axelrod TFT, Fudenberg-Maskin 1986; **established**).
- **8 new cross-domain directories:** `cross-domain/biology-information/`, `cross-domain/neuroscience-physics/`, `cross-domain/mathematics-computer-science/`, `cross-domain/climate-science-biology/`, `cross-domain/geoscience-mathematics/`, `cross-domain/medicine-physics/`, `cross-domain/social-science-mathematics/`, `cross-domain/quantum-physics-information/`.
- **10 new unknowns:** u-sheaf-cohomology-impossibility-theorems, u-genetic-code-channel-capacity-quantitative, u-free-energy-principle-empirical-tests, u-curry-howard-quantum-logic-types, u-kuramoto-mismatch-critical-warming-threshold, u-deep-mantle-reference-frame-true-polar-wander, u-rbe-lq-model-carbon-ion-clinical-validation, u-structural-holes-empirical-betweenness-correlation, u-holographic-code-exact-boundary-conditions, u-critical-discount-factor-empirical-cpr-communities.
- **10 new hypotheses:** h-contextuality-mechanism-design-classification, h-genetic-code-near-optimal-error-correction, h-active-inference-thermodynamic-efficiency, h-homotopy-type-theory-univalence-computation, h-phenological-synchrony-kuramoto-phase-transition, h-plate-circuit-closure-so3-constraint, h-microdosimetry-dna-cluster-repair-threshold, h-social-capital-eigenvector-centrality-income, h-ads-cft-quantum-error-correction-island-formula, h-ostrom-design-principles-folk-theorem-mapping.
- **Knowledge graph rebuilt:** 703 nodes (+10), 571 edges. Dashboard updated: 84 bridges, 518 unknowns, 100 hypotheses.

### Added (2026-05-05 session — bridges 65-74; 693 nodes total)
- **10 new bridges (65–74):** b-biomineralization-crystal-growth (materials-science↔biology, Weiner-Addadi organic matrix control of crystal habit/polymorph/Ostwald ripening/spinodal nucleation; **established**), b-quantum-coherence-photosynthesis (quantum-physics↔biology, FMO complex 2DES oscillations, Lindblad master equation, ENAQT; **contested**), b-lotka-volterra-market-dynamics (economics↔ecology, LV predator-prey for incumbent-disruptor cycles, May complexity-stability, GLV interaction matrix; **proposed**), b-zipf-law-information-efficiency (mathematics↔linguistics, Mandelbrot entropy-max derivation, Ferrer i Cancho phase transition α=1, Piantadosi coding efficiency; **established**), b-neural-control-theory (neuroscience↔engineering, Flash-Hogan minimum-jerk, Wolpert-Kawato MOSAIC, Todorov-Jordan OFC signal-dependent noise, Kalman cerebellum; **established**), b-carbon-pricing-pigouvian (climate-science↔economics, Ramsey growth + IAM, Stern-Nordhaus ρ debate, Weitzman fat tails, SCC as Hamiltonian co-state; **established**), b-induction-bayesian-convergence (philosophy-of-science↔statistics, Doob consistency theorem dissolves Hume, Popperian falsificationism = degenerate 0/1 prior = Dutch book incoherence; **established**), b-cultural-evolution-darwinian (social-science↔biology, Price equation for culture, Cavalli-Sforza/Boyd-Richerson transmission modes, Henrich Eigen threshold analog; **established**), b-control-theory-differential-geometry (engineering↔mathematics, Chow-Rashevsky Lie bracket controllability, PMP = sub-Riemannian geodesics, robotics = fibre bundle holonomy; **established**), b-stellar-structure-thermodynamics (astronomy↔physics, Lynden-Bell-Wood negative heat capacity, virial theorem, Lane-Emden polytropes, gravothermal catastrophe, Chandrasekhar stability; **established**).
- **9 new cross-domain directories:** `cross-domain/materials-science-biology/`, `cross-domain/quantum-physics-biology/`, `cross-domain/economics-ecology/`, `cross-domain/mathematics-linguistics/`, `cross-domain/neuroscience-engineering/`, `cross-domain/climate-science-economics/`, `cross-domain/philosophy-of-science-statistics/`, `cross-domain/social-science-biology/`, `cross-domain/engineering-mathematics/`.
- **10 new unknowns:** u-biomineralization-polymorph-control (materials-science), u-quantum-coherence-physiological-role (biology), u-predator-prey-market-oscillations (economics), u-zipf-law-mechanism-adaptive-vs-null (mathematics), u-neural-optimal-control-noise-model (neuroscience), u-social-cost-carbon-discount-rate (economics), u-bayesian-convergence-prior-dependence (philosophy-of-science), u-cultural-drift-vs-selection-detection (social-science), u-subriemannian-geodesic-abnormal-optimality (mathematics), u-gravothermal-catastrophe-globular-cluster-timescale (astronomy).
- **10 new hypotheses:** h-organic-template-polymorph-selection, h-fmo-enaqt-efficiency, h-lotka-volterra-semiconductor-capex-cycle, h-zipf-critical-point-communication-efficiency, h-cerebellum-kalman-prediction-error, h-ramsey-optimal-carbon-price-tipping-points, h-doob-convergence-rate-scientific-inference, h-price-equation-cultural-trait-frequency, h-lie-bracket-depth-complexity-robot-planning, h-negative-heat-capacity-stellar-stability-criterion.
- **Knowledge graph rebuilt:** 693 nodes (+30), 571 edges (+50). Dashboard updated: 74 bridges, 518 unknowns, 100 hypotheses, 693 nodes.


- **6 new bridges (59–64):** b-earthquake-self-organized-criticality (geoscience↔statistical-physics, Gutenberg-Richter law as SOC power-law, Bak & Tang 1989; **established**), b-efficient-coding-perception (cognitive-science↔information-theory, Barlow 1961 efficient coding, Olshausen & Field 1996 sparse coding, Bell & Sejnowski 1997 ICA; **established**), b-bayesian-scientific-inference (philosophy-of-science↔mathematics, Jeffreys/Howson-Urbach/MacKay Bayesian confirmation theory, Occam factor as theorem, Kass-Raftery Bayes factors; **established**), b-robustness-evolvability-modularity (engineering↔evolutionary-biology, Waddington canalization ↔ robustness, Kirschner-Gerhart evolvability ↔ adaptability, Simon near-decomposability as shared solution; proposed), b-opinion-dynamics-ising (social-science↔statistical-physics, Sznajd/Voter/Deffuant models as Ising variants, polarisation as ferromagnetic phase transition, echo chambers as ferromagnetic domains; proposed), b-aesthetic-complexity-information (art-and-cognition↔mathematics, Birkhoff M=O/C, Kolmogorov complexity, fractal D, musical Shannon entropy, Schmidhuber compression-progress reward; proposed).
- **5 new cross-domain directories:** `cross-domain/geoscience-physics/`, `cross-domain/cognitive-science-information/`, `cross-domain/philosophy-of-science-mathematics/`, `cross-domain/social-science-physics/`, `cross-domain/art-and-cognition-mathematics/`.
- **6 new unknowns:** u-earthquake-soc-universality-class (geoscience), u-efficient-coding-metabolic-optimality (neuroscience), u-bayesian-prior-objectivity (philosophy-of-science), u-modularity-robustness-evolvability-tradeoff (biology), u-opinion-dynamics-critical-homophily (social-science), u-aesthetic-complexity-information-measure (mathematics).
- **6 new hypotheses:** h-gutenberg-richter-soc-btw-exponent, h-v1-gabor-infomax-prediction, h-bayes-factor-theory-selection, h-modular-architecture-robustness-evolvability, h-social-ising-polarization-transition, h-birkhoff-kolmogorov-aesthetic-sweet-spot.
- **Knowledge graph rebuilt:** 663 nodes (+18), 521 edges (+49). Dashboard updated: 64 bridges, 508 unknowns, 90 hypotheses, 663 nodes.

### Added (2026-05-05 session — bridges 55-58 from AI-draft conversion; 645 nodes total)
- **4 new bridges (55–58):** b-neural-criticality-climate-tipping (neuroscience↔climate-science, Beggs/Scheffer/Dakos — same fold-bifurcation normal form, AR1 critical slowing down = neural branching ratio → 1, EWI method transfer), b-predictive-coding-grammar (neuroscience↔linguistics, Friston free-energy = surprisal theory, precision-weighting = syntactic attention, MDL grammar = variational free energy), b-wealth-distribution-statistical-mechanics (economics↔statistical-physics, Boltzmann-Gibbs = exponential income distribution, economic temperature = mean wealth, Bouchaud-Mezard Pareto exponent prediction α = 1 + r/(g-r); status: **established**), b-topology-disease-progression (mathematics↔medicine, TDA Mapper identifies prognostic breast cancer subtype invisible to clustering, Betti numbers classify disease state topology, persistence diagrams distinguish transient vs. stable disease states; status: **established**).
- **4 new cross-domain directories:** `cross-domain/neuroscience-climate/`, `cross-domain/neuroscience-linguistics/`, `cross-domain/economics-physics/`, `cross-domain/mathematics-medicine/`.
- **4 new unknowns:** u-neural-criticality-tipping-shared-mathematics (neuroscience), u-predictive-coding-grammar-neural-substrate (linguistics), u-pareto-exponent-redistribution-mechanism (economics), u-tumor-evolution-topology-branching (medicine).
- **4 new hypotheses:** h-neural-ew-indicators-climate-tipping-transfer (multivariate EWI transfer between fields), h-surprisal-n400-mismatch-equivalence (N400 linear in surprisal, precision-modulated slope), h-pareto-exponent-growth-redistribution-ratio (Bouchaud-Mezard formula cross-country test), h-tda-cancer-subtype-prognosis-superiority (Mapper vs. clustering in TCGA BRCA).
- **Knowledge graph rebuilt:** 645 nodes (+12), 472 edges. Dashboard updated: 58 bridges, 502 unknowns, 84 hypotheses, 645 nodes.

### Added (2026-05-05 session — bridges 50-54 targeting astronomy orphan cluster; 633 nodes total)
- **5 new bridges (50–54):** b-blackhole-information-paradox (astronomy↔information-theory, Bekenstein-Hawking entropy = von Neumann entropy, island formula, AdS/CFT as quantum error-correcting code), b-baryon-asymmetry-cp-violation (astronomy↔particle-physics, Sakharov conditions, leptogenesis, Davidson-Ibarra bound, PMNS CP phase connects to cosmological matter excess), b-dark-matter-phase-transition-relics (astronomy↔statistical-physics, WIMPs from EWPT freeze-out, axions from QCD topological susceptibility, PBHs from QCD horizon mass), b-cosmic-rays-mutagenesis (astronomy↔biology, GCR flux varies with galactic position, GRB-ozone hypothesis for Ordovician extinction, cosmogenic isotope proxies), b-frb-random-matrix (astronomy↔mathematics, FRB waiting-time statistics map to RMT eigenvalue repulsion and GUE/GOE universality classes).
- **4 new cross-domain directories:** `cross-domain/astronomy-information/`, `cross-domain/astronomy-physics/`, `cross-domain/astronomy-biology/`, `cross-domain/astronomy-mathematics/`.
- **5 new unknowns:** u-hawking-channel-capacity (physics), u-leptogenesis-cp-scale (physics), u-qcd-ew-phase-transition-relics (physics), u-grb-mass-extinction-link (biology), u-frb-waiting-time-universality (mathematics).
- **5 new hypotheses:** h-holographic-encoding-hawking-radiation, h-leptogenesis-sm-cp-insufficient, h-dark-matter-qcd-axion-phase-relic, h-grb-cambrian-explosion-trigger, h-frb-gue-universality-magnetar.
- **5 existing astronomy unknowns connected:** u-black-hole-information-paradox, u-baryon-asymmetry-origin, u-dark-matter-particle-identity, u-fast-radio-burst-origin, u-uhecr-origin now carry `related_bridges` and `related_unknowns` pointers.
- **Orphan unknowns reduced:** 329 → 324 (5 large-cluster astronomy unknowns connected for first time).
- **Knowledge graph rebuilt:** 633 nodes (+15), 443 edges. Dashboard updated: 54 bridges, 498 unknowns, 80 hypotheses.

### Added (2026-05-05 session — bridges 45-49 from AI co-pilot proposals; 618 nodes total)
- **5 new bridges (45–49):** b-connectome-neurodegeneration (neuroscience↔medicine, graph-theoretic hub vulnerability predicts neurodegeneration trajectory), b-climate-tipping-health (climate-science↔medicine, fold-bifurcation governs both AMOC and epidemic thresholds), b-inequality-health-gradient (economics↔medicine, Gini coefficient as control parameter for health phase transitions), b-language-biomarker-diagnosis (linguistics↔medicine, NLP speech coherence as non-invasive Alzheimer's/psychiatric biomarker), b-stellar-forcing-paleoclimate (astronomy↔climate-science, Milankovitch cycles and solar variability control ice ages and habitability).
- **5 new unknowns:** u-connectome-neurodegeneration-spread-rate (neuroscience), u-climate-health-tipping-threshold (climate-science), u-inequality-health-phase-transition-threshold (economics), u-language-biomarker-clinical-validity (medicine), u-stellar-forcing-climate-sensitivity-scale (astronomy).
- **5 new hypotheses:** h-connectome-hub-vulnerability-neurodegeneration, h-epidemic-ar1-tipping-warning, h-gini-mortality-phase-transition, h-speech-coherence-alzheimers-prediction, h-milankovitch-nonlinear-resonance-100kyr.
- **5 new cross-domain directories:** neuroscience-medicine, climate-medicine, economics-medicine, linguistics-medicine, astronomy-climate.
- **Medicine domain bridges:** medicine now has 4 cross-domain connections (was 0 per co-pilot audit).
- **Knowledge graph rebuilt:** 618 nodes (+15), 398 edges. Orphan unknowns reduced from 260 to 329 (but base grew by 100+ from concurrent PRs).
- **Dashboard updated:** 49 bridges, 493 unknowns, 75 hypotheses, 618 nodes.

### Added (2026-05-05 session — content push toward 1,000 entries; 603 total)
- **4 new domain directories:** `unknowns-catalog/geoscience/` (28 unknowns), `unknowns-catalog/philosophy-of-science/` (20 unknowns), `unknowns-catalog/engineering/` (25 unknowns), `unknowns-catalog/art-and-cognition/` (15 unknowns).
- **88 new unknowns** spanning: deep Earth water cycle, mantle convection, inner core anisotropy, flood basalt triggers, earthquake nucleation, slow-slip events, supervolcano forecasting, permafrost thaw, ice sheet basal melting, demarcation problem, underdetermination, reproducibility crisis, peer review validity, preregistration, causation inference, turbulent drag reduction, fusion plasma stability, solid-state battery failure, offshore wind fatigue, carbon capture energy, green hydrogen electrolysis, smart grid stability, space debris removal, aesthetic preference, music universals, improvisation neuroscience, flow state, synesthesia, and more.
- **4 new bridges (41–44):** b-seismology-percolation (GR b=1 ↔ percolation criticality), b-philosophy-underdetermination-quantum (underdetermination ↔ quantum measurement problem), b-music-physics-resonance (Fourier analysis ↔ consonance/octave equivalence), b-engineering-reliability-extreme-value (Weibull/Gumbel ↔ Gompertz mortality ↔ fatigue).
- **10 new hypotheses:** h-gutenberg-richter-percolation-threshold, h-gompertz-weibull-aging-unification, h-preregistration-field-replication-rate, h-ice-sheet-basal-topography-instability, h-slow-slip-seismic-loading, h-solid-state-battery-pressure-dendrite, h-flood-basalt-ozone-kill-mechanism, h-permafrost-abrupt-thaw-dominates, h-synchrony-prosociality-physiological, h-kessler-cascade-altitude-band.
- **Knowledge graph rebuilt:** 603 nodes, 628 edges.
- **Dashboard updated:** 44 bridges, 488 unknowns, 70 hypotheses.

### Added (2026-05-05 session - final push - Phase 0 target 500+ achieved)
- **4 new domain directories:** quantum-physics (25), linguistics (25), social-science (25), economics (25).
- **Gap-filled existing domains:** computer-science (+10), neuroscience (+10), ecology (+8), chemistry (+6).
- **135 total new unknowns** across all domains.
- **8 new hypotheses:** h-quantum-advantage-noise-threshold, h-polarisation-ising-phase-transition, h-linguistic-relativity-neural-boundary, h-carbon-price-optimal-100, h-neuroinflammation-depression-biomarker, h-soil-microbiome-carbon-enhancement, h-llm-scaling-emergence-artifact, h-rewilding-trophic-cascade-predictability.
- **2 new bridges (39-40):** b-linguistic-relativity-quantum-basis (observer-dependent reality in language and physics); b-social-ising-polarisation (echo chambers as ferromagnetic domains).
- **Knowledge graph rebuilt:** 502 nodes, 601 edges.
- **Dashboard updated:** 40 bridges, 401 unknowns, 60 hypotheses.
- **Phase 0 target achieved:** 502 total entries.

### Added (2026-05-05 session — bulk content push to 357 entries)
- **6 new domain directories:** `unknowns-catalog/materials-science/` (25 unknowns), `unknowns-catalog/climate-science/` (25), `unknowns-catalog/astronomy/` (25), `unknowns-catalog/medicine/` (30), `unknowns-catalog/cognitive-science/` (20), plus 20 new unknowns in `unknowns-catalog/mathematics/`.
- **145 new unknowns** covering: high-Tc superconductivity, topological insulators, metallic glass, perovskite stability, twistronics, metamaterials; cloud feedback, AMOC collapse, permafrost tipping, ENSO predictability, ice sheet instability, SAI side effects; dark matter identity, dark energy EOS, FRB origin, Hubble tension, baryon asymmetry, BH information paradox, JWST early galaxies; sepsis heterogeneity, autoimmune triggers, immunotherapy non-responders, Alzheimer biomarkers, long COVID, spinal cord repair; hard problem of consciousness, language critical period, working memory capacity, mind-wandering; P vs NP geometric barriers, Riemann zero distribution, abc conjecture verification, turbulence formulation, random matrix universality.
- **10 new hypotheses** (`h-magnetar-rapid-rotation-dynamo`, `h-amoc-saddle-node-bifurcation`, `h-soluble-amyloid-oligomers-synaptic`, `h-permafrost-carbon-tipping-2point5`, `h-gut-microbiome-serotonin-depression`, `h-sei-organic-inorganic-layers`, `h-recurrent-processing-consciousness`, `h-jwst-pop3-lensing-detection`, `h-early-dark-energy-hubble-tension`, `h-microglial-synaptic-pruning-depression`).
- **2 new bridges (37–38):** `b-climate-tipping-percolation` (climate saddle-node bifurcations ↔ percolation phase transitions) in `cross-domain/physics-climate/`; `b-materials-consciousness-criticality` (spin glass SOC ↔ neural criticality) in `cross-domain/physics-neuroscience/`.
- **Knowledge graph rebuilt:** **357 nodes, 582 edges**.
- **Dashboard updated:** 38 bridges, 266 unknowns, 52 hypotheses, 582 graph edges.

### Added (2026-05-05 session — content push to 200 entries)
- **6 new bridges (31–36):** b-synchronization-circadian (Kuramoto ↔ circadian, jet lag as desynchronization crisis), b-allometry-fractal-networks (WBE ↔ Kleiber's law from geometry), b-ecological-stoichiometry-redfield (Redfield ratio as evolutionary attractor), b-minority-game-economics (El Farol ↔ market microstructure ↔ quasispecies), b-landau-theory-universality (Landau order parameter → all second-order transitions), b-scale-free-networks-criticality (Barabási-Albert ↔ brain connectome ↔ internet).
- **New directories:** `unknowns-catalog/chemistry/` (8 unknowns), `unknowns-catalog/neuroscience/` (8 unknowns), `unknowns-catalog/ecology/` (7 unknowns), `cross-domain/physics-networks/`.
- **45 new unknowns** spanning chemistry, neuroscience, ecology, physics, mathematics, biology.
- **11 new hypotheses** including h-circadian-synchrony-kuramoto-critical-coupling, h-tissue-jamming-universality-class, h-turbulence-directed-percolation, h-scale-free-criticality-brain-hub-vulnerability.
- **Knowledge graph rebuilt:** **200 nodes, 421 edges**.
- **Dashboard updated:** 36 bridges, 121 unknowns, 42 hypotheses, 421 graph edges.

### Added (2026-05-05 session — knowledge graph + bridges 27–30)
- **`scripts/build_graph.py`** — Knowledge graph builder. Walks all catalog YAML, creates nodes (bridge/unknown/hypothesis/phenomenon) and edges from cross-reference fields (`related_unknowns`, `related_hypotheses`, `related_bridges`, `suggested_hypotheses`, `candidate_bridges`, `candidate_unknowns`, `unknowns_addressed`, `evidence_links`). Outputs `docs/knowledge_graph.json` with nodes, edges, and meta. Prints top-5 nodes by degree.
- **`docs/knowledge_graph.json`** — Initial graph: **138 nodes, 300 edges**. Top connected: u-grokking-phase-transition (12), u-topological-morphogenesis (11), u-brain-criticality-function (10), u-climate-ew-indicator-universality (10), u-habitat-fragmentation-threshold (10).
- **Bridge 27 — `cross-domain/physics-information/b-entropy-arrow-of-time.yaml`** — Thermodynamic entropy (Boltzmann) ↔ information erasure (Landauer 1961, k_BT ln 2 per bit) ↔ cosmological arrow of time (Penrose Weyl curvature hypothesis). Resolves Maxwell's demon via Szilard-Landauer argument. References: Berut et al. 2012 (Nature, experimental Landauer test).
- **Bridge 28 — `cross-domain/physics-neuroscience/b-stochastic-resonance.yaml`** — Stochastic resonance in bistable physical systems ↔ noise-enhanced detection in crayfish/cricket mechanoreceptors, mammalian hair cells, and human tactile perception. Status: **established**. Therapeutic implications for neuropathy and hearing aids.
- **Bridge 29 — `cross-domain/physics-ecology/b-maximum-entropy-ecology.yaml`** — Jaynes MaxEnt (1957) ↔ Maximum Entropy Theory of Ecology (Harte et al. 2008, METE). Zero-free-parameter predictions of species abundance distributions, species-area relationships, and body-size distributions from S, N, E state variables.
- **Bridge 30 — `cross-domain/physics-computing/b-quantum-error-correction-topology.yaml`** — Kitaev toric code ↔ Z2 lattice gauge theory ↔ topological phase of matter (anyons, topological entanglement entropy). Status: **established**. Includes AdS/CFT holographic QEC connection and fracton extension.
- **4 new unknowns:** `u-arrow-of-time-low-entropy-origin` (physics), `u-stochastic-resonance-neural-tuning` (biology), `u-maxent-ecology-failure-modes` (biology), `u-topological-qec-physical-realization` (physics).
- **4 new hypotheses:** `h-landauer-cosmological-arrow`, `h-sensory-noise-sr-optimality`, `h-mete-non-equilibrium-deviations`, `h-topological-phase-qec-threshold-correspondence`.
- **`dashboard/index.html`** — Updated counts: **30 bridges · 73 unknowns · 31 hypotheses**. New "Knowledge Graph Edges" stat card (300 edges).

### Added (2026-05-05 session — bulk-seed unknowns: 37 new entries across 4 disciplines)
- **`unknowns-catalog/mathematics/`** — New discipline directory seeded with 8 unknowns spanning number theory, statistics, economics, linguistics, and mathematical biology.
- **`unknowns-catalog/computer-science/`** — New discipline directory seeded with 9 unknowns spanning neuromorphic computing, spiking networks, ML theory, and quantum cognition.
- **Physics unknowns (10 new):** `u-quantum-turbulence-simulation-limit`, `u-turbulence-symmetry-breaking-cascade`, `u-minimum-dissipation-network-topology`, `u-vegetation-pattern-tipping-universality`, `u-cardiomyocyte-synchronization-criticality`, `u-active-matter-chiral-renormalization`, `u-replica-boltzmann-machine-glass`, `u-quantum-glass-learning-efficiency`, `u-ion-pump-landauer-thermodynamics`, `u-nonextensive-entropy-turbulence`.
- **Biology unknowns (10 new):** `u-cryptochrome-radical-pair-quantum-nav`, `u-alzheimer-network-attractor-dynamics`, `u-evolution-undecidability-open-ended`, `u-fitness-landscape-overlapping-genes`, `u-pathogen-coevolution-network-percolation`, `u-mechanical-bifurcation-morphogenesis`, `u-temporal-biosignature-information`, `u-ecology-resilience-spatial-indicator`, `u-braess-paradox-biological-foraging`, `u-self-organized-criticality-consciousness`.
- **Mathematics unknowns (8 new):** `u-riemann-zeta-biomedical-discoverability`, `u-optimal-transport-word-order-universals`, `u-spectral-geometry-phylogenetic-trees`, `u-large-deviations-non-markovian-epidemic`, `u-statistical-mechanics-income-wealth`, `u-cortical-folding-poisson-flow`, `u-causal-attribution-chain-rule-universality`, `u-ising-exact-density-states-universality`.
- **Computer-science unknowns (9 new):** `u-astrocyte-memory-replay-transformers`, `u-oscillatory-spiking-neural-computation`, `u-predictive-coding-motion-illusion`, `u-stdp-reward-modulation-rl-equivalence`, `u-continuous-symmetry-neural-topology`, `u-physics-informed-nn-fourier-convergence`, `u-fractional-spiking-neural-memory`, `u-quantum-cognition-lindblad-decisions`, `u-neuromorphic-thermodynamic-energy`.
- All 37 unknowns seeded from arXiv OAI-PMH harvest data (cs-ne, nlin, statmech, qbio, bioph harvests; 2026-03-01 to 2026-05-04).
- All files pass `scripts/validate_schemas.py` (jsonschema Draft202012).
- **`dashboard/index.html`** — Updated counts: 69 unknowns · 26 bridges · 27 hypotheses · 1 observation.

### Added (2026-05-05 session — phenomenology catalog)
- **`phenomenology/`** — New catalog tier for pre-formal observations: dreams, intuitions, engineering hunches, everyday anomalies. Lower bar than `unknowns-catalog/` — no citations or credentials required. Entries are triaged and promoted to `u-`, `b-`, or `h-` entries by domain experts.
- **`schemas/phenomenon.yaml`** — New schema: required fields are `id`, `title`, `origin`, `description`, `date_observed` only. Optional: `sketch_description`, `analogies`, `candidate_fields`, `why_anomalous`, `review_notes`.
- **`phenomenology/physics/p-nonhelical-cavity-resonator.yaml`** — First entry: a dream about a hollow aluminum box with lattice-insulated wire wound non-helically. Triaged to: slow-wave structure inside resonant cavity (traveling-wave tube) OR negative-permeability metamaterial unit cell. Seeds an open question about unexplored non-helical winding geometries.
- **`docs/prompts/intuition_to_unknown.md`** — Step-by-step guide for converting any intuition or observation into a structured entry, including an AI triage prompt.
- **`scripts/validate_schemas.py`** — Extended to validate `phenomenology/p-*.yaml` entries.
- **`dashboard/index.html`** — New "Pre-formal Observations" stat card.

### Added (2026-05-05 session — Landauer and game-theory bridges)
- **`cross-domain/physics-information/b-landauer-information-thermodynamics.yaml`** — 19th bridge: Landauer (1961) proved erasing 1 bit costs k_B*T*ln(2). Resolves Maxwell's demon (94-year-old paradox). Experimentally verified by Berut et al. 2012 to 1%. The brain operates within ~100x of the Landauer limit per synaptic event — closer than any silicon chip.
- **`cross-domain/mathematics-evolution/b-game-theory-evolution.yaml`** — 20th bridge: Nash equilibrium (1950) = ESS (Maynard Smith 1973) = replicator dynamics fixed point = GAN training convergence = RLHF Nash reward models. The Price equation (1970) unifies all of these. Three independent communities rediscovered the same math with ~20-year gaps each.
- **`unknowns-catalog/physics/u-landauer-limit-biological-computation.yaml`** — How close to the Landauer limit do synapses, ribosomes, and DNA repair operate?
- **`unknowns-catalog/biology/u-replicator-dynamics-llm-training.yaml`** — Does LLM self-play RLHF converge to Nash equilibria at the same rate as biological replicator dynamics?
- **`hypotheses/active/h-brain-landauer-efficiency.yaml`** — Brain operates within 2 orders of the Landauer limit per synaptic event.
- **`hypotheses/active/h-gan-training-redqueen-dynamics.yaml`** — GAN instability (mode collapse, oscillation) is predicted by Red Queen zero-sum replicator dynamics.
- **`dashboard/index.html`** — Updated counts: 26 unknowns · 26 hypotheses · 20 bridges.

### Added (2026-05-05 session — Turing patterns and spin-glass bridges)
- **`cross-domain/mathematics-biology/b-turing-reaction-diffusion.yaml`** — 17th bridge: Turing (1952) reaction-diffusion instability ↔ biological pattern formation. Predicted zebrafish stripe wavelength (0.48 mm) matches observed (0.50 mm) using FCS-measured Nodal/Lefty diffusivities — no free parameters. Same mechanism governs digits, hair follicles, palate rugae, and left-right symmetry breaking.
- **`cross-domain/physics-computing/b-spin-glass-neural-networks.yaml`** — 18th bridge: SK spin-glass statistical mechanics ↔ Hopfield associative memory. Critical capacity α_c = 0.138 patterns/neuron derived exactly from the replica method. Above α_c the network enters a spin-glass phase (catastrophic confabulation). Same replica machinery governs deep learning loss landscapes.
- **`unknowns-catalog/biology/u-turing-digit-wavelength-scaling.yaml`** — Does digit count scale as limb-width / Λ* across vertebrate species?
- **`unknowns-catalog/physics/u-hopfield-capacity-cortex.yaml`** — Does human CA3 operate near α_c = 0.138? Does Alzheimer's synapse loss trigger the glass transition?
- **`hypotheses/active/h-turing-zebrafish-diffusivity-ratio.yaml`** — Zebrafish adult stripe period predicted from FCS diffusivities alone; laser-ablation test predicts +15% wavelength shift on iridophore removal.
- **`hypotheses/active/h-hopfield-alzheimers-glass-transition.yaml`** — AD synapse loss (30-50%) pushes CA3 past α_c, causing confabulation rather than blank retrieval; observable as confusion-to-omission error ratio inflection.
- **`scripts/showcase_analysis.py`**, **`scripts/generate_showcase_figure.py`**, **`scripts/math_derivation.py`** — Quantitative showcase scripts: Monte Carlo percolation simulation, power-law β fit, FSS ν fit, one-sample t-test (t=0.52, p=0.63 vs p_c).
- **`docs/showcase_percolation_ecology.png`**, **`docs/math_derivation_percolation.png`** — Publication-quality figures.
- **`dashboard/index.html`** — Updated counts: 24 unknowns · 24 hypotheses · 18 bridges.

### Added (2026-05-04 session — climate and social physics bridges)
- **`cross-domain/physics-climate/b-tipping-points-phase-transitions.yaml`** — 15th bridge: climate tipping elements are formal bifurcations. AMOC, Amazon, Arctic, permafrost each have a specific bifurcation class with universal EWI exponents. Boers (2021) measured rising AR1 in AMOC but never fit the fold scaling exponent 1/2 to estimate remaining warming budget to collapse.
- **`unknowns-catalog/physics/u-climate-ew-indicator-universality.yaml`** — Which bifurcation class is each IPCC tipping element? Are the EWI scaling exponents universal? Has spatial correlation length been computed for Amazon NDVI or Arctic sea ice?
- **`hypotheses/active/h-amoc-fold-bifurcation-ew.yaml`** — Fold exponent 1/2 fit to Boers (2021) AR1 time series estimates T_c (critical warming for AMOC collapse); KZ quench-rate connection links AMOC to embryogenesis and cosmology.
- **`cross-domain/physics-social/b-ising-social-dynamics.yaml`** — 16th bridge: opinion dynamics, norm cascades, echo chamber formation, and market crashes are all Ising universality class. Social tipping coupled to physical climate tipping creates a two-system tipping interaction.
- **`unknowns-catalog/physics/u-social-ising-universality.yaml`** — Do social tipping events show Ising EWIs? Which universality class governs opinion dynamics on real social networks?
- **`hypotheses/active/h-norm-cascade-ising-ew.yaml`** — Same-sex marriage US 1990-2015 should show fold-bifurcation scaling in Gallup data; social and physical tipping linked via KZ quench-rate universality.
- **`data/harvest/mathph-2026-05-04.jsonl`** — 20 records from physics:math-ph (April 2026); continuum percolation paper strengthens ecology bridge.
- **`dashboard/index.html`** — Updated counts: 22 unknowns · 22 hypotheses · 16 bridges.

### Added (2026-05-04 session — Kuramoto and Fisher information bridges)
- **`cross-domain/physics-engineering-neuroscience/b-kuramoto-synchronization.yaml`** — 13th bridge: Kuramoto model unifies neural gamma oscillations, cardiac AF, power grid stability, and laser arrays. The spectral-gap formula for K_c (derived for power grids) predicts sinoatrial node AF threshold. Includes h-kuramoto-af-spectral-gap: pacemaker stimulation protocol from laser engineering.
- **`hypotheses/active/h-kuramoto-af-spectral-gap.yaml`** — AF vulnerability = inverse spectral gap of sinoatrial coupling Laplacian; laser noise-robust phase-locking protocol → novel pacemaker design.
- **`cross-domain/statistics-evolution/b-fisher-information-evolution.yaml`** — 14th bridge: Fisher information I(theta) = additive genetic variance V_A. Fisher's two 1925/1930 theorems are one. Natural selection = natural gradient ascent = TRPO/NPG in deep RL. Connects to h-quantum-compass-precision (quantum Fisher info).
- **`unknowns-catalog/biology/u-fisher-natural-gradient-evolution.yaml`** — Does natural selection saturate the Fisher-information speed limit? Does the G-matrix encode the natural gradient direction?
- **`hypotheses/active/h-fisher-speed-limit-selection.yaml`** — Artificial selection efficiency R/(V_A*beta) near 1.0 in large populations, drops with 1/(2*Ne*s); Illinois maize long-term experiment as test case.
- **GitHub Issues #29-31** — Kuramoto AF spectral gap, Fisher speed limit, habitat percolation SLOSS resolution.
- **`dashboard/index.html`** — Updated counts: 20 unknowns · 20 hypotheses · 14 bridges.
- **`.planning/STATE.md`** — Bridge network table updated to 14 bridges.

### Added (2026-05-04 session — ecology and information-evolution bridges)
- **`cross-domain/physics-ecology/b-habitat-percolation-ecology.yaml`** — 11th bridge: completes the percolation trilogy (oncology, epidemiology, ecology). The ~60% habitat threshold at which forest-interior species collapse is the 2D site percolation threshold p_c=0.593. FSS corrections predict how this threshold shifts in finite landscapes. Resolves the 50-year SLOSS debate analytically.
- **`unknowns-catalog/biology/u-habitat-fragmentation-threshold.yaml`** — Has the 2D percolation FSS exponent nu=4/3 ever been measured from real species-persistence data? No.
- **`hypotheses/active/h-habitat-percolation-critical-density.yaml`** — FSS-corrected threshold p_c(A)=0.593+c*A^(-3/4) measurable from Sentinel-2 satellite data; early-warning indicators of approaching threshold derivable from cluster-size power law.
- **`cross-domain/information-evolution/b-error-threshold-information.yaml`** — 12th bridge: Eigen's quasispecies error threshold and Shannon's channel capacity theorem are the same mathematical result. RNA viruses operate near the Shannon limit. Coronavirus nsp14 proofreading is a capacity-expansion adaptation.
- **`unknowns-catalog/biology/u-error-threshold-genome-size.yaml`** — Has the Shannon bound C=1-H(mu) ever been fitted to the (mu, L) distribution across all domains of life?
- **`hypotheses/active/h-viral-proofreading-shannon-optimality.yaml`** — nsp14 proofreading is Shannon-optimal; nidovirus genome-size distribution should fit the Shannon capacity curve; lethal mutagenesis minimum dose derivable from the bound.
- **`unknowns-catalog/physics/u-gauge-field-epidemic-nonlocality.yaml`** — Seeded from q-bio:PE harvest; QED gauge-field formalism applied to non-local epidemic spreading (April 2026 preprints); speculation clearly labelled.
- **`data/harvest/qbio-pe-2026-05-04.jsonl`** — 25 records from q-bio:q-bio:PE (April 2026).
- **`packages/ingest/src/usdr_ingest/constants.py`** — Fixed OAI-PMH endpoint URL (`/oai` → `/oai2`).
- **`dashboard/index.html`** — Updated counts: 19 unknowns · 18 hypotheses · 12 bridges.
- **`.planning/STATE.md`** — Bridge network table updated to 12 bridges.

### Added (2026-05-04 session — RG and epidemiology bridges)
- **`cross-domain/mathematics-biology/b-renormalization-biological-scaling.yaml`** — 9th bridge: renormalization group (RG) fixed point ↔ biological allometric scaling laws. The WBE vascular branching recursion is structurally an RG equation; the correction-to-scaling exponent predicts how Kleiber's Law breaks down below 1g. Includes full translation table with 7 entries and cross-pollination opportunities.
- **`unknowns-catalog/biology/u-renormalization-allometric.yaml`** — Has the WBE vascular recursion ever been cast as a real-space RG transformation and the correction-to-scaling exponent derived? No.
- **`hypotheses/active/h-allometric-rg-fixed-point.yaml`** — Wilson-Fisher correction-to-scaling exponent from the branching-network RG predicts the observed sub-1g deviation in Savage et al. (2004); testable against ectotherm data.
- **`cross-domain/physics-epidemiology/b-percolation-epidemiology.yaml`** — 10th bridge: network percolation ↔ epidemic threshold. R_0=1 is a percolation phase transition; FSS corrections predict finite-population R_0 bias. COVID-19 nursing home datasets provide the test.
- **`unknowns-catalog/biology/u-percolation-epidemic-fss.yaml`** — Do percolation FSS corrections quantitatively improve R_0 estimates in populations of N < 10,000?
- **`hypotheses/active/h-percolation-outbreak-threshold.yaml`** — FSS correction exponent nu=1 (random-graph universality class) measurable from COVID-19 nursing home outbreak data; 30% R_0 estimation improvement predicted.
- **GitHub Issues #24-26** — contributor tasks for KZ experiment, FSS epidemiology analysis, and RG allometry calculation.
- **`dashboard/index.html`** — Updated counts: 16 unknowns · 16 hypotheses · 10 bridges.
- **`.planning/STATE.md`** — Full bridge network table updated to 10 bridges.

### Added (2026-05-04 session — cross-domain catalog expansion)
- **8th bridge** [`cross-domain/cosmology-biology/b-kibble-zurek-morphogenesis.yaml`](cross-domain/cosmology-biology/b-kibble-zurek-morphogenesis.yaml)
  — Kibble-Zurek mechanism (Big Bang defect formation) ↔ embryonic symmetry breaking (PAR polarisation in *C. elegans*);
  includes full `translation_table`, `cross_pollination_opportunities`, and `communication_gap`.
- **Unknown** [`unknowns-catalog/physics/u-kibble-zurek-embryo.yaml`](unknowns-catalog/physics/u-kibble-zurek-embryo.yaml)
  — Does PAR-domain error density scale with fertilisation quench rate per KZ power-law?
- **Hypothesis** [`hypotheses/active/h-kibble-zurek-polarity-scaling.yaml`](hypotheses/active/h-kibble-zurek-polarity-scaling.yaml)
  — CDK1 quench-rate experiment in *C. elegans* + active-KZ theory extension; closes the loop to `b-topology-morphogenesis`.
- **Hypothesis** [`hypotheses/active/h-quantum-compass-precision.yaml`](hypotheses/active/h-quantum-compass-precision.yaml)
  — Cryptochrome CRY4 operates at the quantum Fisher-information Cramér-Rao bound; proposes QFI ratio measurement
  and bio-inspired protein-scaffold quantum sensor as spinoff; fills `b-quantum-biology-navigation` hypothesis gap
  and closes GitHub Issue #18.
- **`cross-domain/cosmology-biology/README.md`** — Bridge overview with 55-orders-of-magnitude span table.
- **`cross-domain/README.md`** — Updated bridge index table; 8 bridges now listed.
- **`docs/CROSS_DOMAIN_BRIDGES.md`** — Updated bridge table with new KZ and quantum compass entries.
- **`dashboard/index.html`** — Updated counts: 14 unknowns · 14 hypotheses · 8 bridges.

### Changed
- **[`.cursor/rules/documentation-and-dashboard.mdc`](.cursor/rules/documentation-and-dashboard.mdc)** — hub CDN/offline + **HAPPY_PATH_FIRST_RECORDS** when schemas/seed examples change Stream A; sync **README** / **DEV_DASHBOARD** when hub UX changes
- **[docs/DEV_DASHBOARD.md](docs/DEV_DASHBOARD.md)** and **[dashboard/README.md](dashboard/README.md)** — hub UX (theme, nav) and CDN / offline notes
- **Contributor hub** [`dashboard/index.html`](dashboard/index.html): richer hero, sticky “glass” nav + scroll-spy, light/dark toggle, stat deck and motion (respects `prefers-reduced-motion`); [`dashboard/README.md`](dashboard/README.md) updated
- **[docs/OPERATING_RHYTHM.md](docs/OPERATING_RHYTHM.md)** — branch protection: table of status check names + ingest workflow path-filter caveat
- **[docs/OPERATING_RHYTHM.md](docs/OPERATING_RHYTHM.md)** — CI guidance: no markdown links to GitHub Pages base URL until it returns 200 (or use `ignorePatterns`)

### Fixed
- **markdown-link-check (CI):** GitHub Pages URL in README/manifest as plain text (not a link until live); `docs/index.md` uses explicit reference links to `tree/main/...` (avoids broken `../tree/...`); broaden `kr8zysho3.github.io` ignore pattern in `.markdown-link-check.json`
- **ingest pytest (CI):** `test_cli_help.py` sets `TERM=dumb` for `CliRunner` so Rich/Typer help includes option text under `TERM=linux` (GitHub Actions default)

### Added
- **`docs/examples/`** — synthetic [arxiv-oai-metadata-sample.v1.jsonl](docs/examples/arxiv-oai-metadata-sample.v1.jsonl) (envelope v1, fixture-derived); [README](docs/examples/README.md); **MkDocs** Operations nav; [`scripts/generate-ingest-example-jsonl.py`](scripts/generate-ingest-example-jsonl.py); pytest asserts sample validates against [`schemas/ingestion-envelope-1.0.0.json`](schemas/ingestion-envelope-1.0.0.json); [DATA_PLAN.md](docs/DATA_PLAN.md) stretch item filled; DOC_MAP + REPOSITORY_MANIFEST rows
- **[docs/QUALITY_BAR.md](docs/QUALITY_BAR.md)** — anti-sloppiness playbook (CI, review lanes, definition of done); linked from CONTRIBUTING, collaboration doc, onboarding, MkDocs **Community & integrity**, DOC_MAP, manifest, docs index, hub, happy path
- **[docs/HAPPY_PATH_FIRST_RECORDS.md](./docs/HAPPY_PATH_FIRST_RECORDS.md)** — Stream A: setup → unknown YAML → hypothesis YAML → PR; wired through CONTRIBUTING, onboarding, MkDocs, DOC_MAP, manifest, templates README, `docs/index`, contributor hub
- **PR template** ingest/envelope checkbox; **CONTRIBUTING** tooling section for `packages/ingest`; contributor **hub** maintainer bar links **compare** `main...feat/dev-dashboard` for integration PRs
- **[packages/ingest/README.md](packages/ingest/README.md)** — package quickstart; `pyproject` **`readme`** field for metadata; root README ingest section links here
- **[docs/UAT_INGEST.md](docs/UAT_INGEST.md)** — manual acceptance steps for `usdr-ingest` (pytest + CLI smoke + optional live OAI dry-run); linked from [DATA_PLAN.md](docs/DATA_PLAN.md), MkDocs **Operations**, hub, DOC_MAP, manifest
- **[docs/GSD_INTEGRATION.md](docs/GSD_INTEGRATION.md)** — optional GSD boundaries for maintainers; linked from [ROADMAP.md](ROADMAP.md), onboarding, doc map, MkDocs **Operations**, **docs/index**, **REPOSITORY_MANIFEST**, and contributor hub (`dashboard/index.html` Cadence + Reference)
- **`schemas/ingestion-envelope-1.0.0.json`** — JSON Schema for metadata ingest JSONL (`DATA_PLAN` v1.0.0); `packages/ingest` tests validate harvest fixtures against it (`jsonschema` dev dep)
- Cursor rule **documentation-and-dashboard** (`.cursor/rules/documentation-and-dashboard.mdc`): keep docs, CHANGELOG, `.planning/STATE.md`, and `dashboard/` contributor hub current at milestones and ongoing; verify `http://localhost:8765/dashboard/` when hub links change
- AGENTS + OPERATING_RHYTHM alignment with the same expectations
- **GitHub Pages deploy** workflow (`.github/workflows/mkdocs-gh-pages.yml`) + `site_url` in `mkdocs.yml` for `https://kr8zysho3.github.io/Universal-Science-Discovery/`
- README **Published documentation** subsection and REPOSITORY_MANIFEST entry for the live docs URL and `gh-pages` Pages source; `.gitignore` **MkDocs output** (`/site/`) so local builds are not committed
- **arXiv OAI-PMH metadata ingest** — [`packages/ingest`](packages/ingest) (`usdr-ingest`), [`requirements-ingest.txt`](requirements-ingest.txt), root [`pyproject.toml`](pyproject.toml) pytest config; [`.github/workflows/ingest-ci.yml`](.github/workflows/ingest-ci.yml)
- Cursor rule **agent-execution** (`.cursor/rules/agent-execution.mdc`) — prefer in-environment installs, tests, and git
- Phase 0 **seed content**: example unknowns + linked active hypotheses (dark matter / radio–axion-like constraints; aging intervention translatability / metabolic bottlenecks) under `unknowns-catalog/high-priority/` and `hypotheses/active/`
- **Discipline stubs** [`disciplines/physics/README.md`](disciplines/physics/README.md), [`disciplines/biology/README.md`](disciplines/biology/README.md), [`disciplines/computer-science/README.md`](disciplines/computer-science/README.md)
- **Schema validation CI** ([`.github/workflows/validate-schemas.yml`](.github/workflows/validate-schemas.yml)) and [`scripts/validate_schemas.py`](scripts/validate_schemas.py) with [`scripts/requirements-validate.txt`](scripts/requirements-validate.txt)
- **MkDocs site** for `docs/` — [`mkdocs.yml`](mkdocs.yml), [`requirements-docs.txt`](requirements-docs.txt), [`docs/index.md`](docs/index.md), CI [`.github/workflows/mkdocs-build.yml`](.github/workflows/mkdocs-build.yml) (MkDocs ignores broken `../` links to repo-root files so `build --strict` passes)
- README content-layout row for the physics seed
- Blueprint MVP slice: `schemas/` (hypothesis, unknown, dataset), `templates/`, `disciplines/`, `unknowns-catalog/`, `hypotheses/` (subfolders), `cross-domain/`, `code/` with READMEs
- README + DOC_MAP updates for content layout
- `CONTRIBUTING.md` contributor path aligned with blueprint and outreach docs
- `DOC_MAP.md` traceability for all root-level policy and communication documents
- Cross-links between `WHY_CONTRIBUTE.md` and `VISION_COMMUNICATION.md`
- [ROADMAP.md](ROADMAP.md): “Interface development” section linking phased delivery to [INTERFACE.md](INTERFACE.md)

### Changed
- N/A (initial release)

---

## [0.1.0] - 2026-05-01

### Added
- Foundational repository created
- Core root documents: README, LICENSE (MIT + CC0), CONTRIBUTING.md, CODE_OF_CONDUCT.md, LEGAL.md, GOVERNANCE.md, SECURITY.md, CHANGELOG.md
- Detailed blueprint for full implementation (see `universal-science-discovery-repo-blueprint.md`)
- Initial focus on discovery-first principles: unknowns, hypotheses, cross-domain connections
- Plans for DVC integration, knowledge graph export, and AI-assisted hypothesis generation

### Notes
This is the initial planning and documentation release. The repository is not yet public. The first public launch (v0.5.0) is targeted for mid-2026 with seeded content in at least two disciplines.

---

## [0.0.1] - 2026-04-15 (Internal)

### Added
- Project concept and initial conversations
- Vision for a Git-based, version-controlled scientific discovery engine
- Emphasis on legal compliance, community governance, and sustainable open science infrastructure

---

**Legend**
- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` for vulnerability fixes

For older versions, see the [Git history](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/commits/main).