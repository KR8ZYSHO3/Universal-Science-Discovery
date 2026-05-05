"""Generate bulk YAML content for Phase 0 content push (~300 entries)."""
import os
import textwrap

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")


# ─────────────────────────────────────────────────────────────
# MATERIALS SCIENCE UNKNOWNS (25)
# ─────────────────────────────────────────────────────────────
materials = [
    ("u-high-tc-superconductivity-mechanism", "What is the pairing mechanism in cuprate high-temperature superconductors above 77 K?",
     ["Phonon-mediated pairing is insufficient at these temperatures", "RVB and stripe-phase models remain contested"],
     ["Spin-fluctuation-mediated Cooper pairing explains the d-wave gap symmetry in cuprates"]),

    ("u-topological-insulator-surface-states", "Why do topological insulator surface states remain robust under certain perturbations but not others?",
     ["Time-reversal symmetry protection is well characterised", "Disorder effects on Dirac cone lifetime are poorly constrained"],
     ["Electron-electron interactions on TI surfaces create a symmetry-protected metal distinct from bulk predictions"]),

    ("u-metallic-glass-crystallisation", "What determines the nucleation kinetics and crystallisation pathways in metallic glasses?",
     ["Differential scanning calorimetry captures onset temperatures", "Atomic-level nucleation sites remain unresolved"],
     ["Icosahedral medium-range order suppresses crystallisation nucleation by raising the interfacial free energy"]),

    ("u-perovskite-stability-degradation", "What are the dominant degradation mechanisms limiting perovskite solar cell lifetime to under 20 years?",
     ["Ion migration under electric field identified as major pathway", "Role of grain boundaries vs bulk defects unresolved"],
     ["Halide segregation at grain boundaries is the primary long-term degradation pathway in mixed-halide perovskites"]),

    ("u-vdw-heterostructure-emergent-phases", "What emergent electronic phases arise in van der Waals heterostructures beyond graphene-hBN systems?",
     ["Magic-angle graphene superconductivity established", "Systematic phase diagram across twist angles incomplete"],
     ["Twist-angle engineering in TMD bilayers produces a universal phase diagram with Mott, superconducting, and topological regions"]),

    ("u-room-temperature-superconductivity", "What materials architecture would achieve ambient-pressure room-temperature superconductivity?",
     ["Hydrogen-rich compounds show Tc > 200 K at megabar pressures", "Stabilisation at ambient pressure remains unsolved"],
     ["Covalent hydrogen cage structures stabilised by electron donation from heavy elements achieve Tc > 273 K at ambient pressure"]),

    ("u-shape-memory-alloy-fatigue", "What atomic-scale mechanisms drive functional fatigue in shape-memory alloys after repeated cycling?",
     ["Dislocation accumulation measured macroscopically", "Martensite interface pinning at nanoscale unresolved"],
     ["Irreversible dislocation tangles at austenite-martensite interfaces accumulate with each cycle, raising transformation hysteresis"]),

    ("u-phonon-engineering-thermal", "Can phonon dispersion be engineered to achieve near-zero thermal conductivity in crystalline materials?",
     ["Phononic crystals reduce conductivity but introduce new scattering channels", "Lower bound on minimum lattice thermal conductivity disputed"],
     ["Resonant phonon scattering via rattler atoms in cage structures can approach the amorphous thermal conductivity limit"]),

    ("u-twistronics-moire-phases", "What is the full phase diagram of moiré superlattices as a function of twist angle, pressure, and field?",
     ["Correlated insulator and superconductor phases identified at magic angle", "Phase boundaries for non-graphene systems unmapped"],
     ["A universal topological Mott insulator phase exists at commensurate twist angles across all hexagonal van der Waals systems"]),

    ("u-metamaterial-wave-control", "What physical limits govern negative-index metamaterials for sub-diffraction imaging at optical frequencies?",
     ["Microwave negative refraction demonstrated", "Losses at optical frequencies remain prohibitive"],
     ["Gain-assisted optical metamaterials can overcome absorption losses and enable lossless sub-diffraction imaging"]),

    ("u-self-healing-polymer-mechanism", "What is the molecular mechanism enabling autonomous self-healing in non-covalent polymer networks?",
     ["Hydrogen bond reformation characterised by spectroscopy", "Kinetics of macroscopic crack healing poorly quantified"],
     ["Dynamic disulfide bond exchange rate sets the healing timescale independently of polymer backbone stiffness"]),

    ("u-entropy-stabilized-ceramics", "How does configurational entropy stabilise single-phase multi-principal-component oxides at room temperature?",
     ["Five-component high-entropy oxides synthesised at high temperature", "Thermodynamic stability window poorly defined"],
     ["Entropy of mixing exceeds the sum of individual-oxide formation enthalpies above a critical compositional diversity threshold"]),

    ("u-piezoelectric-biopolymers", "Can biological polymers like collagen and cellulose be tuned to achieve technologically relevant piezoelectric coefficients?",
     ["Natural piezoelectricity in bone and wood measured", "Molecular origin of piezoelectric response in hierarchical structures unclear"],
     ["Hierarchical fibril alignment optimised through processing achieves piezoelectric coefficients exceeding conventional ceramics in composite architectures"]),

    ("u-corrosion-mechanism-passivation", "What is the atomic-scale mechanism of passive film breakdown that initiates pitting corrosion?",
     ["Cl- adsorption identified as trigger in steels and aluminium", "Sub-nanometre film structure during breakdown unresolved"],
     ["Halide-induced local dissolution creates nanoscale pits that self-accelerate once depth exceeds a critical threshold"]),

    ("u-battery-dendrite-nucleation", "What determines the nucleation site and growth direction of lithium dendrites in battery anodes?",
     ["Surface heterogeneities identified as nucleation sites", "Predictive model linking surface chemistry to dendrite morphology lacking"],
     ["Local current density hotspots from SEI heterogeneity determine dendrite nucleation, and uniform SEI formation suppresses dendrites"]),

    ("u-solid-electrolyte-interface", "What is the full chemical composition and ion-transport mechanism of the solid electrolyte interphase?",
     ["Cryo-TEM reveals layered SEI structure", "Species-resolved ion conductivity across layers unmeasured"],
     ["Organic outer and inorganic inner SEI layers transport Li+ via distinct mechanisms whose relative resistance determines cycle life"]),

    ("u-hydrogen-embrittlement-pathway", "What is the dominant mechanism of hydrogen embrittlement in high-strength steels?",
     ["Hydrogen-enhanced decohesion and localised plasticity are competing models", "In-situ atomistic observations during fracture lacking"],
     ["Hydrogen localises at dislocations and reduces the Peierls barrier, causing premature plastic instability at crack tips"]),

    ("u-grain-boundary-segregation", "How does solute segregation to grain boundaries control polycrystalline material failure?",
     ["Atom probe tomography reveals segregant concentrations", "Segregation effect on fracture toughness poorly predicted from first principles"],
     ["Grain boundary embrittlement is dominated by electronic charge transfer from segregants rather than volumetric strain effects"]),

    ("u-quasicrystal-stability-origin", "What determines whether a quasicrystalline phase forms versus an approximant crystal in metallic alloys?",
     ["Hume-Rothery electron concentration rules partially explain stability", "Phason strain energy landscape poorly understood"],
     ["Pseudogap deepening at the Fermi level by quasiperiodic diffraction is the dominant stabilising mechanism over competing approximants"]),

    ("u-amorphous-metal-magnetism", "What causes the anomalously high coercivity in some amorphous metallic glass compositions?",
     ["Structural disorder reduces exchange coupling on average", "Local atomic clusters that pin domain walls unresolved"],
     ["Nanoscale chemical heterogeneity in as-quenched metallic glasses creates random magnetic anisotropy that sets coercivity"]),

    ("u-2d-material-defect-transport", "How do point defects and grain boundaries in 2D materials limit carrier mobility?",
     ["Suspended graphene achieves near-ballistic transport", "Chalcogenide grain boundary scattering cross-sections unmeasured"],
     ["Grain boundary tilt angle determines scattering cross-section, and specific tilt angles produce transmission resonances"]),

    ("u-ferroelectric-fatigue-mechanism", "What causes ferroelectric fatigue (loss of switchable polarisation) under repeated electric cycling?",
     ["Oxygen vacancy accumulation at electrodes identified", "Nucleation dynamics of reversed domains after fatigue unclear"],
     ["Oxygen vacancy clustering at 180-degree domain walls pins domain nucleation and suppresses switchable polarisation"]),

    ("u-biomineralisation-control", "How do organisms control polymorph selection and crystallographic texture during biomineralisation?",
     ["Acidic proteins influence calcite vs aragonite selection", "Protein-mineral interaction at nucleation site unresolved atomistically"],
     ["Specific amino acid sequences create epitaxial templates that select mineral polymorph through lattice matching"]),

    ("u-thermoelectric-zT-limit", "Is there a fundamental upper limit to thermoelectric figure-of-merit zT and what materials approach it?",
     ["zT > 3 achieved in some nanostructured materials", "Theoretical limit disputed because of coupled transport coefficients"],
     ["Phonon-glass electron-crystal nanocomposites can decouple thermal and electrical conductivity to achieve zT > 4 at optimal temperatures"]),

    ("u-radiation-damage-recovery", "What atomic mechanisms drive radiation damage recovery in nuclear materials and can they be accelerated?",
     ["Frenkel pair annihilation measured by positron annihilation spectroscopy", "Role of grain boundaries as defect sinks poorly quantified"],
     ["Grain boundaries act as unsaturable sinks for interstitials, and nanocrystalline metals with high boundary density show superior radiation tolerance"]),
]

for slug, title, gaps, hyps in materials:
    path = os.path.join(BASE, "unknowns-catalog", "materials-science", f"{slug}.yaml")
    gaps_str = "\n".join(f'  - "{g}"' for g in gaps)
    hyps_str = "\n".join(f'  - "{h}"' for h in hyps)
    content = f"""id: {slug}
title: "{title}"
status: open
systematic_gaps:
{gaps_str}
suggested_hypotheses:
{hyps_str}
"""
    write(path, content)

print(f"Written {len(materials)} materials-science unknowns")

# ─────────────────────────────────────────────────────────────
# CLIMATE SCIENCE UNKNOWNS (25)
# ─────────────────────────────────────────────────────────────
climate = [
    ("u-cloud-feedback-sign", "What is the net sign and magnitude of cloud feedback to CO2 forcing across all cloud types?",
     ["Low-cloud feedback is the dominant source of uncertainty in ECS", "Observational constraints from short satellite records are insufficient"],
     ["Marine boundary layer cloud amount decreases with SST warming, making low-cloud feedback strongly positive and raising ECS above 4 K"]),

    ("u-aerosol-cloud-indirect", "What is the magnitude of the aerosol first and second indirect effects on global radiative forcing?",
     ["IPCC AR6 estimates -0.45 W/m² with large uncertainty", "Cloud lifetime and precipitation suppression effects poorly separated"],
     ["Aerosol-induced suppression of drizzle in stratocumulus clouds doubles the lifetime effect beyond current model estimates"]),

    ("u-permafrost-tipping-point", "At what global temperature does permafrost carbon release become self-sustaining without further anthropogenic forcing?",
     ["Arctic permafrost holds ~1500 Gt C", "Feedback timescale and threshold temperature poorly constrained"],
     ["A 2.5°C global mean warming triggers irreversible permafrost degradation releasing >200 Gt C by 2200"]),

    ("u-amoc-collapse-threshold", "What is the critical freshwater forcing threshold for AMOC collapse and is it within 21st-century projections?",
     ["Hosing experiments show bistability in models", "Real-world freshwater flux from Greenland melt poorly observed"],
     ["AMOC crosses a saddle-node bifurcation at sustained Greenland melt exceeding 0.3 Sv, achievable under RCP8.5 by 2100"]),

    ("u-enso-predictability-limit", "What determines the fundamental predictability limit of ENSO beyond one year?",
     ["Atmospheric noise forcing limits deterministic predictability", "Coupled model ensembles show skill loss after 12-18 months"],
     ["Stochastic westerly wind burst forcing creates a chaotic barrier to ENSO predictability beyond 15 months"]),

    ("u-ice-sheet-instability-modes", "What are the dominant instability modes of the West Antarctic Ice Sheet under ocean warming?",
     ["Marine ice sheet instability theory predicts runaway retreat", "Ice cliff instability contested as physically unrealisable"],
     ["Retrograde bed slope instability in Thwaites Glacier is irreversible once grounding line retreats 150 km into deep basin"]),

    ("u-sai-side-effects", "What are the regional precipitation and ozone consequences of stratospheric aerosol injection?",
     ["Volcanic analogues suggest monsoon weakening", "Spatial patterns of SAI vs volcanic forcing differ substantially"],
     ["Equatorial SAI disproportionately weakens the West African monsoon while mid-latitude injection produces more uniform cooling"]),

    ("u-methane-clathrate-destabilization", "Under what ocean temperature trajectories do seafloor methane clathrates destabilise and contribute to atmospheric methane?",
     ["Clathrate stability zone shoaling detected in some Arctic shelves", "Emission rates from destabilisation events poorly quantified"],
     ["Shallow Arctic shelf clathrates are the most vulnerable and could contribute 0.5-1 Gt CH4/yr under 3°C ocean warming"]),

    ("u-polar-vortex-disruption", "What drives sudden stratospheric warming events and their link to extreme cold outbreaks at the surface?",
     ["SSW events precede extreme cold by 2-6 weeks", "Predictive mechanism linking stratospheric and tropospheric dynamics unclear"],
     ["Wave-2 Rossby wave breaking is the dominant trigger for major SSW events and accounts for 70% of observed polar vortex disruptions"]),

    ("u-carbon-cycle-feedbacks", "How do terrestrial carbon cycle feedbacks change sign under sustained high-CO2 forcing?",
     ["CO2 fertilisation saturates above certain temperatures and CO2 concentrations", "Threshold for ecosystem carbon source transition poorly constrained"],
     ["Tropical forests transition from carbon sinks to sources above 450 ppm CO2 when warming exceeds 2°C locally"]),

    ("u-ozone-recovery-timeline", "Will Antarctic ozone fully recover by 2070 and what are the confounding factors?",
     ["Montreal Protocol CFC phase-out is proceeding", "Short-lived halogens and climate-ozone interactions may delay recovery"],
     ["Heterogeneous chemistry on polar stratospheric clouds extended by climate change delays full Antarctic ozone recovery to 2090"]),

    ("u-monsoon-bifurcation", "Can the South Asian summer monsoon bifurcate to a permanently weakened state under continued aerosol loading?",
     ["Regional aerosol forcing reduces land-sea temperature gradient", "Tipping point vs smooth transition in monsoon strength unresolved"],
     ["Land-use change combined with absorbing aerosol loading can push the South Asian monsoon across a bifurcation to a persistent weak state"]),

    ("u-deep-ocean-carbon-sequestration", "What fraction of anthropogenic CO2 can be sequestered in the deep ocean on centennial timescales?",
     ["Thermohaline circulation transports carbon-rich surface water to deep ocean", "Remineralisation depth and efficiency poorly constrained by observations"],
     ["Biological pump efficiency increases under high-CO2 conditions, enhancing deep carbon sequestration by 15% per century"]),

    ("u-wildfire-climate-feedback", "What is the net radiative feedback of increasing wildfire frequency and extent under climate change?",
     ["Black carbon from fires has warming effect; aerosols have cooling effect", "Net sign of global wildfire feedback unresolved"],
     ["Increased wildfire aerosol loading has a net cooling effect at the global scale, partially offsetting regional warming from fire-vegetation feedbacks"]),

    ("u-urban-heat-island-nonlinearity", "Are urban heat island effects nonlinear with city size and density, and how do they interact with regional climate?",
     ["Linear scaling of UHI with population observed in some studies", "Mesoscale circulation feedbacks from large urban areas poorly understood"],
     ["Urban areas above 10 million population cross a nonlinear threshold generating persistent mesoscale convergence zones that amplify regional precipitation"]),

    ("u-climate-sensitivity-tails", "What physical processes determine the long upper tail of equilibrium climate sensitivity distributions?",
     ["Most models cluster at 2.5-4 K ECS with fat right tail", "High-ECS models not obviously wrong but not constrained by observations"],
     ["Cloud feedbacks over the Southern Ocean determine whether ECS exceeds 5 K, and present-day observations strongly constrain this"]),

    ("u-abrupt-climate-transitions", "What are the mechanisms of rapid Dansgaard-Oeschger events and can they occur in a warming world?",
     ["DO events involve 10-15°C Greenland warming within decades", "Trigger mechanism and ocean-atmosphere coupling unresolved"],
     ["Sea ice and AMOC positive feedback creates bistability enabling rapid transitions at certain threshold freshwater forcing values"]),

    ("u-marine-ice-cliff-instability", "Is marine ice cliff instability a physically realisable mechanism in Antarctica or limited by buttressing?",
     ["Theory predicts rapid retreat once cliff height exceeds ~90 m", "Laboratory and field evidence for catastrophic calving is limited"],
     ["Firn compaction and englacial hydrofracture are required co-requisites for marine ice cliff instability to contribute materially to sea level rise"]),

    ("u-antarctic-bottom-water", "What controls Antarctic Bottom Water formation rate and how will it respond to ice sheet freshening?",
     ["AABW has slowed 20-30% since the 1990s", "Freshwater sensitivity of AABW formation in models is poorly constrained"],
     ["Ross Sea AABW formation crosses a threshold at sustained freshwater input >0.1 Sv and may not recover on century timescales"]),

    ("u-peatland-carbon-dynamics", "How much carbon stored in tropical and boreal peatlands is vulnerable to release under warming and drainage?",
     ["Tropical peatlands store ~550 Gt C with high vulnerability to fire", "Depth-resolved carbon dating shows heterogeneous age structure"],
     ["Hydrological connectivity between peatland domes and surrounding landscapes determines whether drainage triggers deep carbon loss"]),

    ("u-stratosphere-troposphere-coupling", "How does stratospheric dynamics modulate the tropospheric jet streams on multi-decadal timescales?",
     ["QBO modulates extratropical weather regimes", "Long-term trends in stratospheric influence on surface climate unclear"],
     ["Stratospheric water vapor trends control the strength of downward influence and explain a significant fraction of tropospheric jet variability"]),

    ("u-regional-sea-level-acceleration", "What drives regional sea level accelerations that exceed the global mean by factors of 2-5?",
     ["Gravitational fingerprinting from ice melt partially explains spatial variability", "Ocean dynamic effects poorly constrained at coastal scales"],
     ["Weakening AMOC produces enhanced sea level rise along the US East Coast exceeding global mean by 30% through geostrophic adjustment"]),

    ("u-soil-moisture-atmosphere-feedback", "Does soil moisture-precipitation feedback create bistable wet-dry states in semi-arid regions?",
     ["Land-atmosphere coupling measured in some tropical and subtropical regions", "Threshold for bistability vs monotonic response poorly constrained"],
     ["Vegetation-soil moisture feedback creates hysteresis in rainfall, and degraded semi-arid landscapes can shift to permanently dry attractors"]),

    ("u-cloud-seeding-efficacy", "What is the true efficacy of cloud seeding for precipitation enhancement across different cloud types?",
     ["Randomised experiments are limited by small sample sizes", "Physical mechanism of ice nucleation enhancement under field conditions unclear"],
     ["Glaciogenic cloud seeding increases orographic precipitation by 10-15% in convectively stable clouds with adequate supercooled liquid water"]),

    ("u-arctic-amplification-mechanism", "What fraction of Arctic amplification is caused by local feedbacks versus poleward heat transport changes?",
     ["Sea ice-albedo feedback accounts for ~40% of amplification in models", "Poleward latent and dry static energy transport attribution is model-dependent"],
     ["Increased poleward moisture transport driven by enhanced water vapor content accounts for the majority of polar amplification above 70°N"]),
]

for slug, title, gaps, hyps in climate:
    path = os.path.join(BASE, "unknowns-catalog", "climate-science", f"{slug}.yaml")
    gaps_str = "\n".join(f'  - "{g}"' for g in gaps)
    hyps_str = "\n".join(f'  - "{h}"' for h in hyps)
    content = f"""id: {slug}
title: "{title}"
status: open
systematic_gaps:
{gaps_str}
suggested_hypotheses:
{hyps_str}
"""
    write(path, content)

print(f"Written {len(climate)} climate-science unknowns")

# ─────────────────────────────────────────────────────────────
# ASTRONOMY UNKNOWNS (25)
# ─────────────────────────────────────────────────────────────
astronomy = [
    ("u-dark-matter-particle-identity", "What particle or particles constitute cosmological dark matter?",
     ["WIMPs have not been detected despite decades of searches", "Axion and sterile neutrino parameter space largely unexplored"],
     ["Ultralight axion dark matter with mass ~10^-22 eV forms a Bose-Einstein condensate explaining galactic core-cusp discrepancies"]),

    ("u-dark-energy-equation-of-state", "Is dark energy a cosmological constant or a dynamical field, and what is its equation of state w(z)?",
     ["CMB and supernovae are consistent with w=-1 but uncertainties allow evolution", "DESI 2026 results suggest potential w≠-1 tension"],
     ["Dark energy is a slowly rolling scalar field with w crossing -1 at z~0.3, distinguishable with next-generation surveys"]),

    ("u-fast-radio-burst-origin", "What are the dominant progenitor mechanisms for cosmological fast radio bursts?",
     ["Magnetars confirmed as one source class from SGR 1935+2154", "Volumetric rate and diversity suggest multiple progenitors"],
     ["Magnetar flares account for the majority of repeating FRBs while compact binary mergers produce the non-repeating population"]),

    ("u-magnetar-formation-mechanism", "What fraction of neutron stars form as magnetars and what determines the extreme magnetic field strength?",
     ["Galactic magnetar population constrains birth rate to ~10% of neutron stars", "Dynamo mechanism during proto-NS convection is uncertain"],
     ["Rapid proto-neutron star rotation during convective dynamo amplification generates fields >10^15 G when spin period < 5 ms at birth"]),

    ("u-neutron-star-equation-of-state", "What is the equation of state of dense nuclear matter above 2× nuclear saturation density?",
     ["GW170817 tidal deformability constrains radius to 11-13 km", "Phase transition to quark matter is unconstrained above 3ρ_0"],
     ["A first-order phase transition to deconfined quark matter occurs at ~3 nuclear saturation densities, creating a mass gap at 2.5-2.8 solar masses"]),

    ("u-primordial-gravitational-waves", "What is the tensor-to-scalar ratio r and what does it imply for inflationary models?",
     ["Planck and BICEP/Keck place upper limit r < 0.036", "CMB-S4 and LiteBIRD will probe r ~ 0.001"],
     ["Plateau inflation models predict r ~0.004, detectable by next-generation CMB polarisation experiments"]),

    ("u-hubble-tension-origin", "What physical mechanism resolves the 5σ tension between local and CMB-inferred Hubble constants?",
     ["Cepheid and TRGB distance ladders agree with each other", "No single systematic error identified that explains the discrepancy"],
     ["Early dark energy that decays before recombination reduces the sound horizon and reconciles CMB-inferred H0 with local measurements"]),

    ("u-early-galaxy-formation-jwst", "Why do JWST observations reveal massive, evolved galaxies at z>10 that are absent in ΛCDM predictions?",
     ["JWST finds candidate massive galaxies at z~12-16 inconsistent with standard models", "Photometric redshifts and mass estimates carry large uncertainties"],
     ["Enhanced star formation efficiency in minihaloes at z>10 driven by metal-free Population III enrichment explains the excess massive galaxy population"]),

    ("u-cosmic-string-networks", "Do cosmic string networks exist and what are their observational signatures in the CMB and gravitational wave background?",
     ["CMB non-Gaussianity limits string tension Gμ < 10^-7", "PTA gravitational wave background could include string signal"],
     ["Cosmic string networks with tension Gμ ~10^-10 contribute a distinctive spectral feature to the nanohertz gravitational wave background"]),

    ("u-baryon-asymmetry-origin", "What is the mechanism of baryogenesis that produced the observed matter-antimatter asymmetry?",
     ["Sakharov conditions require B violation, CP violation, and departure from equilibrium", "Standard Model CP violation is insufficient by many orders of magnitude"],
     ["Leptogenesis from heavy Majorana neutrino decay in the early universe generates sufficient baryon asymmetry via sphaleron processes"]),

    ("u-black-hole-information-paradox", "Is information destroyed by black hole evaporation, and if not, how is it encoded in Hawking radiation?",
     ["Page curve requires information to escape before page time", "Island formula and replica wormholes provide calculation but physical mechanism unclear"],
     ["Gravitational replica wormholes encode quantum information in Hawking radiation correlations that only become detectable after the Page time"]),

    ("u-stellar-bh-spin-distribution", "What process sets the spin magnitude distribution of stellar-mass black holes in binary systems?",
     ["LIGO measurements show a bimodal spin distribution", "Natal kick, accretion, and tidal synchronisation contributions poorly separated"],
     ["Natal kick direction relative to pre-collapse spin determines post-collapse misalignment, producing the observed bimodal effective spin distribution"]),

    ("u-type-ia-supernova-progenitor", "What stellar system produces the majority of Type Ia supernovae: single-degenerate or double-degenerate?",
     ["Both channels produce Chandrasekhar and sub-Chandrasekhar explosions", "No surviving companion detected in nearby remnants"],
     ["The double-degenerate merger channel dominates at low metallicity while single-degenerate systems account for the bright-end luminosity function"]),

    ("u-population-iii-stars", "When and where can Population III stars first be detected, and what is their characteristic mass function?",
     ["21-cm observations may probe the cosmic dawn", "No direct observation of Pop III star confirmed"],
     ["JWST can detect gravitationally lensed Pop III stars in magnification events during the epoch of reionisation at z~10-15"]),

    ("u-uhecr-origin", "What are the sources of ultra-high-energy cosmic rays above the GZK cutoff and what accelerates them?",
     ["Pierre Auger Observatory shows anisotropy toward star-forming galaxies", "Composition measurements are inconsistent between experiments"],
     ["Starburst galaxy jets accelerate heavy nuclei via shear acceleration, explaining UHECR composition and directional correlations"]),

    ("u-gwb-spectrum", "What is the origin of the nanohertz gravitational wave background detected by pulsar timing arrays?",
     ["NANOGrav 15-year data shows a stochastic background", "Supermassive black hole binary vs exotic origins unresolved"],
     ["Supermassive black hole binary coalescences at z<1 produce the majority of the observed GWB signal with environmental hardening timescales <100 Myr"]),

    ("u-quasar-feedback-mechanism", "How does quasar feedback quench star formation in massive galaxies across cosmic time?",
     ["AGN-driven outflows observed reaching kpc scales", "Whether outflows prevent star formation or merely redistribute gas is unresolved"],
     ["Quasar-driven outflows heat circumgalactic gas to prevent future infall rather than expelling ISM directly, quenching star formation on Gyr timescales"]),

    ("u-cgm-enrichment", "How is the circumgalactic medium enriched with metals and what is its role in the baryon cycle?",
     ["Quasar absorption spectroscopy reveals CGM metallicity ~0.1 solar", "Mechanism of metal transport from galactic disk to CGM poorly constrained"],
     ["Supernova-driven galactic winds efficiently transport metals to the CGM at z>2, and the CGM acts as a reservoir for future star formation"]),

    ("u-cluster-cooling-flows", "Why do galaxy cluster cooling flows not form stars at the rates predicted by their X-ray luminosities?",
     ["Soft X-ray cooling should deposit hundreds solar masses per year", "Observed star formation rates are 10-100× lower"],
     ["AGN jet feedback deposits energy at the sound speed in the intracluster medium, maintaining thermal balance and suppressing cooling flows"]),

    ("u-exoplanet-biosignature-false-positives", "What abiotic processes can mimic biosignature gases in exoplanet atmospheres?",
     ["Photochemical O2 and O3 production identified around M dwarfs", "False positive probability as a function of host star type unpredictified"],
     ["Volcanic hydrogen outgassing on water-rich rocky planets produces abiotic CH4 and CO2 ratios indistinguishable from biogenic signatures"]),

    ("u-galaxy-angular-momentum", "How is angular momentum transported during galaxy formation to produce the observed diversity of disk sizes?",
     ["Angular momentum is acquired from tidal torques during collapse", "Angular momentum loss to dark matter halo and mergers poorly quantified"],
     ["Feedback-regulated disk formation preserves angular momentum by preventing early gaseous collapse before virialization"]),

    ("u-reionization-topology", "What is the spatial topology of cosmic reionization and which sources dominate the ionizing photon budget?",
     ["21-cm observations will probe reionization morphology", "Faint galaxy vs AGN contribution at z>6 unresolved"],
     ["Low-luminosity star-forming galaxies provide the dominant ionizing photon budget while rare AGN drive topology in overdense regions"]),

    ("u-stellar-initial-mass-function", "Is the stellar initial mass function universal, and what physics drives variations in extreme environments?",
     ["IMF appears top-heavy in some starburst systems", "Radiation pressure and magnetic field effects on fragmentation poorly modelled"],
     ["The characteristic Jeans mass set by dust cooling temperature drives IMF variations, producing top-heavy IMFs in high-pressure starbursts"]),

    ("u-magnetic-field-origin-galaxies", "What generates and maintains large-scale magnetic fields in galaxies over Hubble time?",
     ["Galactic dynamo theory predicts exponential amplification from weak seed fields", "Seed field origin and coherence length are uncertain"],
     ["A small-scale turbulent dynamo operating at z>10 generates sufficient coherent field to seed the large-scale galactic dynamo by cosmic noon"]),

    ("u-globular-cluster-formation", "How do globular clusters form and why do they show multiple stellar populations?",
     ["Multiple populations require multiple star formation episodes within GCs", "Self-enrichment mechanism and required gas retention disputed"],
     ["Massive proto-GC clumps in high-redshift disk galaxies undergo multiple fragmentation episodes, each producing a distinct chemical population"]),
]

for slug, title, gaps, hyps in astronomy:
    path = os.path.join(BASE, "unknowns-catalog", "astronomy", f"{slug}.yaml")
    gaps_str = "\n".join(f'  - "{g}"' for g in gaps)
    hyps_str = "\n".join(f'  - "{h}"' for h in hyps)
    content = f"""id: {slug}
title: "{title}"
status: open
systematic_gaps:
{gaps_str}
suggested_hypotheses:
{hyps_str}
"""
    write(path, content)

print(f"Written {len(astronomy)} astronomy unknowns")

# ─────────────────────────────────────────────────────────────
# MEDICINE UNKNOWNS (30)
# ─────────────────────────────────────────────────────────────
medicine = [
    ("u-sepsis-heterogeneity", "What molecular subtypes of sepsis determine differential responses to standard-of-care treatment?",
     ["Two genomic endotypes (SRS1/SRS2) identified from ICU transcriptomics", "Causal pathway from subtype to outcome unresolved"],
     ["SRS1 immunosuppressed endotype requires immune reconstitution rather than anti-inflammatory therapy to improve mortality"]),

    ("u-autoimmune-trigger-identification", "What environmental triggers initiate autoimmune disease in genetically susceptible individuals?",
     ["Molecular mimicry between pathogen peptides and self-antigens identified in some conditions", "Timing and dose-response of trigger exposure poorly characterised"],
     ["Gut epithelial barrier breach during specific bacterial dysbiosis states is the necessary co-trigger for autoimmune onset in genetically susceptible hosts"]),

    ("u-immunotherapy-nonresponders", "Why do most solid tumour patients not respond to PD-1/PD-L1 checkpoint blockade?",
     ["Tumour mutational burden and PD-L1 expression are insufficient predictors", "Microbiome, tumour microenvironment, and systemic immunity all contribute"],
     ["Dysfunction of CD8+ T cell precursor exhaustion state rather than terminal exhaustion determines whether checkpoint blockade restores anti-tumour immunity"]),

    ("u-alzheimer-causal-biomarkers", "Which amyloid and tau species are causal versus correlational in Alzheimer's disease progression?",
     ["Anti-amyloid trials have had mixed results", "Temporal ordering of amyloid, tau, and neurodegeneration biomarkers remains debated"],
     ["Soluble amyloid oligomers rather than plaques drive synaptic dysfunction, explaining why plaque clearance does not consistently improve cognition"]),

    ("u-antibiotic-resistance-rate", "What determines the rate at which antibiotic resistance evolves in clinical settings?",
     ["Horizontal gene transfer and selection pressure are key factors", "Quantitative prediction of resistance emergence timeline is lacking"],
     ["Phage predation pressure co-determines resistance evolution rate, and phage therapy can slow resistance emergence by imposing evolutionary trade-offs"]),

    ("u-microbiome-mental-health", "Does gut microbiome composition causally influence mental health outcomes via the gut-brain axis?",
     ["Germ-free animal studies show gut microbiome affects anxiety-like behaviour", "Human causal evidence limited by confounding"],
     ["Specific short-chain fatty acid producers modulate tryptophan availability to the brain and causally influence depression susceptibility"]),

    ("u-long-covid-mechanism", "What are the pathological mechanisms driving long COVID symptoms persisting beyond 12 weeks?",
     ["Viral persistence, autoimmunity, and microbiome disruption are candidate mechanisms", "No single mechanism has been confirmed in all patients"],
     ["Persistent SARS-CoV-2 RNA in gut reservoir drives systemic inflammation and explains the heterogeneous multi-system symptoms of long COVID"]),

    ("u-placebo-neural-basis", "What are the neural mechanisms mediating placebo analgesia and can they be therapeutically enhanced?",
     ["Endogenous opioid activation is one mechanism", "Non-opioid placebo pathways and their magnitude are poorly characterised"],
     ["Expectation-driven descending inhibitory control through the periaqueductal gray mediates the majority of placebo analgesia independent of opioid tone"]),

    ("u-anesthesia-consciousness", "By what mechanism do general anaesthetics suppress consciousness and could this inform theories of consciousness?",
     ["GABA-A potentiation and NMDA inhibition are primary targets", "Why different drugs at different doses produce the same endpoint of unconsciousness is unclear"],
     ["General anaesthetics suppress consciousness by disrupting thalamocortical feedback necessary for global workspace ignition, not by directly silencing cortex"]),

    ("u-chronic-pain-sensitization", "What drives the transition from acute to chronic pain via central sensitization?",
     ["Spinal dorsal horn long-term potentiation is a candidate mechanism", "Genetic and psychological risk factors for chronification poorly integrated"],
     ["Microglial-mediated synaptic stripping in the spinal dorsal horn establishes a self-sustaining central sensitization state independent of peripheral input"]),

    ("u-prion-spread-pathway", "By what cellular and intercellular mechanisms do prion proteins spread between neurons?",
     ["Exosome-mediated transfer and trans-synaptic spread are candidate pathways", "In vivo kinetics of prion propagation poorly quantified"],
     ["Tunnelling nanotube-mediated transfer of misfolded PrP between neurons is the dominant spread pathway and explains anatomical progression patterns"]),

    ("u-stem-cell-niche-regulation", "What signals maintain adult stem cell quiescence and what triggers activation for tissue repair?",
     ["Wnt, Notch and mTOR pathways regulate stem cell state", "Cell-extrinsic metabolic signals from the niche are poorly characterised"],
     ["Lactate secreted by niche stromal cells is a primary metabolic signal that maintains HSC quiescence via epigenetic regulation"]),

    ("u-organ-fibrosis-reversibility", "Under what conditions is established organ fibrosis reversible rather than permanent?",
     ["Liver fibrosis can regress after HCV cure", "Myofibroblast fate and matrix cross-linking extent determine reversibility"],
     ["Myofibroblast reversion to quiescent stellate cells occurs when TGF-β signalling is withdrawn before irreversible collagen cross-linking, defining a treatment window"]),

    ("u-telomere-aging-causality", "Does telomere shortening causally drive aging or is it a biomarker of other aging processes?",
     ["Mendelian randomisation studies show mixed results", "Telomerase activation in model organisms extends healthspan but not consistently lifespan"],
     ["Telomere shortening in replicative tissues causally limits healthspan via senescence induction, but is not the primary driver of post-mitotic tissue aging"]),

    ("u-mrna-vaccine-durability", "What limits the durability of immunity from mRNA vaccines and can formulation changes extend it?",
     ["mRNA vaccine immunity wanes faster than live-attenuated vaccines", "Germinal centre dynamics and long-lived plasma cell generation differ between platforms"],
     ["Lipid nanoparticle clearance kinetics determine antigen exposure duration and are the primary determinant of germinal centre quality and memory B cell output"]),

    ("u-type2-diabetes-reversal", "What is the mechanism of type 2 diabetes remission following bariatric surgery or very low calorie diets?",
     ["Rapid glucose normalisation precedes weight loss, suggesting gut hormone effects", "Relative contribution of gut hormones, caloric restriction, and gut microbiome is disputed"],
     ["Portal fatty acid signalling disruption after bariatric surgery is the primary mechanism of rapid beta cell function recovery independent of weight loss"]),

    ("u-tbi-repair-limits", "What limits neurological recovery after severe traumatic brain injury and what interventions cross this limit?",
     ["Axonal regeneration in the CNS is suppressed by myelin-associated inhibitors", "Secondary injury cascades in the weeks following TBI worsen outcomes"],
     ["Scar-forming reactive astrocytes create a physical and molecular barrier that limits axonal regeneration, and matrix metalloproteinase-mediated scar remodelling restores connectivity"]),

    ("u-cardiac-regeneration-barriers", "Why do adult mammalian cardiomyocytes fail to regenerate after myocardial infarction?",
     ["Neonatal hearts can regenerate but adults cannot", "Transition from regenerative to non-regenerative phenotype occurs around postnatal day 7 in rodents"],
     ["Oxidative metabolism transition at postnatal day 7 induces cardiomyocyte binucleation and cell cycle arrest, and reverting to glycolytic metabolism restores proliferative capacity"]),

    ("u-hearing-regeneration-mammals", "Why do mammals fail to regenerate cochlear hair cells after noise or drug-induced loss?",
     ["Birds and fish regenerate hair cells via supporting cell transdifferentiation", "Wnt and Notch pathway manipulation partially restores hair cell number in mice"],
     ["Epigenetic silencing of pro-regenerative Atoh1 target genes in adult mammalian supporting cells prevents transdifferentiation and is reversible by HDAC inhibition"]),

    ("u-spinal-cord-complete-repair", "Is complete motor function recovery after complete spinal cord injury achievable and what barriers remain?",
     ["Epidural stimulation restores stepping in incomplete injuries", "Axonal bridging across complete lesions has not been achieved in clinical settings"],
     ["Combinatorial treatment with axon guidance molecules, neural stem cell bridges, and activity-dependent stimulation achieves functional reconnection across complete lesions in primates"]),

    ("u-cancer-immunoediting", "How does tumour immunoediting shape the neoantigen landscape and what drives immune escape?",
     ["Loss of HLA alleles and neoantigen downregulation documented", "Kinetics of immunoediting during early oncogenesis poorly characterised"],
     ["Early clonal neoantigens are preferentially lost through immunoediting, and the degree of neoantigen loss predicts checkpoint blockade response"]),

    ("u-pain-sex-differences", "What biological mechanisms underlie sex differences in pain sensitivity and chronic pain prevalence?",
     ["Microglia play a sexually dimorphic role in pain signalling in rodents", "Hormonal versus genetic contributions to human sex differences are poorly separated"],
     ["T cell-dependent microglial activation in the spinal cord drives chronic pain in males while females use a T cell-independent CGRP-mediated pathway"]),

    ("u-vaccine-adjuvant-mechanism", "How do vaccine adjuvants enhance adaptive immune responses at the cellular and molecular level?",
     ["TLR agonist adjuvants activate innate immunity to provide danger signals", "Downstream mechanisms linking adjuvant to germinal centre quality are unclear"],
     ["Adjuvant-induced type I interferon production by dendritic cells is the primary signal enhancing germinal centre reactions and long-lived plasma cell output"]),

    ("u-neuroinflammation-psychiatric", "What is the causal role of neuroinflammation in treatment-resistant psychiatric disorders?",
     ["Elevated inflammatory markers correlate with treatment resistance", "Whether inflammation causes or results from psychiatric symptoms is unresolved"],
     ["Microglia-mediated synaptic pruning in the prefrontal cortex is a causal mechanism in treatment-resistant depression that is reversible by anti-inflammatory intervention"]),

    ("u-immune-aging-rejuvenation", "What drives age-related immune decline (immunosenescence) and can it be pharmacologically reversed?",
     ["Thymic involution and naive T cell pool contraction are key features", "Transcriptional vs epigenetic basis of T cell exhaustion poorly separated"],
     ["Thymic regeneration through IL-7 and FGF7 signalling combined with senescent cell clearance restores naive T cell output and reverses functional immunosenescence"]),

    ("u-organ-clock-synchrony", "How do peripheral circadian clocks in organs synchronise with the central SCN clock and what disrupts this?",
     ["Feeding time entrains peripheral clocks independently of light cues", "Molecular mechanism of peripheral desynchrony in shift workers unclear"],
     ["Liver clock desynchrony from feeding-fasting cycles in shift workers is the primary driver of metabolic syndrome risk independent of sleep disruption"]),

    ("u-cancer-stem-cell-hierarchy", "Is cancer stem cell hierarchy fixed or plastic and what determines transition between states?",
     ["Lineage tracing shows clonal evolution in some cancers", "Non-hierarchical stochastic models also fit data in some cancers"],
     ["Microenvironmental signalling gradients maintain cancer stem cell hierarchy in vivo, and this hierarchy is plastic and reversed by EMT induction"]),

    ("u-blood-brain-barrier-regulation", "What molecular signals dynamically regulate blood-brain barrier permeability in health and disease?",
     ["Tight junction proteins and efflux transporters characterised", "Dynamic regulation by neural activity and inflammation poorly understood"],
     ["Astrocyte end-feet signalling through aquaporin-4 dynamically regulates paracellular permeability in response to neuronal activity"]),

    ("u-pancreatic-beta-cell-exhaustion", "What drives beta cell exhaustion in type 2 diabetes and can exhausted cells be functionally rescued?",
     ["Glucotoxicity and lipotoxicity impair insulin secretion", "Whether beta cell mass loss or functional exhaustion dominates is unresolved"],
     ["Endoplasmic reticulum stress from unfolded proinsulin is the primary driver of beta cell dysfunction and is reversible by GLP-1 receptor agonism"]),

    ("u-lymphatic-system-brain", "How does the glymphatic-lymphatic system clear metabolic waste from the brain and what impairs this in aging?",
     ["Sleep-dependent AQP4-mediated CSF-ISF exchange characterised", "Whether glymphatic impairment causes or follows Alzheimer's pathology unclear"],
     ["AQP4 depolarisation from reactive astrogliosis impairs glymphatic clearance and accelerates amyloid accumulation in a self-sustaining feedback loop"]),
]

for slug, title, gaps, hyps in medicine:
    path = os.path.join(BASE, "unknowns-catalog", "medicine", f"{slug}.yaml")
    gaps_str = "\n".join(f'  - "{g}"' for g in gaps)
    hyps_str = "\n".join(f'  - "{h}"' for h in hyps)
    content = f"""id: {slug}
title: "{title}"
status: open
systematic_gaps:
{gaps_str}
suggested_hypotheses:
{hyps_str}
"""
    write(path, content)

print(f"Written {len(medicine)} medicine unknowns")

# ─────────────────────────────────────────────────────────────
# COGNITIVE SCIENCE UNKNOWNS (20)
# ─────────────────────────────────────────────────────────────
cognitive = [
    ("u-hard-problem-consciousness", "Why and how does subjective experience arise from physical brain processes?",
     ["Neural correlates of consciousness identified but not explanatory", "Integrated information theory and global workspace theory make conflicting predictions"],
     ["Recurrent processing in higher cortical areas is necessary and sufficient for phenomenal consciousness, and feedforward-only processing is never conscious"]),

    ("u-neural-correlates-self", "What neural substrates constitute the minimal self and how do they generate a sense of personal identity?",
     ["Default mode network implicated in self-referential processing", "Bodily self, autobiographical self, and narrative self have different substrates"],
     ["Interoceptive prediction error signals from the insula construct the minimal bodily self, and disruption of this signal explains depersonalisation"]),

    ("u-language-critical-period", "What biological mechanisms close the critical period for first language acquisition at puberty?",
     ["Myelination and synaptic pruning occur during the critical period", "Whether closure is driven by neural maturation or experience-dependent plasticity is unresolved"],
     ["GABAergic maturation shifts the excitation-inhibition balance in language cortex, closing the critical period independently of language exposure"]),

    ("u-face-recognition-substrate", "What is the computational and neural architecture of face recognition in humans versus other primates?",
     ["Fusiform face area and occipital face area form a cortical network", "Why faces engage specialised processing while other expert object categories do not is unclear"],
     ["Face recognition employs a holistic configural processing strategy implemented in a partially specialised cortical network that develops through experience with faces"]),

    ("u-working-memory-capacity", "What neural and computational mechanisms impose the ~4-item limit of working memory?",
     ["Gamma-theta oscillatory coding has been proposed", "Whether capacity limit reflects interference, resource, or slot-based constraints is unresolved"],
     ["Competitive attractor dynamics in prefrontal cortex allow at most 4 stable simultaneously active representations due to inhibitory normalisation constraints"]),

    ("u-decision-fatigue-neural", "What neural mechanisms produce decision fatigue and degraded choice quality with repeated decisions?",
     ["Anterior cingulate activity declines with repeated decisions", "Metabolic depletion versus neural adaptation explanations are unresolved"],
     ["Repeated engagement of conflict monitoring in ACC induces synaptic depression that reduces effortful deliberation quality independently of blood glucose levels"]),

    ("u-creativity-neural-mechanism", "What distinguishes the neural dynamics of creative versus routine cognition?",
     ["Default mode and executive control networks co-activate during creative tasks", "Whether DMN-ECN coupling is necessary or correlational is unclear"],
     ["Transient synchronisation between default mode, salience, and executive networks creates a cognitive state enabling remote association that is the neural basis of creative insight"]),

    ("u-insight-problem-solving", "What neural and computational processes underlie the sudden insight that solves previously stuck problems?",
     ["Gamma bursts in right temporal cortex precede insight reports", "Unconscious restructuring of problem representation has no agreed neural mechanism"],
     ["Spreading activation in semantic networks accumulates below threshold until a contextual cue causes superadditive summation that crosses the threshold for conscious insight"]),

    ("u-mind-wandering-function", "What adaptive function does mind wandering serve and what determines its content?",
     ["Mind wandering correlates with future-oriented prospective thinking", "Whether spontaneous thought is content-random or systematically biased toward concerns is debated"],
     ["Mind wandering implements offline prospective simulation that prioritises unresolved personal goals, serving planning and autobiographical memory consolidation"]),

    ("u-social-cognition-architecture", "What is the neural architecture of social cognition and how does it differ from non-social cognition?",
     ["Temporoparietal junction and medial prefrontal cortex implicated in mentalizing", "Whether social cognition uses domain-specific or domain-general mechanisms is disputed"],
     ["Social cognition uses partially specialised neural systems with a domain-general predictive coding substrate modified by statistical structure specific to social agents"]),

    ("u-emotion-categorization", "Are basic emotions universal biological categories or culturally constructed prototypes?",
     ["Cross-cultural facial expression studies show both universal and culture-specific patterns", "Methodological confounds in cross-cultural research unresolved"],
     ["Core affect dimensions (valence, arousal) are universal neurobiological primitives, while discrete emotion categories are cultural conceptual overlays"]),

    ("u-hippocampal-spatial-code", "How does the hippocampal-entorhinal spatial code scale to large environments and abstract cognitive maps?",
     ["Grid cells tile space with scale determined by entorhinal location", "How grid scale is set and whether maps are continuous or modular is unresolved"],
     ["A hierarchy of grid scales from dorsal to ventral entorhinal cortex enables spatial representation across 7 orders of magnitude through nested modular maps"]),

    ("u-time-perception-mechanism", "What neural mechanisms produce subjective time perception and what causes its distortions?",
     ["Interval timing in the seconds range involves basal ganglia and supplementary motor area", "Mechanism of temporal distortion under emotion or attention load unclear"],
     ["Dopaminergic striatal activity encodes subjective time by setting the rate of pacemaker-like oscillatory cycles that accumulate in working memory"]),

    ("u-attention-spotlight-mechanism", "How does selective attention filter sensory information and what are the neural mechanisms of the attentional spotlight?",
     ["Top-down signals from FEF and IPS modulate sensory cortex activity", "Whether attention operates through gain modulation, noise reduction, or synchronisation is unresolved"],
     ["Attention selectively synchronises gamma-band oscillations between visual cortex and frontoparietal areas, implementing competitive selection through oscillatory gating"]),

    ("u-perceptual-binding-problem", "How does the brain bind features processed in different cortical areas into unified percepts?",
     ["Synchronous gamma oscillations proposed as binding mechanism", "No single mechanism has withstood experimental scrutiny"],
     ["Recurrent feedback from higher areas imposes coherent phase relationships on lower-area gamma oscillations, implementing binding without requiring synchrony as an independent mechanism"]),

    ("u-theory-of-mind-substrate", "What is the minimal neural substrate for theory of mind and when does it develop ontogenetically?",
     ["TPJ and mPFC are reliably activated in explicit ToM tasks", "Whether implicit ToM in infancy uses the same substrate as explicit ToM in adults is unresolved"],
     ["Implicit ToM uses an automatic subcortical route through the superior colliculus and pulvinar while explicit ToM additionally recruits prefrontal deliberative processes"]),

    ("u-metacognition-substrate", "What neural mechanisms allow metacognitive access to one's own cognitive states?",
     ["Prefrontal areas are necessary for metacognitive reports", "Whether metacognition uses a dedicated system or is a special case of general monitoring is unresolved"],
     ["Hierarchical predictive processing in anterior prefrontal cortex generates second-order predictions about first-order confidence that constitute metacognitive representations"]),

    ("u-implicit-explicit-memory-boundary", "What determines whether a memory is expressed implicitly versus explicitly and can this boundary be shifted?",
     ["Hippocampus is necessary for explicit but not implicit memory", "Boundary conditions between systems and their interaction are poorly characterised"],
     ["Retrieval context determines which memory system dominates expression, and sleep selectively consolidates hippocampal traces into neocortical representations available for explicit access"]),

    ("u-sleep-creative-insight", "How does sleep enhance creative problem solving and what stages are critical?",
     ["REM sleep associated with remote association improvements", "NREM sleep role in creative insight distinct from its role in procedural memory is unclear"],
     ["REM sleep reactivates weakly associated memory traces and enhances semantic network connectivity, producing novel associations detectable as creative insight on waking"]),

    ("u-cognitive-reserve-mechanism", "What neural mechanisms underlie cognitive reserve and how do they delay symptom onset in Alzheimer's disease?",
     ["Education and cognitive activity correlate with reserve", "Whether reserve reflects more synapses, more efficient networks, or compensatory recruitment is unresolved"],
     ["Cognitive reserve is implemented through increased functional network redundancy that allows rerouting of processing around focal Alzheimer's pathology"]),
]

for slug, title, gaps, hyps in cognitive:
    path = os.path.join(BASE, "unknowns-catalog", "cognitive-science", f"{slug}.yaml")
    gaps_str = "\n".join(f'  - "{g}"' for g in gaps)
    hyps_str = "\n".join(f'  - "{h}"' for h in hyps)
    content = f"""id: {slug}
title: "{title}"
status: open
systematic_gaps:
{gaps_str}
suggested_hypotheses:
{hyps_str}
"""
    write(path, content)

print(f"Written {len(cognitive)} cognitive-science unknowns")

# ─────────────────────────────────────────────────────────────
# MATHEMATICS UNKNOWNS (20 new)
# ─────────────────────────────────────────────────────────────
mathematics = [
    ("u-p-vs-np-geometric-barriers", "What geometric barriers prevent current proof techniques from resolving P vs NP?",
     ["Relativisation, natural proofs, and algebrisation barriers identified", "No framework captures all known barriers simultaneously"],
     ["A fourth barrier related to non-uniform circuit complexity prevents diagonalisation-based approaches from separating P and NP"]),

    ("u-riemann-zero-distribution", "What determines the distribution of non-trivial zeros of the Riemann zeta function along the critical line?",
     ["Over 10^13 zeros confirmed on the critical line by numerical computation", "Random matrix theory predicts spacing statistics that match, without a proof"],
     ["The GUE eigenvalue statistics of zeros reflect an underlying quantum chaotic Hamiltonian whose existence would imply the Riemann Hypothesis"]),

    ("u-abc-conjecture-verification", "Is Mochizuki's proof of the abc conjecture correct and how can it be made verifiable by the community?",
     ["IUT theory has been disputed by Scholze and Stix since 2018", "The gap in Corollary 3.12 has not been resolved to community consensus"],
     ["A reformulation of IUT in classical scheme-theoretic language exists that would make the proof verifiable without understanding the full inter-universal Teichmuller theory"]),

    ("u-3manifold-invariants-completeness", "Are quantum invariants of 3-manifolds complete in the sense of distinguishing all non-homeomorphic 3-manifolds?",
     ["Jones polynomial and Witten-Reshetikhin-Turaev invariants distinguish many but not all pairs", "Whether any single quantum invariant is complete is unknown"],
     ["The coloured Jones polynomial evaluated at all roots of unity is a complete invariant for prime 3-manifolds"]),

    ("u-langlands-physics-connection", "What is the precise mathematical connection between the geometric Langlands program and quantum field theory?",
     ["Kapustin-Witten established a physics framework via S-duality of 4d gauge theories", "Derived categorical formulation and its relation to QFT is incomplete"],
     ["Electric-magnetic duality in 4d N=4 super Yang-Mills is the exact physical counterpart of geometric Langlands duality, and a rigorous proof exists via TQFT factorisation"]),

    ("u-turbulence-mathematical-formulation", "Can turbulence in three-dimensional fluids be described by a complete mathematical theory?",
     ["Existence and smoothness of Navier-Stokes solutions is a Millennium Prize problem", "Statistical theories (Kolmogorov) work in practice but lack rigorous foundation"],
     ["Navier-Stokes solutions remain globally smooth in 3D but with energy cascade statistics that are non-perturbatively controlled by a UV fixed point of the renormalisation group"]),

    ("u-random-matrix-universality", "Why does random matrix universality arise in systems as diverse as nuclear spectra, number theory zeros, and quantum chaos?",
     ["Universality classes established empirically across many systems", "The mathematical mechanism linking GOE/GUE statistics to physical chaos is poorly understood"],
     ["Quantum ergodicity of eigenstates is the necessary and sufficient condition for RMT level statistics, unifying all known universality instances"]),

    ("u-tropical-geometry-combinatorics", "What is the precise relationship between tropical geometry and the combinatorics of polytopes and matroids?",
     ["Tropical hyperplane arrangements correspond to subdivisions of polytopes", "Matroid theory connection to tropical geometry remains partially developed"],
     ["Every matroid has a canonical tropical linear space whose f-vector encodes all Whitney numbers and settles the conjecture of Dowling and Wilson"]),

    ("u-homotopy-type-theory-foundations", "Can homotopy type theory serve as a complete foundation for mathematics replacing ZFC set theory?",
     ["HoTT provides a foundation for homotopy theory but lacks a constructive large cardinal hierarchy", "Univalence axiom has no computational interpretation in all settings"],
     ["Cubical type theory with a universe hierarchy equivalent to ZFC with large cardinals provides a complete computable foundation for all current mathematics"]),

    ("u-motivic-cohomology-calculations", "Can motivic cohomology groups be computationally determined for all smooth projective varieties?",
     ["Voevodsky's motivic cohomology is defined but hard to compute", "Relationship to algebraic K-theory and étale cohomology is well-developed theoretically"],
     ["A spectral sequence relating motivic cohomology to étale and crystalline cohomology allows algorithmic computation for all varieties over finite and number fields"]),

    ("u-symplectic-capacities", "Are Ekeland-Hofer and Gromov-Witten symplectic capacities equal for all convex bodies?",
     ["Equality conjectured by Viterbo and proved in special cases", "General proof or counterexample would require new geometric measure theory"],
     ["Symplectic capacities of convex bodies are all equal and determined by the length of the shortest Reeb orbit on the boundary"]),

    ("u-pseudo-holomorphic-curve-counts", "What determines the well-definedness of pseudo-holomorphic curve counts in symplectic topology?",
     ["Gromov-Witten invariants require virtual perturbation theory to handle multiply-covered curves", "Polyfold and Kuranishi structure approaches compete without full consensus"],
     ["A canonical transversality perturbation using abstract simplicial techniques provides well-defined rational curve counts that are independent of all choices"]),

    ("u-derived-algebraic-geometry", "What are the fundamental obstructions to extending derived algebraic geometry to characteristic p arithmetic geometry?",
     ["Perfectoid techniques partially extend characteristic-0 derived geometry", "Prismatic cohomology provides new tools but a fully derived prismatic theory is incomplete"],
     ["A derived prismatic site construction provides the correct setting for an arithmetic derived algebraic geometry with functorial six-functor formalism"]),

    ("u-infinity-category-limits", "What are the fundamental completeness properties of infinity-categories and when do they have all small limits?",
     ["Lurie's Higher Topos Theory establishes many existence results", "Accessibility and presentability conditions are not fully transparent for algebraic applications"],
     ["Every locally presentable infinity-category is equivalent to a left exact localisation of a presheaf infinity-topos, providing complete limit-colimit calculus"]),

    ("u-constructive-incompleteness", "What is the constructive content of Godel incompleteness theorems and which unprovable statements have computational meaning?",
     ["Proof-theoretic ordinals characterise provability strength", "Computational interpretation of independence results is poorly understood"],
     ["Every Pi-0-2 statement independent of PA has a Turing degree that characterises its computational complexity, forming a hierarchy of unprovability"]),

    ("u-model-theory-arithmetic", "What model-theoretic properties distinguish the standard model of arithmetic from non-standard models?",
     ["Non-standard models satisfy the same first-order theory as the standard model", "Second-order categoricity requires second-order comprehension axioms"],
     ["The standard model is the unique model of arithmetic with a definable well-ordering in any extension of ZFC, characterising it up to isomorphism"]),

    ("u-descriptive-set-projective-hierarchy", "What are the full regularity properties (measurability, BP, PSP) of sets in the projective hierarchy?",
     ["L(R) determinacy implies regularity for all projective sets under large cardinal assumptions", "Constructible universe counterexamples exist without large cardinals"],
     ["All projective sets have the perfect set property, Lebesgue measurability, and Baire property if and only if Projective Determinacy holds"]),

    ("u-banach-space-geometry", "What is the geometry of the space of all Banach spaces under various equivalence relations on their structure?",
     ["Isomorphic classification of Banach spaces is far from complete", "Generic Banach spaces in the Baire-category sense have been studied but remain exotic"],
     ["The Banach-Mazur compactum is infinite-dimensional with no isolated points, and the generic Banach space contains all separable Banach spaces as subspaces"]),

    ("u-harmonic-analysis-sparse-recovery", "What are the sharp conditions for sparse signal recovery from harmonic measurements with minimal samples?",
     ["RIP conditions guarantee recovery but are NP-hard to verify", "Prony-type methods and super-resolution theory give partial answers"],
     ["Super-resolution from n Fourier samples achieves exact recovery of n-sparse signals supported on a grid when source separation exceeds 1/(2n)"]),

    ("u-quantum-group-representation", "What is the complete representation theory of quantum groups at roots of unity and its physical interpretation?",
     ["Tilting modules and quantum dimensions partially characterise representations", "Relation to logarithmic conformal field theory is conjectural"],
     ["Quantum groups at roots of unity have a semisimplification equivalent to a modular tensor category that classifies all rational 2D CFTs with the corresponding symmetry"]),
]

for slug, title, gaps, hyps in mathematics:
    path = os.path.join(BASE, "unknowns-catalog", "mathematics", f"{slug}.yaml")
    gaps_str = "\n".join(f'  - "{g}"' for g in gaps)
    hyps_str = "\n".join(f'  - "{h}"' for h in hyps)
    content = f"""id: {slug}
title: "{title}"
status: open
systematic_gaps:
{gaps_str}
suggested_hypotheses:
{hyps_str}
"""
    write(path, content)

print(f"Written {len(mathematics)} mathematics unknowns")

# ─────────────────────────────────────────────────────────────
# HYPOTHESES (10)
# ─────────────────────────────────────────────────────────────
hypotheses = [
    {
        "id": "h-magnetar-rapid-rotation-dynamo",
        "title": "Rapid proto-neutron star rotation during convective dynamo amplification generates extreme magnetic fields in magnetars when spin period at birth is less than 5 milliseconds",
        "status": "active",
        "priority": "high",
        "impact_score": 0.82,
        "created": "2026-05-05",
        "unknowns_addressed": ["u-magnetar-formation-mechanism"],
        "related_disciplines": ["astronomy", "physics"],
        "evidence_links": [
            {"type": "supporting", "confidence": 0.4, "arxiv": "1908.05664", "note": "Proto-neutron star magnetic field amplification via convective dynamo (metadata only)"},
            {"type": "related", "url": "https://www.nature.com/articles/nature07317", "note": "Magnetar field constraints from X-ray timing (metadata link only)"},
            {"type": "contradicting", "confidence": 0.25, "note": "Population synthesis suggests most magnetars born at slower rotation rates"},
        ],
        "proposed_tests": [
            {"summary": "Measure initial spin period distribution of magnetars from young SNR associations and test correlation with field strength"},
            {"summary": "MHD simulations of proto-neutron star convection varying initial rotation rate to identify critical spin threshold for dynamo saturation"},
        ],
    },
    {
        "id": "h-amoc-saddle-node-bifurcation",
        "title": "AMOC crosses a saddle-node bifurcation at sustained Greenland melt rates exceeding 0.3 Sv, leading to irreversible collapse achievable under high-emission scenarios by 2100",
        "status": "active",
        "priority": "critical",
        "impact_score": 0.92,
        "created": "2026-05-05",
        "unknowns_addressed": ["u-amoc-collapse-threshold"],
        "related_disciplines": ["climate-science", "physics", "oceanography"],
        "evidence_links": [
            {"type": "supporting", "confidence": 0.35, "note": "Box model and CMIP6 models show AMOC bistability under freshwater hosing"},
            {"type": "related", "url": "https://www.science.org/doi/10.1126/science.abn7950", "note": "Early warning signals in AMOC fingerprints (metadata link only)"},
            {"type": "contradicting", "confidence": 0.3, "note": "Higher-resolution models show weaker bistability due to eddy mixing"},
        ],
        "proposed_tests": [
            {"summary": "Hosing experiments in eddy-resolving ocean models with calibrated Greenland melt rates to determine bistability in high-resolution settings"},
            {"summary": "Observational RAPID array analysis for early-warning statistical signals (variance, autocorrelation) preceding AMOC weakening"},
        ],
    },
    {
        "id": "h-soluble-amyloid-oligomers-synaptic",
        "title": "Soluble amyloid beta oligomers rather than insoluble plaques are the primary drivers of synaptic dysfunction in Alzheimer's disease, explaining why plaque clearance does not consistently improve cognition",
        "status": "active",
        "priority": "critical",
        "impact_score": 0.88,
        "created": "2026-05-05",
        "unknowns_addressed": ["u-alzheimer-causal-biomarkers"],
        "related_disciplines": ["medicine", "neuroscience"],
        "evidence_links": [
            {"type": "supporting", "confidence": 0.55, "url": "https://www.nature.com/articles/s41593-018-0230-9", "note": "Synaptic toxicity of Abeta oligomers in cell and animal models (metadata link only)"},
            {"type": "related", "note": "Lecanemab trial shows cognitive benefit proportional to oligomer clearance rather than plaque reduction"},
            {"type": "contradicting", "confidence": 0.2, "note": "DIAN-TU trial plaque clearance data does not show consistent oligomer-specific effect"},
        ],
        "proposed_tests": [
            {"summary": "Develop oligomer-selective immunotherapy and compare cognitive outcome to plaque-targeting therapy in matched patient cohorts"},
            {"summary": "CSF oligomer concentration time-series in MCI patients correlated with synaptic loss markers and cognitive trajectory"},
        ],
    },
    {
        "id": "h-permafrost-carbon-tipping-2point5",
        "title": "A 2.5 degree Celsius global mean warming threshold triggers irreversible permafrost degradation releasing over 200 Gt of carbon by 2200 in a self-sustaining feedback",
        "status": "active",
        "priority": "critical",
        "impact_score": 0.90,
        "created": "2026-05-05",
        "unknowns_addressed": ["u-permafrost-tipping-point"],
        "related_disciplines": ["climate-science", "ecology"],
        "evidence_links": [
            {"type": "supporting", "confidence": 0.3, "note": "Earth system models show permafrost carbon feedback acceleration above 2C"},
            {"type": "related", "url": "https://www.nature.com/articles/nature14338", "note": "Permafrost carbon pool and vulnerability assessment (metadata link only)"},
            {"type": "contradicting", "confidence": 0.25, "note": "Model uncertainty in talik formation rates spans an order of magnitude"},
        ],
        "proposed_tests": [
            {"summary": "Synthesise observational talik depth and carbon flux data from the pan-Arctic to constrain permafrost vulnerability model parameters"},
            {"summary": "Isotopic partitioning of Arctic CO2 and CH4 fluxes to separate permafrost from vegetation and thermokarst lake contributions"},
        ],
    },
    {
        "id": "h-gut-microbiome-serotonin-depression",
        "title": "Specific short-chain fatty acid producing gut bacteria modulate tryptophan availability to the brain and causally influence depression susceptibility via the gut-brain axis",
        "status": "active",
        "priority": "high",
        "impact_score": 0.77,
        "created": "2026-05-05",
        "unknowns_addressed": ["u-microbiome-mental-health"],
        "related_disciplines": ["medicine", "neuroscience", "microbiology"],
        "evidence_links": [
            {"type": "supporting", "confidence": 0.35, "url": "https://www.nature.com/articles/s41591-019-0675-0", "note": "Gut microbiome composition differences in depression cohorts (metadata link only)"},
            {"type": "supporting", "confidence": 0.3, "note": "Germ-free mouse behavioural deficits rescued by butyrate supplementation"},
            {"type": "contradicting", "confidence": 0.3, "note": "Human probiotic RCTs for depression show inconsistent effects"},
        ],
        "proposed_tests": [
            {"summary": "Mendelian randomisation analysis using microbiome QTLs as instruments for depression outcomes in UK Biobank"},
            {"summary": "Controlled dietary intervention (high-fiber vs low-fiber) with paired plasma tryptophan, fecal SCFA, and depression symptom measurements"},
        ],
    },
    {
        "id": "h-sei-organic-inorganic-layers",
        "title": "The organic outer and inorganic inner SEI layers transport lithium ions via distinct mechanisms whose relative thickness and conductance ratio determines battery cycle life",
        "status": "active",
        "priority": "high",
        "impact_score": 0.79,
        "created": "2026-05-05",
        "unknowns_addressed": ["u-solid-electrolyte-interface"],
        "related_disciplines": ["materials-science", "chemistry"],
        "evidence_links": [
            {"type": "supporting", "confidence": 0.45, "note": "Cryo-TEM reveals nanoscale layered SEI structure in cycled Li-metal cells"},
            {"type": "related", "arxiv": "2301.05478", "note": "First-principles calculation of SEI Li+ transport pathways (metadata only)"},
            {"type": "contradicting", "confidence": 0.2, "note": "Some cryogenic studies show amorphous rather than layered SEI structure"},
        ],
        "proposed_tests": [
            {"summary": "Atom probe tomography of SEI from cells with varying electrolyte formulations to correlate layer composition with cycle life"},
            {"summary": "Electrochemical impedance spectroscopy with equivalent circuit models distinguishing organic and inorganic SEI transport contributions"},
        ],
    },
    {
        "id": "h-recurrent-processing-consciousness",
        "title": "Recurrent processing in higher cortical areas is necessary and sufficient for phenomenal consciousness, and feedforward-only processing generates no subjective experience",
        "status": "active",
        "priority": "high",
        "impact_score": 0.85,
        "created": "2026-05-05",
        "unknowns_addressed": ["u-hard-problem-consciousness"],
        "related_disciplines": ["cognitive-science", "neuroscience"],
        "evidence_links": [
            {"type": "supporting", "confidence": 0.4, "url": "https://www.nature.com/articles/s41583-021-00490-4", "note": "Recurrent processing theory review and evidence synthesis (metadata link only)"},
            {"type": "related", "note": "TMS suppression of occipital feedback abolishes visual awareness without affecting early evoked responses"},
            {"type": "contradicting", "confidence": 0.35, "note": "Some masking paradigms suggest feedforward processing can support brief awareness"},
        ],
        "proposed_tests": [
            {"summary": "High-density ECoG recordings during anesthesia induction to identify when recurrent vs feedforward processing decouples from consciousness"},
            {"summary": "Optogenetic suppression of feedback projections in non-human primates during visual detection tasks"},
        ],
    },
    {
        "id": "h-jwst-pop3-lensing-detection",
        "title": "JWST can detect individual gravitationally lensed Population III stars in magnification events during the epoch of reionisation at redshifts 10-15",
        "status": "active",
        "priority": "medium",
        "impact_score": 0.72,
        "created": "2026-05-05",
        "unknowns_addressed": ["u-population-iii-stars"],
        "related_disciplines": ["astronomy"],
        "evidence_links": [
            {"type": "supporting", "confidence": 0.35, "arxiv": "2208.01612", "note": "Sensitivity estimates for JWST detection of lensed Pop III stars (metadata only)"},
            {"type": "related", "note": "Earendel star detected by HST demonstrates stellar caustic crossing magnification at z>6"},
            {"type": "contradicting", "confidence": 0.2, "note": "Pop III luminosity function uncertainties span several orders of magnitude"},
        ],
        "proposed_tests": [
            {"summary": "JWST Cycle 3 monitoring of known cluster lenses for transient point sources at z>10 with UV-bright spectral energy distributions"},
            {"summary": "Statistical analysis of transient rate in high-magnification arcs to constrain Pop III stellar mass function"},
        ],
    },
    {
        "id": "h-early-dark-energy-hubble-tension",
        "title": "Early dark energy that decays before recombination reduces the sound horizon and reconciles CMB-inferred H0 with local distance ladder measurements without introducing new tensions",
        "status": "active",
        "priority": "high",
        "impact_score": 0.83,
        "created": "2026-05-05",
        "unknowns_addressed": ["u-hubble-tension-origin"],
        "related_disciplines": ["astronomy", "physics"],
        "evidence_links": [
            {"type": "supporting", "confidence": 0.3, "arxiv": "1907.10625", "note": "Early dark energy model fitting CMB, BAO, and local H0 data (metadata only)"},
            {"type": "contradicting", "confidence": 0.4, "note": "CMB lensing and large-scale structure constraints disfavour most EDE models"},
            {"type": "related", "url": "https://www.nature.com/articles/s41550-021-01319-7", "note": "Review of Hubble tension and proposed solutions (metadata link only)"},
        ],
        "proposed_tests": [
            {"summary": "CMB-S4 and Simons Observatory power spectrum measurements to constrain EDE energy injection fraction below 5%"},
            {"summary": "Cross-correlation of CMB lensing with DESI galaxy clustering to break degeneracy between EDE and matter power spectrum amplitude"},
        ],
    },
    {
        "id": "h-microglial-synaptic-pruning-depression",
        "title": "Microglia-mediated excess synaptic pruning in the prefrontal cortex is a causal mechanism in treatment-resistant depression that is partially reversible by anti-inflammatory intervention",
        "status": "active",
        "priority": "high",
        "impact_score": 0.80,
        "created": "2026-05-05",
        "unknowns_addressed": ["u-neuroinflammation-psychiatric"],
        "related_disciplines": ["medicine", "neuroscience"],
        "evidence_links": [
            {"type": "supporting", "confidence": 0.35, "note": "PET imaging shows elevated microglial activation in treatment-resistant depression"},
            {"type": "supporting", "confidence": 0.3, "url": "https://www.cell.com/neuron/fulltext/S0896-6273(16)30759-9", "note": "Complement-mediated synapse elimination by microglia (metadata link only)"},
            {"type": "contradicting", "confidence": 0.25, "note": "Anti-inflammatory trial results in depression have been inconsistent across studies"},
        ],
        "proposed_tests": [
            {"summary": "CSF complement and synaptic protein biomarker panel in treatment-resistant vs treatment-responsive depression correlated with anti-inflammatory treatment response"},
            {"summary": "Post-mortem PFC synapse density quantification stratified by CRP and microglial activation markers"},
        ],
    },
]

for hyp in hypotheses:
    slug = hyp["id"]
    path = os.path.join(BASE, "hypotheses", "active", f"{slug}.yaml")
    ev_lines = []
    for ev in hyp.get("evidence_links", []):
        ev_lines.append("  - type: " + ev["type"])
        if "confidence" in ev:
            ev_lines.append(f"    confidence: {ev['confidence']}")
        if "doi" in ev:
            ev_lines.append(f'    doi: "{ev["doi"]}"')
        if "arxiv" in ev:
            ev_lines.append(f'    arxiv: "{ev["arxiv"]}"')
        if "url" in ev:
            ev_lines.append(f'    url: {ev["url"]}')
        if "note" in ev:
            ev_lines.append(f'    note: "{ev["note"]}"')
    tests_lines = []
    for t in hyp.get("proposed_tests", []):
        tests_lines.append(f'  - summary: >-\n      {t["summary"]}')
    unknowns_lines = "\n".join(f"  - {u}" for u in hyp.get("unknowns_addressed", []))
    disciplines_lines = "\n".join(f"  - {d}" for d in hyp.get("related_disciplines", []))

    content = f"""id: {hyp['id']}
title: "{hyp['title']}"
status: {hyp['status']}
priority: {hyp['priority']}
impact_score: {hyp['impact_score']}
created: "{hyp['created']}"
author: "USDR seed content (replace with GitHub handle when stewarded)"
unknowns_addressed:
{unknowns_lines}
related_disciplines:
{disciplines_lines}
evidence_links:
{chr(10).join(ev_lines)}
proposed_tests:
{chr(10).join(tests_lines)}
"""
    write(path, content)

print(f"Written {len(hypotheses)} hypotheses")

# ─────────────────────────────────────────────────────────────
# BRIDGES (2)
# ─────────────────────────────────────────────────────────────

bridge37 = """id: b-climate-tipping-percolation
title: "Tipping points in Earth's climate system are mathematically equivalent to percolation phase transitions in disordered networks"
status: proposed
fields:
  - climate-science
  - statistical-physics
  - mathematics
bridge_claim: >
  Climate tipping elements (AMOC, permafrost, ice sheets) exhibit saddle-node bifurcations
  whose mathematical structure is identical to the second-order phase transition in percolation
  theory on heterogeneous networks. The critical forcing threshold maps to the percolation
  threshold p_c, and the power-law scaling of early warning signals near the tipping point
  mirrors correlation length divergence near p_c. This mapping is non-trivial because it
  implies that network topology of Earth system interactions determines which tipping cascades
  are possible in analogy to how network degree distribution determines percolation critical exponents.
translation_table:
  - field_a_term: "climate tipping element"
    field_b_term: "percolation cluster"
    note: "Each tipping element is a node; coupling between elements is an edge with weight proportional to teleconnection strength"
  - field_a_term: "critical forcing threshold"
    field_b_term: "percolation threshold p_c"
    note: "Both mark the transition from isolated change to system-wide cascade"
  - field_a_term: "tipping cascade"
    field_b_term: "giant connected component formation"
    note: "A cascade of tipping elements is analogous to the formation of the giant percolation cluster above p_c"
  - field_a_term: "early warning signals (variance, autocorrelation)"
    field_b_term: "diverging correlation length near critical point"
    note: "Critical slowing down near tipping points corresponds to correlation length divergence in percolation"
related_unknowns:
  - u-permafrost-tipping-point
  - u-amoc-collapse-threshold
  - u-abrupt-climate-transitions
cross_pollination_opportunities:
  - "Apply percolation-based graph fragility analysis to Earth system interaction networks to identify which tipping elements are most dangerous to destabilise"
  - "Use percolation universality classes to predict scaling of tipping cascade size with coupling strength, testable in paleoclimate records"
  - "Transfer climate model early warning signal methodology to network percolation experiments in the laboratory"
communication_gap: >
  Climate scientists use dynamical systems theory (bifurcation analysis) while statistical physicists
  use percolation and field theory. The communities publish in different journals and attend different
  conferences. The mathematical equivalence is recognised by a small number of complexity scientists
  but has not been systematically exploited.
last_reviewed: "2026-05-05"
"""

bridge38 = """id: b-materials-consciousness-criticality
title: "Phase transitions near the critical point in disordered materials and the neural dynamics associated with consciousness share mathematical structure through self-organised criticality"
status: proposed
fields:
  - materials-science
  - cognitive-science
  - statistical-physics
bridge_claim: >
  Self-organised criticality (SOC) in neural networks, proposed as a substrate for
  consciousness and optimal information processing, shares its mathematical formalism
  with critical phenomena in disordered materials systems such as amorphous metals
  and spin glasses. In both cases, the system self-tunes to a critical manifold where
  correlation lengths diverge and scale-free dynamics emerge. The Lyapunov exponent
  spectrum, avalanche statistics, and 1/f noise signatures are identical in both
  physical and neural SOC systems. This non-trivial mapping suggests that experimental
  tools from materials physics (neutron scattering, dielectric spectroscopy) could
  be adapted to measure criticality in neural tissue.
translation_table:
  - field_a_term: "spin glass order parameter"
    field_b_term: "neural synchrony order parameter"
    note: "Edwards-Anderson order parameter in spin glasses maps to the global synchronisation measure in neural field theories"
  - field_a_term: "avalanche size distribution in sandpile"
    field_b_term: "neural avalanche power law"
    note: "Both follow P(s) ~ s^-3/2 consistent with mean-field branching process criticality"
  - field_a_term: "Griffiths phase in disordered magnets"
    field_b_term: "Griffiths phase in heterogeneous neural networks"
    note: "Network heterogeneity extends the critical region in both systems, potentially explaining robustness of neural criticality"
related_unknowns:
  - u-hard-problem-consciousness
  - u-amorphous-metal-magnetism
related_hypotheses:
  - h-recurrent-processing-consciousness
cross_pollination_opportunities:
  - "Apply replica symmetry breaking mathematics from spin glasses to model consciousness transitions under anaesthesia"
  - "Use neutron spin echo spectroscopy protocols adapted for MEG/EEG to measure neural correlation length divergence"
  - "Test whether Griffiths phase mathematics explains the robustness of conscious states to focal brain lesions"
communication_gap: >
  Materials scientists working on disordered systems and neuroscientists studying criticality
  both use SOC language but attend entirely separate conferences. No active collaboration
  between condensed matter physics groups and neuroscience criticality groups has resulted
  in mutual methodological transfer.
last_reviewed: "2026-05-05"
"""

write(os.path.join(BASE, "cross-domain", "physics-climate", "b-climate-tipping-percolation.yaml"), bridge37)
write(os.path.join(BASE, "cross-domain", "physics-neuroscience", "b-materials-consciousness-criticality.yaml"), bridge38)
print("Written 2 bridges")

# ─────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────
total_new = len(materials) + len(climate) + len(astronomy) + len(medicine) + len(cognitive) + len(mathematics) + len(hypotheses) + 2
print(f"\nTotal new entries written: {total_new}")
print(f"  Materials science unknowns: {len(materials)}")
print(f"  Climate science unknowns:   {len(climate)}")
print(f"  Astronomy unknowns:         {len(astronomy)}")
print(f"  Medicine unknowns:          {len(medicine)}")
print(f"  Cognitive science unknowns: {len(cognitive)}")
print(f"  Mathematics unknowns:       {len(mathematics)}")
print(f"  Hypotheses:                 {len(hypotheses)}")
print(f"  Bridges:                    2")
