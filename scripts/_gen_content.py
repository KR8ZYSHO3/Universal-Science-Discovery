"""Script to generate new content files for the Phase 0 500+ target."""
import os

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Created: {os.path.basename(path)}')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ────────────────────────────────────────────────────────────────
# 1. QUANTUM-PHYSICS (25 unknowns)
# ────────────────────────────────────────────────────────────────
QP = os.path.join(BASE, 'unknowns-catalog', 'quantum-physics')

quantum_files = {
'u-quantum-gravity-unification.yaml': """id: u-quantum-gravity-unification
title: What is the correct theory unifying quantum mechanics and general relativity, and what are its experimentally distinguishable predictions?
status: open
priority: high
disciplines:
  - quantum-gravity
  - theoretical-physics
  - cosmology
summary: >
  Loop quantum gravity, string theory, and causal dynamical triangulations each offer
  candidate frameworks for quantum gravity, yet none has produced a confirmed
  experimental prediction. The Planck scale (10^-35 m) is inaccessible to direct
  probing; candidate signatures include Lorentz invariance violation in gamma-ray
  bursts, primordial gravitational wave polarisation, and quantum foam effects on
  photon propagation. No consensus exists on which candidate theory is closest to
  correct or what experiment could discriminate between them.
systematic_gaps:
  - No experimental signature of quantum gravity has been confirmed.
  - The renormalisability of gravity as a quantum field theory remains unresolved beyond effective field theory.
  - String theory landscape has ~10^500 vacua with no selection principle.
last_reviewed: "2026-05-05"
""",

'u-measurement-problem-interpretation.yaml': """id: u-measurement-problem-interpretation
title: What physical process constitutes quantum measurement, and which interpretation of quantum mechanics is empirically correct?
status: open
priority: high
disciplines:
  - quantum-foundations
  - quantum-mechanics
  - philosophy-of-physics
summary: >
  The measurement problem remains unresolved after a century. Competing interpretations
  (Copenhagen, many-worlds, pilot wave, relational, QBism, objective collapse) agree on
  all standard predictions but differ on ontology. Proposed experimental discriminators
  include Leggett-Garg inequality violations, objective collapse via gravitational
  decoherence (Penrose-Diosi), and interference of large molecules.
systematic_gaps:
  - Objective collapse theories make predictions quantitatively different from standard QM but experiments are not yet sensitive enough.
  - Many-worlds interpretation has no agreed measure for probability.
  - Decoherence explains why interference is not observed but does not explain why only one outcome is experienced.
last_reviewed: "2026-05-05"
""",

'u-decoherence-timescales-warm-systems.yaml': """id: u-decoherence-timescales-warm-systems
title: What determines quantum decoherence timescales in warm, wet biological systems, and can coherence survive long enough to be functionally relevant?
status: open
priority: high
disciplines:
  - quantum-biology
  - quantum-mechanics
  - biophysics
summary: >
  Quantum coherence in photosynthesis, avian magnetoreception, and enzyme tunnelling
  is hotly debated. Femtosecond spectroscopy reveals long-lived coherences in
  light-harvesting complexes, but whether these are quantum or vibrationally assisted
  classical oscillations is disputed. Warm, wet environments couple quantum systems to
  thermal baths that should cause rapid decoherence.
systematic_gaps:
  - Distinguishing quantum from vibronic coherence in 2D spectroscopy is technically difficult and disputed.
  - No causal experiment has shown that disrupting quantum coherence degrades biological function.
  - Theoretical models of decoherence in structured protein environments do not agree on coherence timescales.
last_reviewed: "2026-05-05"
""",

'u-quantum-advantage-classical-boundary.yaml': """id: u-quantum-advantage-classical-boundary
title: For which computational problems does quantum hardware achieve asymptotic speedup that is robust to realistic noise and classical simulation advances?
status: open
priority: high
disciplines:
  - quantum-computing
  - computational-complexity
  - algorithms
summary: >
  Claims of quantum advantage have been challenged by improved classical simulation
  algorithms that narrow or close claimed gaps. The boundary between problems where
  quantum computers provide robust asymptotic advantage versus classical alternatives
  is poorly understood. Shor factoring and Grover search provide provable speedups but
  require fault-tolerant hardware far beyond current capability.
systematic_gaps:
  - No NISQ device has demonstrated quantum advantage on a practically useful problem that classical computers cannot simulate.
  - The classical simulation complexity of random circuit sampling has not been formally resolved.
  - Variational quantum algorithms have not demonstrated quantum speedup on chemistry or optimisation instances.
last_reviewed: "2026-05-05"
""",

'u-topological-qc-fault-tolerance-threshold.yaml': """id: u-topological-qc-fault-tolerance-threshold
title: Can topological quantum error correction achieve fault-tolerant thresholds in physical systems, and what are the minimum hardware requirements?
status: open
priority: high
disciplines:
  - quantum-computing
  - condensed-matter-physics
  - quantum-error-correction
summary: >
  Topological quantum computing using anyons offers inherent protection from local noise.
  Despite investment in Majorana-based qubits, the claimed detection of Majorana zero
  modes was retracted in 2021. Topological qubits have not yet achieved gate fidelities
  necessary to demonstrate threshold crossing.
systematic_gaps:
  - Definitive experimental observation of non-Abelian anyons remains contested.
  - Surface code requires thousands of physical qubits per logical qubit; topological protection may not reduce overhead sufficiently.
  - Decoherence mechanisms specific to Majorana devices are not fully characterised.
last_reviewed: "2026-05-05"
""",

'u-quantum-error-correction-overhead.yaml': """id: u-quantum-error-correction-overhead
title: What is the minimum physical-to-logical qubit overhead required for fault-tolerant quantum computing, and can it be reduced below current theoretical estimates?
status: open
priority: medium
disciplines:
  - quantum-error-correction
  - quantum-computing
  - information-theory
summary: >
  Current estimates for fault-tolerant quantum computing require thousands to millions
  of physical qubits per logical qubit. Recent advances in LDPC codes promise
  dramatically lower overhead, but the resource requirements for practical quantum
  advantage remain enormous.
systematic_gaps:
  - The minimum achievable physical-to-logical qubit ratio has no tight lower bound.
  - Concatenated codes, surface codes, and LDPC codes have different tradeoffs not yet achievable in hardware.
  - Magic state distillation overhead for universal quantum computation remains a significant resource bottleneck.
last_reviewed: "2026-05-05"
""",

'u-many-worlds-copenhagen-experimental.yaml': """id: u-many-worlds-copenhagen-experimental
title: Is there any experiment that could empirically distinguish many-worlds from Copenhagen or other single-outcome interpretations of quantum mechanics?
status: open
priority: medium
disciplines:
  - quantum-foundations
  - quantum-mechanics
  - philosophy-of-physics
summary: >
  Both many-worlds and Copenhagen reproduce identical predictions for all standard
  quantum experiments. Some theorists argue that interference between branches could
  in principle distinguish MWI, but such interference would require reversing
  decoherence across macroscopic systems. Proposed discriminators via Wigner's friend
  scenarios show interpretational conflicts but not falsifiable differences.
systematic_gaps:
  - No agreed operationalisation of what constitutes a "world" in MWI makes experimental test design impossible.
  - Frauchiger-Renner thought experiment reveals logical consistency issues but does not distinguish interpretations empirically.
  - Wigner's friend realisations with quantum agents remain beyond current technology.
last_reviewed: "2026-05-05"
""",

'u-quantum-darwinism-evidence.yaml': """id: u-quantum-darwinism-evidence
title: Does quantum Darwinism explain the emergence of classical objectivity from quantum mechanics, and what experimental evidence would confirm it?
status: open
priority: medium
disciplines:
  - quantum-foundations
  - quantum-mechanics
  - quantum-information
summary: >
  Quantum Darwinism proposes that classical reality emerges because information about
  preferred pointer states proliferates into the environment. Recent experiments in
  photonic systems have provided partial evidence for redundant encoding, but the
  conditions under which quantum Darwinism applies versus other decoherence frameworks
  remain disputed.
systematic_gaps:
  - Pointer states predicted by quantum Darwinism and those from decoherence alone are difficult to distinguish experimentally.
  - The quantum-to-classical transition timescale as a function of system-environment coupling has not been measured systematically.
  - Quantum Darwinism in interacting non-Markovian environments is not well understood theoretically.
last_reviewed: "2026-05-05"
""",

'u-bell-loophole-free-implications.yaml': """id: u-bell-loophole-free-implications
title: What are the full physical implications of loophole-free Bell inequality violations, and do they definitively rule out all local hidden variable theories?
status: open
priority: medium
disciplines:
  - quantum-foundations
  - quantum-mechanics
  - quantum-information
summary: >
  Loophole-free Bell tests (Hensen et al. 2015, Giustina et al. 2015) closed the
  detection and locality loopholes, confirming no local hidden variable theory can
  reproduce quantum correlations. However, the freedom-of-choice (superdeterminism)
  loophole remains open.
systematic_gaps:
  - Superdeterminism cannot be ruled out in principle; quantitative constraints on fine-tuning required are weak.
  - Non-local hidden variable theories (Bohmian mechanics) remain consistent with all Bell test results.
  - The transition from fundamental nonlocality to practical quantum cryptography security proofs requires additional assumptions.
last_reviewed: "2026-05-05"
""",

'u-quantum-memory-coherence-limits.yaml': """id: u-quantum-memory-coherence-limits
title: What are the fundamental limits on quantum memory coherence times in solid-state, atomic, and photonic systems, and how close are current implementations?
status: open
priority: medium
disciplines:
  - quantum-computing
  - quantum-information
  - atomic-physics
summary: >
  Quantum memories span microseconds to hours in coherence time depending on platform.
  The fundamental limits imposed by phonon coupling, magnetic noise, and radiative decay
  are not saturated in most systems. The gap between achieved and fundamental coherence
  times varies from 1x to 10^6x depending on the platform.
systematic_gaps:
  - Which decoherence mechanism dominates in each platform has not been definitively established.
  - Dynamic decoupling approaching the fundamental coherence limit has only been demonstrated in a few systems.
  - The tradeoff between coherence time and coupling efficiency is poorly characterised.
last_reviewed: "2026-05-05"
""",

'u-photonic-qc-scalability.yaml': """id: u-photonic-qc-scalability
title: Can photonic quantum computing achieve fault-tolerant scalability given current photon loss rates and deterministic gate requirements?
status: open
priority: medium
disciplines:
  - quantum-computing
  - quantum-optics
  - photonics
summary: >
  Photonic quantum computing avoids cryogenic requirements but faces fundamental
  challenges: weak photon-photon interactions, photon loss destroying quantum
  information, and imperfect deterministic single-photon sources. Fault-tolerant
  photonic computing requires photon loss rates below ~1% per gate, not yet achieved
  with scalable integrated photonics.
systematic_gaps:
  - Integrated photonic circuits achieving less than 1 percent loss per component at scale have not been demonstrated.
  - Deterministic single-photon sources with more than 99.9 percent efficiency and indistinguishability are not yet available.
  - The resource overhead of fusion-based quantum computing has not been validated experimentally.
last_reviewed: "2026-05-05"
""",

'u-neutral-atom-qubit-fidelity.yaml': """id: u-neutral-atom-qubit-fidelity
title: What limits neutral atom qubit gate fidelities, and can they reach the error thresholds required for fault-tolerant quantum computing?
status: open
priority: medium
disciplines:
  - quantum-computing
  - atomic-physics
  - quantum-information
summary: >
  Neutral atom arrays have emerged as a leading quantum computing platform, with 2D
  arrays of hundreds of qubits demonstrated. Two-qubit gate fidelities via Rydberg
  interactions reach 99.5 percent, approaching the fault-tolerance threshold. Key
  questions involve dominant error sources and whether mid-circuit measurements can
  achieve the speed required for real-time error correction.
systematic_gaps:
  - Rydberg excitation crosstalk and leakage to unintended states limits gate fidelity and has not been fully characterised at scale.
  - Mid-circuit measurement fidelity and speed do not yet meet error correction requirements.
  - Clock qubit coherence during atom shuttling degrades in ways not fully modelled.
last_reviewed: "2026-05-05"
""",

'u-quantum-repeater-distance-limit.yaml': """id: u-quantum-repeater-distance-limit
title: What is the maximum distance over which quantum entanglement can be distributed using quantum repeaters, and what are the fundamental rate-distance tradeoffs?
status: open
priority: medium
disciplines:
  - quantum-networks
  - quantum-information
  - quantum-optics
summary: >
  Quantum repeaters overcome photon loss in optical fibre to enable long-distance
  quantum communication. Satellite-based QKD demonstrated entanglement distribution
  over 1200 km but with very low key rates. No quantum repeater has yet outperformed
  direct transmission for any distance.
systematic_gaps:
  - No quantum repeater has demonstrated repeater-assisted entanglement distribution with higher rate than direct transmission.
  - Quantum memories with sufficiently long coherence time and high coupling efficiency for repeater operation have not been co-integrated.
  - Multi-node repeater chains with entanglement swapping have only been demonstrated with two nodes.
last_reviewed: "2026-05-05"
""",

'u-quantum-sensing-biological-limits.yaml': """id: u-quantum-sensing-biological-limits
title: Can quantum sensing technologies achieve the sensitivity required to probe biological processes at the single-molecule level in living systems?
status: open
priority: medium
disciplines:
  - quantum-sensing
  - biophysics
  - quantum-metrology
summary: >
  NV centres in diamond offer nanoscale magnetic field sensing at room temperature.
  Current NV sensors achieve ~100 nT per Hz^0.5 sensitivity, insufficient for single
  action potential magnetic fields (~100 pT). The gap between current sensitivity
  and biologically relevant thresholds spans ~3 orders of magnitude.
systematic_gaps:
  - Achieving Heisenberg-limited sensitivity in solid-state sensors at room temperature in the presence of biological noise has not been demonstrated.
  - Spin squeezing beyond the standard quantum limit in NV centre ensembles has not been demonstrated in nanoscale volumes.
  - Biocompatibility of diamond nanoparticles for in-vivo sensing is poorly characterised.
last_reviewed: "2026-05-05"
""",

'u-quantum-thermodynamics-arrow.yaml': """id: u-quantum-thermodynamics-arrow
title: Does quantum thermodynamics provide a microscopic derivation of the second law, and does quantum coherence generate or suppress thermodynamic irreversibility?
status: open
priority: medium
disciplines:
  - quantum-thermodynamics
  - statistical-mechanics
  - quantum-information
summary: >
  Quantum thermodynamics extends classical thermodynamics to systems where coherence,
  entanglement, and measurement play active roles. Whether quantum coherence enhances
  thermodynamic efficiency beyond classical bounds remains disputed. The quantum origin
  of the thermodynamic arrow of time is not resolved.
systematic_gaps:
  - Whether quantum coherence provides thermodynamic advantage beyond classical stochastic engines is not settled theoretically or experimentally.
  - Landauer principle at the quantum limit has been partially tested but not at the coherence-relevant regime.
  - The connection between quantum scrambling and thermodynamic entropy production lacks experimental validation.
last_reviewed: "2026-05-05"
""",

'u-quantum-chaos-scrambling-rates.yaml': """id: u-quantum-chaos-scrambling-rates
title: What determines quantum information scrambling rates in chaotic systems, and does the Maldacena-Shenker-Stanford bound saturate in black holes and quantum matter?
status: open
priority: medium
disciplines:
  - quantum-chaos
  - quantum-gravity
  - condensed-matter-physics
summary: >
  Quantum chaos is characterised by rapid information scrambling measured by
  out-of-time-order correlators. The MSS bound conjectures the Lyapunov exponent
  lambda is at most 2 pi kT/hbar, with black holes saturating this bound. Whether
  any condensed matter system truly saturates the MSS bound remains contested.
systematic_gaps:
  - OTOC measurements in condensed matter systems are difficult; no clean saturation of MSS bound has been demonstrated experimentally.
  - The connection between scrambling rates in quantum processors and thermodynamic properties of black holes remains speculative.
  - Whether linear-T resistivity in strange metals implies MSS-saturating scrambling is not established.
last_reviewed: "2026-05-05"
""",

'u-entanglement-entropy-area-law-exceptions.yaml': """id: u-entanglement-entropy-area-law-exceptions
title: What are the conditions under which quantum systems violate the entanglement entropy area law, and what do violations imply for classical simulability?
status: open
priority: medium
disciplines:
  - quantum-information
  - condensed-matter-physics
  - quantum-computing
summary: >
  The area law for entanglement entropy states that ground states of local gapped
  Hamiltonians have entanglement entropy scaling with boundary area, not volume.
  Violations occur at quantum critical points and in topological phases. Understanding
  when area law holds determines the boundary of classical simulation efficiency.
systematic_gaps:
  - A complete classification of which Hamiltonians satisfy area law in 2D and higher dimensions does not exist.
  - The relationship between area-law violations at excited states and thermal phase transitions is not fully understood.
  - No algorithm exploits area-law-adjacent structure for general 2D quantum systems as efficiently as DMRG does in 1D.
last_reviewed: "2026-05-05"
""",

'u-quantum-simulation-classical-hardness.yaml': """id: u-quantum-simulation-classical-hardness
title: For which quantum systems is classical simulation provably hard, and where does the quantum-classical hardness boundary lie in practice?
status: open
priority: medium
disciplines:
  - quantum-computing
  - computational-physics
  - quantum-chemistry
summary: >
  Quantum simulation of fermionic systems is believed classically hard in the worst
  case, but the average-case complexity for physically relevant instances is unclear.
  Variational methods, neural network quantum states, and tensor networks continue to
  push the boundary of simulable system sizes.
systematic_gaps:
  - Worst-case hardness proofs for quantum simulation do not imply typical-case hardness for specific Hamiltonians of interest.
  - Classical algorithms continue to push the boundary of simulable system sizes; the moving frontier is not tracked systematically.
  - Proof of classical hardness for the Fermi-Hubbard model at intermediate coupling remains open.
last_reviewed: "2026-05-05"
""",

'u-quantum-speedup-optimization-np.yaml': """id: u-quantum-speedup-optimization-np
title: Can quantum algorithms provide polynomial or superpolynomial speedups for NP-hard combinatorial optimisation problems?
status: open
priority: high
disciplines:
  - quantum-computing
  - computational-complexity
  - algorithms
summary: >
  Quantum annealing and QAOA are proposed approaches for NP-hard combinatorial
  problems. No quantum algorithm has demonstrated proven speedup over state-of-the-art
  classical algorithms for any NP-hard problem on instances of practical size.
systematic_gaps:
  - QAOA requires circuit depth exponential in problem size for near-optimal solutions on hard instances.
  - Quantum annealing on D-Wave hardware has not demonstrated speedup over simulated annealing on any tested problem class.
  - Complexity-theoretic barriers prevent quantum computers from solving NP-complete problems in polynomial time.
last_reviewed: "2026-05-05"
""",

'u-quantum-annealing-qaoa-comparison.yaml': """id: u-quantum-annealing-qaoa-comparison
title: Under what conditions does quantum annealing outperform QAOA or classical optimisation methods for structured combinatorial problems?
status: open
priority: medium
disciplines:
  - quantum-computing
  - algorithms
  - optimisation
summary: >
  Quantum annealing exploits quantum tunnelling to escape local minima. QAOA uses
  parameterised quantum circuits with a variational outer loop. Neither has demonstrated
  consistent advantage over classical methods. The conditions under which tunnelling
  provides advantage depend on energy landscape structure not yet characterised.
systematic_gaps:
  - The energy landscape structure of practically relevant NP-hard instances is poorly characterised for quantum annealing analysis.
  - QAOA performance scaling with circuit depth p for specific problem classes has not been determined analytically.
  - Head-to-head benchmark comparisons controlling for hardware noise have not been published for competitive classical baselines.
last_reviewed: "2026-05-05"
""",

'u-quantum-random-number-true-randomness.yaml': """id: u-quantum-random-number-true-randomness
title: Can quantum random number generators produce certifiably true randomness, and what are the practical limits of device-independent randomness certification?
status: open
priority: low
disciplines:
  - quantum-information
  - cryptography
  - quantum-foundations
summary: >
  Quantum random number generators exploit intrinsic quantum uncertainty. Device-
  independent QRNGs certify randomness using Bell inequality violations, but loopholes,
  side-channel attacks, and assumptions about measurement independence all limit
  certification strength.
systematic_gaps:
  - Practical device-independent QRNGs generate randomness at rates orders of magnitude below application requirements.
  - The relationship between Bell violation strength and randomness certification tightness has not been experimentally validated in practical devices.
  - Side-channel attacks on QRNGs based on implementation imperfections are not comprehensively characterised.
last_reviewed: "2026-05-05"
""",

'u-qkd-practical-limits.yaml': """id: u-qkd-practical-limits
title: What are the practical security limits of quantum key distribution against quantum computer attacks, side channels, and photonic implementation imperfections?
status: open
priority: medium
disciplines:
  - quantum-cryptography
  - quantum-information
  - information-security
summary: >
  QKD is information-theoretically secure in idealised implementations. Practical
  systems deviate through detector side-channels, photon number splitting attacks, and
  finite-key effects. Recent attacks on commercial QKD systems have exploited
  implementation imperfections.
systematic_gaps:
  - No comprehensive security analysis exists for commercial QKD systems including all known side-channel attack vectors.
  - Finite-key security bounds become very conservative for short transmission distances and low photon rates.
  - Device-independent QKD has not been demonstrated at distances or rates practical for real-world use.
last_reviewed: "2026-05-05"
""",

'u-post-quantum-cryptography-transition.yaml': """id: u-post-quantum-cryptography-transition
title: What is the timeline and risk profile of the transition to post-quantum cryptography, and which current systems are most vulnerable to harvest-now-decrypt-later attacks?
status: open
priority: high
disciplines:
  - cryptography
  - quantum-computing
  - cybersecurity
summary: >
  NIST standardised post-quantum cryptographic algorithms in 2024. The transition
  requires updating billions of devices. Harvest-now-decrypt-later attacks collect
  encrypted traffic today to decrypt when sufficiently powerful quantum computers exist.
  The timeline to cryptographically relevant quantum computers is estimated at 10-20
  years but is uncertain.
systematic_gaps:
  - The timeline to CRQC is uncertain by a factor of 2-5x depending on error rate assumptions.
  - The volume of harvested encrypted traffic being stored for future decryption is not known.
  - Implementation vulnerabilities in post-quantum algorithms continue to be discovered.
last_reviewed: "2026-05-05"
""",

'u-quantum-metrology-heisenberg-limit.yaml': """id: u-quantum-metrology-heisenberg-limit
title: Can quantum metrology routinely achieve Heisenberg-limited sensitivity in practical measurement contexts, overcoming decoherence and photon loss?
status: open
priority: medium
disciplines:
  - quantum-metrology
  - quantum-optics
  - quantum-sensing
summary: >
  The Heisenberg limit promises quadratic improvement over the standard quantum limit.
  This advantage has been demonstrated in idealised lab settings using entangled states,
  but practical implementations suffer from photon loss and decoherence that degrade
  the advantage. Above a critical loss rate, quantum advantage vanishes.
systematic_gaps:
  - The crossover loss rate at which Heisenberg-limited sensing fails to outperform the standard quantum limit has not been experimentally mapped for all sensor types.
  - Entangled probe states (NOON states) are extremely fragile; creating them for large N at photon frequencies relevant to atomic imaging is not feasible.
  - Multi-parameter quantum metrology (simultaneous sensing of multiple fields) is theoretically incomplete.
last_reviewed: "2026-05-05"
""",

'u-qft-non-perturbative-regimes.yaml': """id: u-qft-non-perturbative-regimes
title: What analytical or computational methods can access the non-perturbative regimes of quantum field theories, particularly strongly coupled gauge theories?
status: open
priority: high
disciplines:
  - quantum-field-theory
  - theoretical-physics
  - nuclear-physics
summary: >
  Perturbation theory fails when the coupling constant is large. QCD at low energies
  (confinement, hadron structure) is non-perturbative. Lattice QCD provides numerical
  access but is limited by sign problems at finite density. Non-perturbative methods
  including resurgence, conformal bootstrap, and tensor networks are active research
  fronts but have not solved the full problem.
systematic_gaps:
  - The sign problem in lattice QCD at finite baryon density prevents simulation of dense nuclear matter relevant to neutron stars.
  - Confinement in QCD has no rigorous proof; the Yang-Mills mass gap Millennium Problem remains unsolved.
  - AdS/CFT duality provides tools for strongly coupled QFTs but only in the large-N limit and for specific theories.
last_reviewed: "2026-05-05"
""",
}

print("Creating quantum-physics unknowns...")
for filename, content in quantum_files.items():
    write(os.path.join(QP, filename), content)
print(f"  Total: {len(quantum_files)} files\n")

# ────────────────────────────────────────────────────────────────
# 2. LINGUISTICS (25 unknowns)
# ────────────────────────────────────────────────────────────────
LG = os.path.join(BASE, 'unknowns-catalog', 'linguistics')

linguistics_files = {
'u-linguistic-relativity-cognition.yaml': """id: u-linguistic-relativity-cognition
title: Does the language one speaks causally shape non-linguistic thought and perception, and to what degree does the Sapir-Whorf hypothesis hold?
status: open
priority: high
disciplines:
  - linguistics
  - cognitive-science
  - psychology
summary: >
  Strong linguistic relativity (Whorf's hypothesis that language determines thought)
  is generally rejected, but weak relativity (language influences cognition) has
  empirical support in domains including color perception, spatial reasoning, and time
  conceptualisation. The causal direction remains disputed: do speakers of languages
  with more color terms perceive colors differently, or do they merely categorise them
  differently? Cross-linguistic studies show robust effects but replication crisis
  has affected key findings.
systematic_gaps:
  - Distinguishing linguistic from cultural effects in cross-linguistic studies is methodologically difficult.
  - Color perception effects of linguistic categories have been replicated with different spatial patterns across studies.
  - The neural mechanisms by which linguistic categories influence pre-linguistic perception are not known.
last_reviewed: "2026-05-05"
""",

'u-syntax-innateness-evidence.yaml': """id: u-syntax-innateness-evidence
title: Is there a genetically specified universal grammar, and what is the evidence for or against Chomsky's poverty of the stimulus argument?
status: open
priority: high
disciplines:
  - linguistics
  - cognitive-science
  - developmental-psychology
summary: >
  Chomsky's universal grammar (UG) hypothesis holds that humans have an innate
  language acquisition device that constrains the form of possible grammars. The
  poverty of the stimulus argument claims children acquire grammatical knowledge that
  is underdetermined by the linguistic input they receive. Usage-based approaches
  argue that statistical learning from rich input is sufficient. Neither camp has
  a fully satisfying account of language acquisition, and what is innate versus learned
  remains deeply contested.
systematic_gaps:
  - No specific UG principle has been identified in the genome or neural architecture.
  - Modern large language models acquire complex grammar from statistical patterns, weakening the poverty of stimulus argument but not eliminating it.
  - Cross-linguistic acquisition studies do not agree on whether construction-specific or abstract syntactic knowledge emerges first.
last_reviewed: "2026-05-05"
""",

'u-semantic-change-prediction.yaml': """id: u-semantic-change-prediction
title: What mechanisms drive lexical semantic change over time, and can computational models predict which word meanings will shift?
status: open
priority: medium
disciplines:
  - linguistics
  - computational-linguistics
  - historical-linguistics
summary: >
  Semantic change — the shift in word meaning over time (broadening, narrowing,
  metaphorical extension, amelioration, pejoration) — is documented across languages
  but not well predicted in advance. Distributional semantic models trained on
  diachronic corpora can detect shifts post-hoc but predicting which words will change
  and in what direction is largely impossible. The drivers of semantic change (social
  contact, technological change, taboo replacement) interact in complex ways.
systematic_gaps:
  - No predictive model of semantic change achieves better than baseline accuracy on held-out data from historical corpora.
  - The relative contribution of contact-driven versus internal structural pressures to semantic change is not quantified.
  - Short-term semantic drift in internet language does not follow the same patterns as long-term historical change.
last_reviewed: "2026-05-05"
""",

'u-language-death-reversal-feasibility.yaml': """id: u-language-death-reversal-feasibility
title: Under what conditions can a dying language be successfully revitalised, and what are the cognitive and social prerequisites for sustainable reversal?
status: open
priority: medium
disciplines:
  - linguistics
  - sociolinguistics
  - language-policy
summary: >
  Hebrew revitalisation is the only well-documented case of a dormant language
  achieving full native speaker community revival. Other revitalisation efforts
  (Welsh, Maori, Hawaiian) show partial success but no language with fewer than
  1000 remaining speakers has achieved full intergenerational transmission recovery.
  The conditions distinguishing successful from unsuccessful revitalisation (community
  attitudes, institutional support, critical mass, orthography decisions) are
  debated and poorly quantified.
systematic_gaps:
  - No validated predictive model identifies which endangered languages are most likely to benefit from intervention.
  - The role of written tradition versus oral transmission in revitalisation success is not established across cases.
  - Long-term outcomes of language nests and immersion education beyond 20 years have not been tracked.
last_reviewed: "2026-05-05"
""",

'u-creole-genesis-mechanism.yaml': """id: u-creole-genesis-mechanism
title: What grammatical and social mechanisms produce creole languages from contact situations, and is there a universal creole prototype?
status: open
priority: medium
disciplines:
  - linguistics
  - contact-linguistics
  - sociolinguistics
summary: >
  Creole languages arise in contact situations (colonial plantations, trade posts)
  where speakers of mutually unintelligible languages must communicate. Competing
  theories include: superstrate primacy (creole grammars reflect the dominant
  language), bioprogramme hypothesis (creoles reflect universal innate grammar),
  and gradualist models (creoles emerge from pidgins over generations). No single
  mechanism explains all creole grammatical features across cases.
systematic_gaps:
  - The bioprogramme hypothesis predicts specific creole universals that are contested across cases.
  - The role of adults versus children in creolisation has not been determined from historical records.
  - Creole formation in contemporary signed language contact situations has not been fully studied.
last_reviewed: "2026-05-05"
""",

'u-signed-language-neural-substrate.yaml': """id: u-signed-language-neural-substrate
title: Do signed languages engage the same or different neural substrates as spoken languages, and what does this reveal about language universality?
status: open
priority: medium
disciplines:
  - linguistics
  - neuroscience
  - cognitive-science
summary: >
  Signed languages (ASL, BSL, LSF) are fully natural languages with phonology,
  morphology, and syntax. Neuroimaging shows left-hemisphere language areas are
  recruited for both signed and spoken language, suggesting neural substrate
  universality. However, signed languages also engage right-hemisphere visuospatial
  regions more than spoken languages. Whether the additional visuospatial processing
  reflects language-specific or modality-specific neural circuits is disputed.
systematic_gaps:
  - The lateralisation of signed language in deaf versus hearing signers shows different patterns not fully explained by models of language lateralisation.
  - The neural basis of cross-modal influence (speechreading modifying auditory processing in hearing signers) is not well understood.
  - Deaf native signers and hearing L2 signers show different neural activation patterns whose interpretation is contested.
last_reviewed: "2026-05-05"
""",

'u-bilingual-cognitive-advantage-replication.yaml': """id: u-bilingual-cognitive-advantage-replication
title: Does bilingualism confer measurable cognitive advantages in executive function, and why have many key findings failed to replicate?
status: open
priority: medium
disciplines:
  - linguistics
  - cognitive-science
  - psychology
summary: >
  Early studies claimed bilinguals outperform monolinguals on executive function tasks
  (task-switching, inhibitory control) due to constant experience managing two language
  systems. Several high-powered replication attempts have failed, and meta-analyses
  show publication bias. The question of whether any robust bilingual advantage exists
  and under what conditions remains unresolved.
systematic_gaps:
  - The definition of bilingualism (degree of proficiency, age of acquisition, language use frequency) varies so much across studies that comparison is difficult.
  - Publication bias in favour of positive results severely inflates effect size estimates in meta-analyses.
  - Laboratory executive function tasks may not reflect real-world cognitive performance differences.
last_reviewed: "2026-05-05"
""",

'u-language-thought-interface.yaml': """id: u-language-thought-interface
title: Is language necessary for abstract thought, or can complex reasoning occur in pre-linguistic or non-linguistic representational formats?
status: open
priority: high
disciplines:
  - linguistics
  - cognitive-science
  - philosophy-of-mind
summary: >
  The debate about whether language is constitutive of abstract thought (language-of-
  thought hypothesis, Fodor) or merely expressive has persisted for decades. Evidence
  from nonhuman primates, pre-linguistic infants, deaf individuals raised without
  language, and acquired aphasia patients offers conflicting clues. Large language
  models apparently perform complex reasoning without any of the pragmatic, embodied,
  or social dimensions of human language acquisition, complicating the picture.
systematic_gaps:
  - Patients with severe aphasia who lose language production/comprehension sometimes retain complex reasoning abilities, but the extent is debated.
  - Pre-linguistic infants demonstrate abstract numerical and causal reasoning, but whether this is linguistic is definitionally circular.
  - The mentalese hypothesis (inner language of thought) is unfalsifiable in its strong form.
last_reviewed: "2026-05-05"
""",

'u-metaphor-universality.yaml': """id: u-metaphor-universality
title: Are conceptual metaphors universal across languages and cultures, or are they culturally specific constructions reflecting local experience?
status: open
priority: medium
disciplines:
  - linguistics
  - cognitive-science
  - anthropology
summary: >
  Conceptual metaphor theory (Lakoff and Johnson) claims that abstract thought is
  structured by embodied conceptual metaphors (TIME IS MONEY, ARGUMENT IS WAR) that
  are universal because they arise from shared physical experience. Cross-linguistic
  studies show many metaphors are widespread but not universal; some appear culturally
  specific (e.g., metaphors for time in Aymara, Mandarin, English differ systematically).
  The degree to which metaphors are driven by embodied universals versus cultural
  convention is not resolved.
systematic_gaps:
  - Cross-linguistic corpus studies of conceptual metaphor are biased toward Indo-European languages.
  - Distinguishing universal from widespread-but-not-universal metaphors requires very broad typological sampling not yet done.
  - The relationship between linguistic metaphor and non-linguistic analogical reasoning is not established.
last_reviewed: "2026-05-05"
""",

'u-pragmatic-inference-neural-basis.yaml': """id: u-pragmatic-inference-neural-basis
title: What neural mechanisms support pragmatic inference (implicature, irony, indirect speech), and why are these mechanisms impaired in autism spectrum conditions?
status: open
priority: medium
disciplines:
  - linguistics
  - neuroscience
  - cognitive-science
summary: >
  Pragmatic language inference — understanding that a speaker means more or something
  different than the literal content of their words — requires theory of mind, world
  knowledge, and social context integration. Neuroimaging implicates right hemisphere
  regions (temporal-parietal junction, medial prefrontal cortex) beyond the classical
  left-hemisphere language areas. Autism spectrum conditions show selective impairment
  in pragmatics without impairment in syntax, suggesting dissociable neural substrates.
systematic_gaps:
  - The neural basis of scalar implicature (interpreting "some" as "not all") is disputed between left and right hemisphere theories.
  - The relationship between pragmatic impairment in ASD and theory of mind deficit is correlational, not causal.
  - Pragmatic inference in second language speakers recruits different neural circuits than in native speakers; the developmental trajectory is unknown.
last_reviewed: "2026-05-05"
""",

'u-prosody-meaning-mapping.yaml': """id: u-prosody-meaning-mapping
title: How are the acoustic properties of prosody (pitch, duration, rhythm) systematically mapped to meaning, and how is this mapping acquired?
status: open
priority: medium
disciplines:
  - linguistics
  - phonetics
  - cognitive-science
summary: >
  Prosody — intonation, stress, rhythm, and timing — conveys information about
  sentence structure, information status (given vs new), and speaker attitude that is
  not encoded in words. Cross-linguistic studies show both universal tendencies (rising
  intonation for questions) and language-specific realisations. How prosodic patterns
  are acquired and represented in the mental grammar, and how they interact with lexical
  tone in tonal languages, remains incompletely understood.
systematic_gaps:
  - A unified formal account of prosody that handles both intonation phonology and pragmatic meaning in all language types does not exist.
  - The acquisition timeline of prosody compared to segmental phonology has not been systematically cross-linguistically compared.
  - Prosodic disambiguation in parsing (bracketing prosody) is modelled separately from information-structural prosody without unification.
last_reviewed: "2026-05-05"
""",

'u-tonal-language-cognitive-effects.yaml': """id: u-tonal-language-cognitive-effects
title: Does speaking a tonal language confer cognitive differences in pitch processing, and does this interact with absolute pitch ability?
status: open
priority: medium
disciplines:
  - linguistics
  - cognitive-science
  - music-cognition
summary: >
  Approximately 70 percent of the world's languages use lexical tone (Mandarin, Yoruba,
  Vietnamese). Speakers of tonal languages show enhanced pitch discrimination in
  non-linguistic contexts and have higher rates of absolute pitch in musicians. Whether
  this constitutes a domain-general enhancement or a language-specific effect, and
  whether it arises from early linguistic experience or genetic predisposition, is not
  resolved.
systematic_gaps:
  - Studies of absolute pitch in tonal language musicians are subject to selection bias as tonal language communities have different musical training traditions.
  - The developmental window during which tonal language exposure enhances pitch processing has not been established.
  - Neurological basis of tone processing differences between tonal and non-tonal language speakers is undercharacterised.
last_reviewed: "2026-05-05"
""",

'u-writing-system-cognition-effects.yaml': """id: u-writing-system-cognition-effects
title: Do different writing systems (alphabetic, syllabic, logographic) produce measurable differences in reading processes and cognitive architecture?
status: open
priority: medium
disciplines:
  - linguistics
  - cognitive-science
  - educational-psychology
summary: >
  Alphabetic (English), syllabic (Japanese kana), and logographic (Chinese characters)
  writing systems require different encoding strategies. Cross-linguistic reading
  research shows different neural pathways for reading Chinese versus English, and
  different phonological awareness requirements. Whether these differences reflect the
  writing system itself or the language it encodes, and whether they have downstream
  effects on broader cognition, is debated.
systematic_gaps:
  - The neural basis of logographic versus alphabetic reading shows consistent differences in imaging studies, but their cognitive significance is not clear.
  - Dyslexia manifests differently in different writing systems; whether it is one disorder or many remains unknown.
  - The causal effect of writing system choice (e.g., Atatürk's romanisation of Turkish) on literacy rates and cognition has not been isolated from confounding factors.
last_reviewed: "2026-05-05"
""",

'u-language-acquisition-poverty-stimulus.yaml': """id: u-language-acquisition-poverty-stimulus
title: Does the logical problem of language acquisition (poverty of the stimulus) require innate grammatical knowledge, or can it be solved by statistical learning?
status: open
priority: high
disciplines:
  - linguistics
  - developmental-psychology
  - computational-linguistics
summary: >
  Children acquire complex grammatical knowledge — including knowledge of structure-
  dependence, island constraints, binding principles — despite not receiving explicit
  instruction or (apparently) sufficient evidence in the input. Chomsky argued this
  requires innate grammatical knowledge (universal grammar). Statistical learning
  advocates argue that sufficiently rich distributional information in natural input,
  combined with general learning mechanisms, is sufficient. Neither position has
  decisive empirical support.
systematic_gaps:
  - The statistical information available to children for specific grammatical structures (e.g. subject-auxiliary inversion) has not been exhaustively computed from child-directed speech corpora.
  - Large language models acquire apparently structure-dependent knowledge from text, but they receive vastly more input than children and lack embodied experience.
  - The age at which specific grammatical structures are acquired cross-linguistically does not follow predictions of either strong nativist or strong empiricist models.
last_reviewed: "2026-05-05"
""",

'u-recursion-uniquely-human.yaml': """id: u-recursion-uniquely-human
title: Is syntactic recursion uniquely human and essential for language, or do non-human animals possess recursive cognitive mechanisms?
status: open
priority: medium
disciplines:
  - linguistics
  - cognitive-science
  - animal-cognition
summary: >
  Hauser, Chomsky, and Fitch (2002) proposed that recursion is the only uniquely human
  aspect of language faculty. Everett challenged this with claims that Piraha lacks
  grammatical recursion. Animal learning experiments test whether non-human species
  (macaques, starlings) can learn recursive grammars. Disputes concern what counts as
  recursion and whether it is grammatically or cognitively instantiated.
systematic_gaps:
  - The claim that Piraha lacks recursion is disputed by other linguists on grammatical grounds; the fieldwork has not been replicated by independent researchers.
  - Animal grammar learning experiments cannot distinguish pattern memorisation from recursive rule learning with current methods.
  - Whether recursion in language is the same cognitive capacity as recursion in mathematical and spatial reasoning is not established.
last_reviewed: "2026-05-05"
""",

'u-semantic-compositionality-limits.yaml': """id: u-semantic-compositionality-limits
title: To what extent is natural language meaning compositional, and where do non-compositional constructions require fundamentally different processing?
status: open
priority: medium
disciplines:
  - linguistics
  - formal-semantics
  - cognitive-science
summary: >
  Compositionality — that the meaning of a complex expression is determined by the
  meanings of its parts and how they are combined — is a foundational assumption of
  formal semantics. Idioms, lexical bundles, constructions, and pragmatic enrichment
  all challenge strict compositionality. How much of natural language meaning can be
  compositionally derived, and what mechanisms handle the rest, is an open question
  in both formal semantics and neural language models.
systematic_gaps:
  - Formal compositional semantics handles core syntax-semantics interface well but cannot account for conventional implicature, presupposition, and constructional meaning in a unified framework.
  - Neural language models appear to handle non-compositional constructions but their internal representations are not compositional in the formal sense.
  - The developmental trajectory of compositional versus construction-specific meaning acquisition in children is not established.
last_reviewed: "2026-05-05"
""",

'u-language-model-meaning-vs-human.yaml': """id: u-language-model-meaning-vs-human
title: Do large language models have genuine semantic understanding of language meaning, or do they manipulate form without accessing meaning?
status: open
priority: high
disciplines:
  - linguistics
  - artificial-intelligence
  - philosophy-of-mind
summary: >
  Large language models demonstrate impressive linguistic behaviour including
  metaphor comprehension, pragmatic inference, and analogical reasoning, but achieve
  this through statistical patterns over form rather than through the embodied,
  social, and causal experience that underlies human language understanding. Whether
  this constitutes genuine semantic understanding, a functional approximation, or
  neither is philosophically and empirically contested.
systematic_gaps:
  - No agreed operationalisation of "genuine understanding" exists that would distinguish LLM competence from human competence.
  - LLMs fail on systematic generalisation tasks in ways that human language users do not, but the nature of these failures is disputed.
  - Whether grounding language in perception and action is necessary for semantic understanding or merely sufficient cannot be determined from current experiments.
last_reviewed: "2026-05-05"
""",

'u-endangered-language-documentation-priority.yaml': """id: u-endangered-language-documentation-priority
title: What documentation strategies best preserve endangered languages for future linguistic and cultural research, and how should priorities be set?
status: open
priority: medium
disciplines:
  - linguistics
  - language-documentation
  - anthropology
summary: >
  Approximately half of the world's 7000 languages may cease to be spoken by 2100.
  Language documentation aims to create a record for future research and community use.
  Competing approaches prioritise grammatical description, lexicon, naturalistic text,
  multimedia corpus, or community-driven revitalisation. Limited resources make
  prioritisation necessary but the criteria for prioritisation (speaker age, structural
  uniqueness, community interest) are not agreed.
systematic_gaps:
  - The relative value of different documentation types for future linguistic research versus community use are not empirically assessed.
  - Digital preservation formats and archiving standards are not standardised across documentation projects, creating fragmentation.
  - The effectiveness of documentation in supporting later revitalisation has not been systematically evaluated across projects.
last_reviewed: "2026-05-05"
""",

'u-linguistic-relativity-color-perception.yaml': """id: u-linguistic-relativity-color-perception
title: Does the number and location of color term boundaries in a language causally affect the speed and accuracy of cross-category color discrimination?
status: open
priority: medium
disciplines:
  - linguistics
  - cognitive-science
  - perceptual-psychology
summary: >
  Languages differ in the number of basic color terms and where they place category
  boundaries. English distinguishes blue and green; Russian has separate terms for
  light and dark blue (goluboy/siniy). Psychophysical studies show faster
  discrimination at linguistic boundaries than within categories (categorical
  perception), but whether this is a permanent cognitive effect or a task-specific
  verbal interference effect is contested.
systematic_gaps:
  - Perceptual interference studies (where verbal interference reduces the color categorical perception effect) are not conclusive about whether the effect is pre-linguistic.
  - Cross-cultural color categorisation studies rely on Munsell chips that may not be culturally neutral stimuli.
  - The effect size of cross-linguistic color categorical perception differences is small and contested in meta-analyses.
last_reviewed: "2026-05-05"
""",

'u-historical-reconstruction-limit.yaml': """id: u-historical-reconstruction-limit
title: What is the temporal limit of reliable linguistic reconstruction, and can proto-language families beyond 10,000 years be validly inferred?
status: open
priority: medium
disciplines:
  - linguistics
  - historical-linguistics
  - anthropology
summary: >
  The comparative method reliably reconstructs proto-languages back ~10,000 years
  (Proto-Indo-European, ~6000 years ago; Uralic, ~7000 years ago). Claims about
  deeper relationships (Proto-Nostratic, Proto-Sapiens, Proto-World) remain highly
  contested because random similarity probability rises with time, regularity of
  correspondence erodes, and lexical replacement rates limit detectable signal.
  Whether any deep historical relationships can be scientifically established is debated.
systematic_gaps:
  - No agreed statistical method distinguishes deep genealogical relationship from chance similarity at timescales beyond 10,000 years.
  - Mass comparison (Greenberg) and the comparative method give different and incompatible results on the same language groupings.
  - Archaeological and genetic evidence is inconsistent with some linguistic family groupings and cannot resolve the disputes.
last_reviewed: "2026-05-05"
""",

'u-language-universals-typology.yaml': """id: u-language-universals-typology
title: Which linguistic features are truly universal across all human languages, and what explains the implicational universals observed in typological surveys?
status: open
priority: medium
disciplines:
  - linguistics
  - linguistic-typology
  - cognitive-science
summary: >
  Greenberg's (1963) typological universals revealed implicational patterns across
  languages (if SOV then postpositions). Subsequent research has shown many proposed
  universals are tendencies, not absolutes, and that sampling bias towards well-studied
  languages inflates apparent universality. The explanation for observed universals
  (innate constraints, processing efficiency, learning biases, cultural transmission
  biases) remains debated.
systematic_gaps:
  - WALS (World Atlas of Language Structures) covers only a fraction of languages and is biased toward documented, larger languages.
  - The distinction between hard universals and strong tendencies has not been resolved due to insufficient typological coverage.
  - Processing efficiency explanations for word order universals have been challenged by the existence of flexible word order languages that are also common.
last_reviewed: "2026-05-05"
""",

'u-language-evolution-emergence.yaml': """id: u-language-evolution-emergence
title: How and when did language evolve in the hominin lineage, and what were the anatomical, neural, and social preconditions?
status: open
priority: high
disciplines:
  - linguistics
  - evolutionary-biology
  - paleoanthropology
summary: >
  Human language leaves no fossil record directly. Proxy evidence includes FOXP2
  gene expression in Neandertals, fossil hyoid bone shape, cranial endocasts showing
  Broca's area development, and symbolic artefact appearance. Competing models propose
  language emergence as: (a) sudden (Chomsky), (b) gradual via gesture-first
  (Arbib), (c) driven by cooperative information sharing (Tomasello). No consensus
  exists on the timeline, number of transitions, or selective pressures.
systematic_gaps:
  - FOXP2 mutations affecting language in humans are present in Neandertals but FOXP2 alone does not determine language ability.
  - The genetic basis of the full language apparatus spans hundreds of genes; evolutionary reconstruction is not possible from known variants.
  - Archaeological proxies for language (symbolic behaviour, complex tools) may reflect other cognitive capacities rather than language specifically.
last_reviewed: "2026-05-05"
""",

'u-prosodic-bootstrapping-acquisition.yaml': """id: u-prosodic-bootstrapping-acquisition
title: Does prosodic structure in infant-directed speech provide bootstrapping cues for syntactic acquisition, and how large is its contribution?
status: open
priority: medium
disciplines:
  - linguistics
  - developmental-psychology
  - phonetics
summary: >
  Prosodic bootstrapping theory (Gleitman, Morgan) proposes that infants use prosodic
  phrase boundaries to segment the acoustic stream and infer syntactic structure before
  they understand word meanings. Evidence includes infant sensitivity to prosodic
  boundaries from birth and preference for grammatical over prosodically
  manipulated strings. The magnitude of the prosodic bootstrapping contribution
  relative to other acquisition mechanisms remains quantified only weakly.
systematic_gaps:
  - The specific syntactic information that can be inferred from prosodic patterns alone has not been formally delimited.
  - Cross-linguistic infant studies on prosodic bootstrapping are biased toward English; rhythmically different languages have not been comparably studied.
  - The interaction between prosodic bootstrapping and semantic or pragmatic bootstrapping has not been modelled.
last_reviewed: "2026-05-05"
""",

'u-gesture-language-interface.yaml': """id: u-gesture-language-interface
title: What is the cognitive and neural relationship between gesture and speech, and does gesture play a constitutive role in language production and comprehension?
status: open
priority: medium
disciplines:
  - linguistics
  - cognitive-science
  - neuroscience
summary: >
  Speakers gesture spontaneously when speaking and gesture even on the phone. McNeill
  proposes gesture and speech form an integrated utterance. Gesture conveys information
  that supplements or contradicts speech, and comprehenders integrate gestural meaning
  with spoken meaning. Whether gesture is a constitutive part of language or a
  parallel communicative channel, and what its role in thought is, remains debated.
systematic_gaps:
  - The neural regions integrating gesture and speech have been identified but the computational mechanisms of integration are not modelled.
  - Whether gesturing facilitates thinking or merely indexes thinking is not experimentally distinguished in current paradigms.
  - Cross-cultural variation in gesture use and its effects on comprehension are undercharacterised.
last_reviewed: "2026-05-05"
""",
}

print("Creating linguistics unknowns...")
for filename, content in linguistics_files.items():
    write(os.path.join(LG, filename), content)
print(f"  Total: {len(linguistics_files)} files\n")

# ────────────────────────────────────────────────────────────────
# 3. SOCIAL-SCIENCE (25 unknowns)
# ────────────────────────────────────────────────────────────────
SS = os.path.join(BASE, 'unknowns-catalog', 'social-science')

social_files = {
'u-social-norm-cascade-tipping-points.yaml': """id: u-social-norm-cascade-tipping-points
title: What are the tipping point conditions under which social norms rapidly cascade through populations, and can they be predicted in advance?
status: open
priority: high
disciplines:
  - social-science
  - complex-systems
  - sociology
summary: >
  Social norms — shared expectations about behaviour — can shift rapidly and
  non-linearly. Historical examples include smoking denormalisation, same-sex marriage
  acceptance, and #MeToo. Models predict tipping points at certain minority thresholds
  (Centola's 25 percent theory), but empirical identification of approaching tipping
  points before they occur has not been demonstrated. Social media accelerates norm
  diffusion but also creates artificial pluralistic ignorance.
systematic_gaps:
  - No validated early warning indicator of social norm tipping points has been demonstrated prospectively.
  - The minimum committed minority fraction required to trigger norm cascade varies widely across empirical cases.
  - Online norm change does not reliably predict offline norm change.
last_reviewed: "2026-05-05"
""",

'u-institutional-trust-collapse.yaml': """id: u-institutional-trust-collapse
title: What mechanisms drive rapid collapses in institutional trust, and can early warning signs be identified before collapse occurs?
status: open
priority: high
disciplines:
  - social-science
  - political-science
  - sociology
summary: >
  Trust in democratic institutions, media, science, and government has declined
  sharply in many Western democracies since the 1970s. Whether this represents
  a universal trend, a cyclical process, or a permanent structural change is debated.
  The causal mechanisms — elite failures, media fragmentation, economic inequality,
  or demographic change — are disputed and their relative contributions unquantified.
  Predicting institutional trust collapse has proven extremely difficult.
systematic_gaps:
  - Long-run institutional trust data spanning different countries and institutional types is not comparable across measurement instruments.
  - Causal identification of the specific mechanisms driving trust collapse is confounded by simultaneous changes in multiple factors.
  - The relationship between measured trust and institutional behaviour (compliance, cooperation, voting) is not stable across contexts.
last_reviewed: "2026-05-05"
""",

'u-political-polarisation-dynamics.yaml': """id: u-political-polarisation-dynamics
title: What drives increasing political polarisation in democracies, and are online filter bubbles a primary cause or a symptom?
status: open
priority: high
disciplines:
  - social-science
  - political-science
  - computational-social-science
summary: >
  Affective polarisation (partisan animosity) has increased sharply in the US and
  several European democracies, even as ideological polarisation on specific policy
  issues shows a more complex pattern. Proposed causes include social media filter
  bubbles, economic inequality, geographic sorting, and elite-driven polarisation.
  Natural experiments (deactivating social media accounts) show small effects on
  polarisation, suggesting social media is not the primary driver.
systematic_gaps:
  - The relative contribution of social media versus economic and geographic factors to polarisation is not causally established.
  - Polarisation in countries with different media ecosystems shows heterogeneous patterns not explained by any single theory.
  - The feedback between elite polarisation and mass polarisation is not modelled dynamically.
last_reviewed: "2026-05-05"
""",

'u-misinformation-correction-asymmetry.yaml': """id: u-misinformation-correction-asymmetry
title: Why is misinformation often more persistent and spreadable than corrections, and what interventions reliably reduce its effects?
status: open
priority: high
disciplines:
  - social-science
  - psychology
  - communication-science
summary: >
  False information often spreads faster and further than corrections on social media.
  Attempted corrections can produce backfire effects (strengthening belief in the
  original falsehood), though the robustness of backfire effects is disputed. Prebunking
  (inoculation theory) and accuracy nudges show promise in laboratory settings but
  their real-world effectiveness at scale is limited. The mechanisms underlying
  misinformation persistence (confirmation bias, emotional resonance, source distrust)
  vary by individual and context.
systematic_gaps:
  - Meta-analyses of correction effectiveness show high heterogeneity; the conditions predicting successful correction are not established.
  - Laboratory interventions for misinformation correction often fail to replicate or generalise to real-world misinformation.
  - The relationship between misinformation exposure and actual belief change is measured inconsistently across studies.
last_reviewed: "2026-05-05"
""",

'u-collective-action-without-authority.yaml': """id: u-collective-action-without-authority
title: Under what conditions can groups solve collective action problems without central authority, and how do informal institutions maintain cooperation?
status: open
priority: high
disciplines:
  - social-science
  - economics
  - political-science
summary: >
  Ostrom's work showed that communities often self-govern common pool resources
  without state intervention or privatisation. The conditions enabling successful
  self-governance (design principles: clear boundaries, proportional rules, collective
  choice, monitoring, graduated sanctions, conflict resolution) are partially identified
  but not fully understood. Whether Ostrom's principles generalise to global commons
  (atmosphere, oceans) is contested.
systematic_gaps:
  - The minimum group size and cultural conditions for successful self-governance have not been systematically established.
  - Scaling Ostrom's principles to large-scale digital commons or global public goods has not been validated.
  - The interaction between formal legal institutions and informal self-governance is not modelled dynamically.
last_reviewed: "2026-05-05"
""",

'u-social-capital-measurement.yaml': """id: u-social-capital-measurement
title: What is the best way to measure social capital, and do different definitions (bonding, bridging, linking) have different effects on economic and social outcomes?
status: open
priority: medium
disciplines:
  - social-science
  - economics
  - sociology
summary: >
  Social capital — networks, norms, and trust enabling collective action — is
  measured inconsistently across studies using survey trust questions, network density,
  civic participation, or institutional quality. The distinction between bonding
  (within-group), bridging (cross-group), and linking (vertical) social capital
  predicts different outcomes. Causal identification of social capital effects on
  economic growth, health, and governance is extremely difficult due to endogeneity.
systematic_gaps:
  - No agreed measurement instrument for social capital enables cross-national comparison with consistent validity.
  - The causal effect of social capital on economic outcomes is confounded by common causes (culture, institutions, geography).
  - Whether social capital is generative (communities create it) or inherited (path-dependent from historical institutions) has not been resolved.
last_reviewed: "2026-05-05"
""",

'u-cultural-evolution-rate-prediction.yaml': """id: u-cultural-evolution-rate-prediction
title: What determines the rate of cultural evolution, and can formal evolutionary models predict the speed and direction of cultural change?
status: open
priority: medium
disciplines:
  - social-science
  - cultural-evolution
  - anthropology
summary: >
  Cultural evolution theory applies Darwinian principles to the spread and modification
  of cultural variants (ideas, practices, technologies). Formal models predict rates of
  change based on population size, variation generation, and selection pressure. The
  degree to which cultural evolution is driven by biased transmission (conformity,
  prestige), content biases, or neutral drift varies across domains and is not agreed.
systematic_gaps:
  - The neutral model of cultural evolution (random cultural drift) is not consistently distinguishable from selection-driven change in empirical data.
  - Gene-culture coevolution models are formally developed but empirically tested only for a few traits (lactase persistence, alcohol metabolism).
  - Predicting which cultural variants will spread versus die out in advance has not been demonstrated reliably.
last_reviewed: "2026-05-05"
""",

'u-economic-inequality-tipping-points.yaml': """id: u-economic-inequality-tipping-points
title: At what level of economic inequality do self-reinforcing mechanisms kick in to produce permanently elevated inequality, and can policy reverse this?
status: open
priority: high
disciplines:
  - social-science
  - economics
  - political-science
summary: >
  Rising economic inequality in advanced economies since the 1980s may reflect self-
  reinforcing mechanisms (wealth effects on political influence, skill-biased
  technological change, capital-labour dynamics). Piketty's r > g thesis proposes
  that capital returns exceeding growth rates naturally produce rising inequality.
  Whether there are tipping points beyond which inequality becomes self-perpetuating
  and politically irreversible, and where those thresholds are, is not established.
systematic_gaps:
  - The causal relationship between inequality and political influence (the inequality trap) has not been established rigorously.
  - Whether inequality is a cause or consequence of institutional quality is not resolved.
  - Historical reductions in inequality (interwar period, 1945-1975) do not agree on which mechanisms drove the change.
last_reviewed: "2026-05-05"
""",

'u-democracy-stability-conditions.yaml': """id: u-democracy-stability-conditions
title: Under what economic, social, and institutional conditions is democracy stable, and what early warning indicators predict democratic backsliding?
status: open
priority: high
disciplines:
  - political-science
  - social-science
  - economics
summary: >
  Democratic backsliding — gradual erosion of democratic norms and institutions by
  elected leaders — has been observed in Hungary, Turkey, Poland, India, and the US.
  The conditions distinguishing stable from fragile democracies include: per-capita
  income, prior democratic experience, party system institutionalisation, and military
  subordination to civilian control. Early warning indicators have been developed but
  not prospectively validated.
systematic_gaps:
  - Early warning indicators of democratic backsliding show high false-positive rates when tested prospectively.
  - The relative importance of economic versus institutional factors in preventing backsliding is not established.
  - Whether democratic backsliding is reversible after a certain point has not been studied systematically.
last_reviewed: "2026-05-05"
""",

'u-social-mobility-measurement.yaml': """id: u-social-mobility-measurement
title: How should intergenerational social mobility be measured, and what policies reliably increase it across different national contexts?
status: open
priority: medium
disciplines:
  - social-science
  - economics
  - sociology
summary: >
  Intergenerational mobility measures (earnings elasticity, rank-rank correlation,
  relative vs absolute mobility) give different and sometimes contradictory pictures
  of mobility trends. The Great Gatsby Curve (Corak) shows higher inequality is
  associated with lower mobility across countries, but the causal mechanisms are
  disputed. Effective policies for increasing mobility are not agreed across national
  contexts.
systematic_gaps:
  - Different mobility measures give different rankings of countries and different trend assessments; no agreed measure exists.
  - The causal pathways from parental income to child outcomes (neighbourhood, school quality, social networks, cultural capital) have not been individually isolated.
  - Policies shown to increase mobility in one country often fail to replicate in another.
last_reviewed: "2026-05-05"
""",

'u-gender-gap-stem-causes.yaml': """id: u-gender-gap-stem-causes
title: What explains persistent gender gaps in STEM participation, and why do gaps vary so widely across countries, disciplines, and historical periods?
status: open
priority: medium
disciplines:
  - social-science
  - psychology
  - education-research
summary: >
  Women are underrepresented in physics, computing, and engineering but overrepresented
  in biology and medicine. The gender gap in STEM varies dramatically across countries
  (larger in Scandinavian countries with high gender equality — the "gender equality
  paradox"), implying that purely societal explanations are insufficient. Proposed
  causes include stereotype threat, implicit bias, interests, confidence, and
  structural barriers.
systematic_gaps:
  - The gender equality paradox (larger gaps in more equal societies) has multiple proposed explanations none of which is empirically resolved.
  - Stereotype threat effects in STEM have shown inconsistent replication across studies.
  - The relative contribution of interests versus structural barriers to gender gaps cannot be causally disentangled.
last_reviewed: "2026-05-05"
""",

'u-criminal-justice-deterrence.yaml': """id: u-criminal-justice-deterrence
title: What is the evidence that criminal punishment deters crime, and which punishment characteristics (certainty, severity, speed) have the largest effects?
status: open
priority: medium
disciplines:
  - social-science
  - criminology
  - public-policy
summary: >
  Deterrence theory predicts crime rates respond to punishment certainty, severity,
  and celerity. Meta-analyses find that punishment certainty has a larger deterrent
  effect than severity, and that marginal increases in sentence length beyond moderate
  levels have negligible deterrent effects. However, the evidence is largely observational
  and plagued by endogeneity; few natural experiments isolate specific punishment
  parameters.
systematic_gaps:
  - Natural experiments that cleanly identify the causal effect of specific deterrence parameters are rare; most evidence is quasi-experimental.
  - Deterrence effects vary substantially by crime type, offender type, and context in ways not fully explained.
  - The relative effectiveness of deterrence versus incapacitation versus rehabilitation in reducing crime is not established across national contexts.
last_reviewed: "2026-05-05"
""",

'u-social-media-mental-health-causality.yaml': """id: u-social-media-mental-health-causality
title: Does social media use causally increase depression, anxiety, and loneliness in adolescents, and which usage patterns are most harmful?
status: open
priority: high
disciplines:
  - social-science
  - psychology
  - public-health
summary: >
  Cross-sectional and longitudinal studies show correlations between social media use
  and worse mental health outcomes in adolescents, with stronger effects for girls.
  However, causal identification is extremely difficult; reverse causation and
  confounding are plausible. The few experimental studies (deactivation experiments)
  show small effects. The question of whether specific platforms, content types, or
  usage patterns drive harm remains unresolved.
systematic_gaps:
  - Natural experiments (Facebook rollout, platform outages) show heterogeneous and often null effects on mental health outcomes.
  - The mechanism (social comparison, sleep displacement, cyberbullying, algorithmic amplification) for any harm is not established.
  - Effect sizes in longitudinal studies are small (r~0.05) and may not be practically significant even if causal.
last_reviewed: "2026-05-05"
""",

'u-urban-segregation-self-reinforcement.yaml': """id: u-urban-segregation-self-reinforcement
title: To what degree does residential racial and economic segregation self-reinforce through school quality, social networks, and political power?
status: open
priority: medium
disciplines:
  - social-science
  - urban-economics
  - sociology
summary: >
  US urban residential segregation remains high despite decades of fair housing laws.
  Proposed self-reinforcing mechanisms include: school quality tied to property taxes,
  social network homophily, political influence over zoning, and taste-based
  discrimination. Whether these mechanisms constitute a stable equilibrium requiring
  active intervention to escape, or a slow convergence, is not empirically resolved.
systematic_gaps:
  - The relative contribution of taste-based discrimination, economic sorting, and political mechanisms to sustained segregation is not causally identified.
  - The conditions under which desegregation policies succeed versus fail are not predictable from current theory.
  - Segregation dynamics in cities with different housing market structures have not been compared in a unified framework.
last_reviewed: "2026-05-05"
""",

'u-war-onset-prediction.yaml': """id: u-war-onset-prediction
title: What variables most reliably predict the onset of interstate and civil wars, and do existing models generalise across historical periods and regions?
status: open
priority: high
disciplines:
  - political-science
  - social-science
  - international-relations
summary: >
  Quantitative conflict research has identified correlates of war (power parity,
  regime type, trade interdependence, ethnic fractionalization, past conflict),
  but predictive models have poor out-of-sample performance. The democratic peace
  (democracies rarely fight each other) is one of the most replicated findings in
  political science but has contested boundary conditions. Predicting specific war
  onset in advance has not been reliably demonstrated.
systematic_gaps:
  - Conflict prediction models trained on pre-2000 data perform poorly on post-2000 conflicts; the conflict landscape has changed in ways not captured by traditional variables.
  - The distinction between variables that are genuine causes versus indicators (epiphenomena) of conflict is not established.
  - Civil war and interstate war are modelled separately but their interaction (spillover, proxy conflicts) is poorly theorised.
last_reviewed: "2026-05-05"
""",

'u-genocide-early-warning-validity.yaml': """id: u-genocide-early-warning-validity
title: Do genocide early warning systems have sufficient predictive validity and response time to enable preventive intervention?
status: open
priority: high
disciplines:
  - political-science
  - social-science
  - international-relations
summary: >
  Genocide early warning systems (Genocide Watch, Atrocity Forecasting Project)
  use structured risk assessments based on known precursors (dehumanising rhetoric,
  political exclusion, prior violence, weapon distribution). Their prospective
  predictive validity — whether they identify at-risk cases before violence occurs
  with sufficient lead time — has not been rigorously evaluated against a held-out
  test set of cases.
systematic_gaps:
  - The base rate of genocide is very low, making false positive rates extremely important and difficult to manage.
  - Early warning systems have not been prospectively validated on out-of-sample cases with pre-registered predictions.
  - The causal effectiveness of early warning + intervention in preventing genocide has not been established; most cases with warning signals do not receive effective intervention.
last_reviewed: "2026-05-05"
""",

'u-multilateral-cooperation-failure-modes.yaml': """id: u-multilateral-cooperation-failure-modes
title: Why do multilateral cooperation arrangements fail for global commons problems, and what institutional designs are most robust to defection?
status: open
priority: high
disciplines:
  - political-science
  - social-science
  - international-relations
summary: >
  International cooperation on global commons problems (climate, pandemics, nuclear
  weapons, ocean governance) often fails or produces weak agreements. Game-theoretic
  models predict defection incentives in prisoner's-dilemma-like structures, but many
  successful international agreements exist. The conditions distinguishing successful
  from failed multilateral cooperation (linkage, side payments, monitoring, sanctions,
  reciprocity) are partially identified but not generalisable.
systematic_gaps:
  - The relative effectiveness of different institutional design features (trade linkage, financial transfers, verification mechanisms) is not established across cooperation domains.
  - Most international relations research on cooperation is case-based; quantitative comparative analysis across all major cooperation attempts is lacking.
  - The role of domestic politics in determining a country's international cooperation behaviour is modelled separately from the international level but both levels interact.
last_reviewed: "2026-05-05"
""",

'u-social-contagion-vs-homophily.yaml': """id: u-social-contagion-vs-homophily
title: For any given social behaviour, how much of its clustering in social networks is due to social influence (contagion) versus homophily (assortative mixing)?
status: open
priority: high
disciplines:
  - social-science
  - network-science
  - sociology
summary: >
  Social network studies routinely find that behaviours, beliefs, and health states
  cluster in networks. This can result from social contagion (friends influencing
  each other) or homophily (similar people choose to associate). Distinguishing these
  requires either experimental evidence or strong observational identification
  strategies. Most studies cannot achieve this, and claims of social contagion for
  depression, obesity, and political attitudes have been disputed on homophily grounds.
systematic_gaps:
  - No observational study design can perfectly distinguish contagion from homophily and latent variable confounding; the problem is mathematically underidentified without experimental variation.
  - Natural experiments exploiting exogenous variation in network formation are rare and specific; generalisation is limited.
  - Online social network studies measure self-reported tie formation which may not reflect the ties relevant for social influence.
last_reviewed: "2026-05-05"
""",

'u-happiness-set-point.yaml': """id: u-happiness-set-point
title: Do individuals have a hedonic set point that pulls subjective wellbeing back to baseline after life events, and can deliberate activities shift it permanently?
status: open
priority: medium
disciplines:
  - social-science
  - psychology
  - economics
summary: >
  The hedonic treadmill hypothesis (Brickman and Campbell, 1971) proposes that
  individuals adapt to positive and negative life events and return to a baseline
  happiness level. Studies of lottery winners and accident victims provided early
  evidence, but long-term longitudinal panel data (BHPS, SOEP, HILDA) show that
  major life events (marriage, bereavement, unemployment) have lasting effects for
  some individuals, contradicting pure set-point theory.
systematic_gaps:
  - Panel attrition in longitudinal happiness studies is non-random, creating selection effects that bias estimates of adaptation.
  - The measurement of subjective wellbeing by single survey items versus multi-item scales gives different adaptation patterns.
  - Individual differences in adaptation rate are large but the predictors of slow versus fast adapters are poorly characterised.
last_reviewed: "2026-05-05"
""",

'u-racial-achievement-gap-mechanisms.yaml': """id: u-racial-achievement-gap-mechanisms
title: What are the causal mechanisms producing persistent racial achievement gaps in education, and which interventions most reliably close them?
status: open
priority: high
disciplines:
  - social-science
  - education-research
  - psychology
summary: >
  Racial achievement gaps in test scores and educational attainment persist in the
  US and other countries despite decades of intervention. Proposed mechanisms include:
  school resource disparities, neighbourhood effects, family wealth gaps, stereotype
  threat, implicit teacher bias, and cultural mismatch. Interventions from school
  desegregation to high-dosage tutoring show variable effects; no single intervention
  reliably closes gaps at scale.
systematic_gaps:
  - The relative contribution of school quality versus neighbourhood environment versus family resources to the achievement gap is not causally identified.
  - Stereotype threat effects on test performance have shown inconsistent replication.
  - Interventions effective in controlled settings often fail to scale due to implementation heterogeneity.
last_reviewed: "2026-05-05"
""",

'u-trust-network-scale.yaml': """id: u-trust-network-scale
title: How does interpersonal trust scale from dyadic to community to institutional levels, and when does network structure facilitate or undermine trust formation?
status: open
priority: medium
disciplines:
  - social-science
  - sociology
  - network-science
summary: >
  Trust enables economic exchange, collective action, and social cohesion. Trust at
  the dyadic level (I trust you) does not simply aggregate to institutional trust.
  Network structure (clustering, transitivity, bridging ties) predicts trust formation
  and maintenance. How trust propagates through social networks and under what
  conditions it collapses is not well modelled.
systematic_gaps:
  - The mapping from interpersonal network structure to generalised social trust (trusting strangers) has no agreed theoretical mechanism.
  - Cross-cultural trust measurement using experimental games (trust game, public goods) versus surveys gives divergent results.
  - The threshold at which network structure shifts from trust-enabling to trust-fragile is not identified.
last_reviewed: "2026-05-05"
""",

'u-stereotype-formation-persistence.yaml': """id: u-stereotype-formation-persistence
title: How do group stereotypes form, persist, and spread, and under what conditions do accurate versus inaccurate stereotypes prevail?
status: open
priority: medium
disciplines:
  - social-science
  - psychology
  - sociology
summary: >
  Stereotypes are generalised beliefs about group members. The question of whether
  stereotypes are accurate summaries of group differences (kernel of truth hypothesis)
  or systematic distortions reflecting prejudice is empirically and normatively
  contested. The mechanisms by which inaccurate stereotypes persist despite
  disconfirming evidence (subtyping, confirmation bias, social transmission biases)
  are identified qualitatively but not quantitatively modelled.
systematic_gaps:
  - Measuring stereotype accuracy requires agreed criteria for which group differences are real versus artefactual, which is itself contested.
  - The social transmission dynamics of stereotypes in networks have not been formally modelled with empirical validation.
  - The conditions under which stereotype correction interventions generalise from laboratory to field are not established.
last_reviewed: "2026-05-05"
""",

'u-inequality-health-pathway.yaml': """id: u-inequality-health-pathway
title: Does income inequality causally harm population health beyond individual poverty effects, and what are the specific pathways?
status: open
priority: medium
disciplines:
  - social-science
  - public-health
  - economics
summary: >
  The Wilkinson-Pickett thesis (The Spirit Level) claims that more unequal societies
  have worse health outcomes for all income groups, not just the poor, suggesting
  that relative deprivation, stress, and social comparison pathways operate beyond
  absolute poverty effects. This claim has been contested on methodological grounds
  (ecological fallacy, country selection, confounding), and the specific causal
  pathways have not been established.
systematic_gaps:
  - Cross-national ecological studies of inequality and health are confounded by correlated country characteristics (culture, institutions, welfare state generosity).
  - Within-country studies using local inequality variation find smaller and less consistent effects than cross-national studies.
  - The proposed biological mechanisms (chronic stress, cortisol, immune dysregulation) linking relative deprivation to health have not been established causally.
last_reviewed: "2026-05-05"
""",
}

print("Creating social-science unknowns...")
for filename, content in social_files.items():
    write(os.path.join(SS, filename), content)
print(f"  Total: {len(social_files)} files\n")

# ────────────────────────────────────────────────────────────────
# 4. ECONOMICS (25 unknowns)
# ────────────────────────────────────────────────────────────────
EC = os.path.join(BASE, 'unknowns-catalog', 'economics')

economics_files = {
'u-business-cycle-prediction-limits.yaml': """id: u-business-cycle-prediction-limits
title: What are the fundamental limits of macroeconomic forecasting, and why do professional forecasters systematically fail to predict recessions in advance?
status: open
priority: high
disciplines:
  - economics
  - macroeconomics
  - forecasting
summary: >
  Business cycle forecasting has poor track records: the IMF, OECD, and central banks
  almost never forecast recessions more than one quarter in advance. Whether this
  reflects fundamental informational limits (efficient markets) or model specification
  failures is debated. Leading indicators (yield curve, credit spreads) predict
  recessions with moderate accuracy but high false positive rates.
systematic_gaps:
  - Whether business cycle forecast failure reflects rational market efficiency or model failure has not been distinguished empirically.
  - Machine learning models trained on historical macro data do not consistently outperform simpler econometric forecasts.
  - The relationship between forecast horizon and uncertainty does not follow calibrated Bayesian prediction in central bank models.
last_reviewed: "2026-05-05"
""",

'u-financial-contagion-network-topology.yaml': """id: u-financial-contagion-network-topology
title: How does the network topology of interbank lending and asset holdings determine systemic risk, and can pre-crisis network measures predict contagion?
status: open
priority: high
disciplines:
  - economics
  - finance
  - network-science
summary: >
  The 2008 financial crisis highlighted that interconnected financial networks
  transmit shocks in ways not captured by aggregate models. Network properties
  (interconnectedness, concentration, leverage) are associated with systemic risk,
  but causal identification of which topological features amplify or dampen contagion
  is not established. Regulatory macroprudential tools based on network analysis
  have not been validated prospectively.
systematic_gaps:
  - The specific network topology (core-periphery vs distributed) that maximises systemic stability is theoretically disputed.
  - Real-time interbank network data is not available to regulators; mapping network exposures requires major data infrastructure.
  - The threshold at which network topology transitions from robust-yet-fragile to unstable has not been identified empirically.
last_reviewed: "2026-05-05"
""",

'u-cryptocurrency-value-store-viability.yaml': """id: u-cryptocurrency-value-store-viability
title: Can cryptocurrencies function as long-term stores of value, and what determines whether any given cryptocurrency survives versus fails?
status: open
priority: medium
disciplines:
  - economics
  - finance
  - monetary-economics
summary: >
  Bitcoin and other cryptocurrencies are proposed as stores of value independent of
  government monetary policy. Their extreme price volatility undermines this function.
  Network effects, regulatory treatment, and energy costs all affect long-term viability.
  Most cryptocurrencies created since 2008 have failed; what determines which survive
  is not understood with sufficient precision to predict.
systematic_gaps:
  - The determinants of cryptocurrency adoption equilibria (multiple equilibria vs winner-take-all) are not established theoretically or empirically.
  - Whether Bitcoin's fixed supply schedule creates deflationary spirals in hypothetical widespread adoption scenarios is debated.
  - Regulatory treatment heterogeneity across jurisdictions prevents clean natural experiments on crypto adoption.
last_reviewed: "2026-05-05"
""",

'u-universal-basic-income-macro-effects.yaml': """id: u-universal-basic-income-macro-effects
title: What are the macroeconomic effects of universal basic income on labour supply, inflation, innovation, and wellbeing at scale?
status: open
priority: high
disciplines:
  - economics
  - public-policy
  - labour-economics
summary: >
  UBI pilot programs (Finland, Kenya, Stockton CA, Manitoba) show positive effects on
  wellbeing and small reductions in labour supply. However, pilots cannot capture
  general equilibrium effects: inflation from demand stimulus, behavioural changes when
  universal rather than targeted, and fiscal sustainability at national scale. The
  macroeconomic effects of a universally implemented UBI at a meaningful income level
  remain unknown.
systematic_gaps:
  - Pilot programs are too small and short to capture general equilibrium price and wage effects.
  - The labour supply elasticity at the extensive (work vs not work) margin at UBI-level income is not known from any real-world implementation.
  - Financing mechanisms (wealth tax, VAT, LVT) have different distributional and macroeconomic consequences not jointly modelled with UBI.
last_reviewed: "2026-05-05"
""",

'u-automation-employment-equilibrium.yaml': """id: u-automation-employment-equilibrium
title: Will automation and AI cause persistent unemployment, or will labour markets adapt through new job creation and sectoral reallocation?
status: open
priority: high
disciplines:
  - economics
  - labour-economics
  - technology-economics
summary: >
  Historical technological displacement has been offset by job creation (Lump of Labour
  Fallacy). Whether AI automation is qualitatively different — displacing cognitive
  work across skill levels simultaneously — is debated. Acemoglu argues current AI is
  automation-biased (replacing labour) rather than labour-complementing. Historical
  agricultural and industrial transitions took decades and caused significant transitional
  unemployment.
systematic_gaps:
  - Distinguishing automation that complements labour from automation that substitutes for it is difficult with available data on job tasks.
  - The speed of AI capability improvement relative to the speed of occupational adaptation is not empirically characterised.
  - General equilibrium effects of widespread AI adoption on wages, prices, and new job creation have not been modelled with sufficient empirical grounding.
last_reviewed: "2026-05-05"
""",

'u-gig-economy-welfare-effects.yaml': """id: u-gig-economy-welfare-effects
title: What are the net welfare effects of gig economy platforms on workers, consumers, and incumbent industries, and how do regulatory regimes affect these?
status: open
priority: medium
disciplines:
  - economics
  - labour-economics
  - industrial-organisation
summary: >
  Gig economy platforms (Uber, Airbnb, TaskRabbit) create value for consumers through
  lower prices and convenience, but their effects on worker welfare are contested.
  Surveys show high satisfaction among gig workers (flexibility) and high instability
  (income volatility, no benefits). Whether gig work complements or substitutes for
  traditional employment and what regulatory framework maximises total welfare is not
  resolved across jurisdictions.
systematic_gaps:
  - Income volatility among gig workers is documented but its welfare cost relative to the value of flexibility is not measured.
  - The effect of gig platforms on incumbent industry wages (taxi drivers, hotel workers) is estimated with inconsistent methods.
  - Regulatory treatments (California AB5, UK Supreme Court ruling, EU Platform Work Directive) vary widely; their comparative welfare effects are not evaluated.
last_reviewed: "2026-05-05"
""",

'u-cbdc-monetary-policy-implications.yaml': """id: u-cbdc-monetary-policy-implications
title: What are the implications of central bank digital currencies for financial stability, monetary policy transmission, and bank disintermediation?
status: open
priority: high
disciplines:
  - economics
  - monetary-economics
  - financial-economics
summary: >
  More than 100 central banks are researching or piloting CBDCs. The implications
  for financial stability are uncertain: CBDCs could disintermediate commercial banks
  (reducing their role in credit creation) or complement them. CBDCs could enable
  new monetary policy tools (negative rates, helicopter money) but could also create
  bank runs during crises as depositors shift to CBDC. China's e-CNY and the Bahamas'
  Sand Dollar provide early data but are not at full macro scale.
systematic_gaps:
  - The bank disintermediation effect of CBDCs depends on design choices (remuneration, holding limits) whose equilibrium consequences are not modelled.
  - Whether CBDCs strengthen or weaken monetary policy transmission depends on assumptions about bank lending behaviour that are contested.
  - Privacy and surveillance implications of CBDC have not been formally included in welfare models.
last_reviewed: "2026-05-05"
""",

'u-housing-affordability-structural-causes.yaml': """id: u-housing-affordability-structural-causes
title: What are the primary structural causes of the housing affordability crisis in high-income cities, and which policy interventions are most effective?
status: open
priority: high
disciplines:
  - economics
  - urban-economics
  - housing-policy
summary: >
  Housing costs in major cities (London, San Francisco, Sydney) have risen much faster
  than incomes for four decades. Proposed causes include zoning restrictions limiting
  supply, low interest rates inflating demand, institutional investment in residential
  property, NIMBYism, and construction cost increases. The relative importance of
  supply versus demand factors and the effectiveness of rent control, upzoning, and
  social housing vary across cities and studies.
systematic_gaps:
  - Natural experiments on zoning reform show heterogeneous effects that are not explained by current supply models.
  - The effect of institutional investor purchasing on housing affordability is estimated inconsistently across studies.
  - Rent control effects on long-run housing supply are contested between economists; empirical estimates span a wide range.
last_reviewed: "2026-05-05"
""",

'u-healthcare-cost-spiral-mechanisms.yaml': """id: u-healthcare-cost-spiral-mechanisms
title: What mechanisms drive persistently rising healthcare costs in high-income countries, and which healthcare system structures most effectively contain them?
status: open
priority: high
disciplines:
  - economics
  - health-economics
  - public-policy
summary: >
  Healthcare costs as a share of GDP have risen persistently in high-income countries.
  Proposed mechanisms include: technological change (Baumol's cost disease meets new
  technology), insurance moral hazard, provider market power, administrative costs, and
  disease burden changes. The US spends twice as much as similarly wealthy countries
  with worse average outcomes; the institutional causes are debated.
systematic_gaps:
  - The decomposition of healthcare cost growth into technological change, price inflation, and volume growth is methodologically contested.
  - Cross-national comparison of healthcare system performance is confounded by measurement differences and case-mix variation.
  - The long-run effects of cost containment policies (DRG payment, global budgets, reference pricing) on innovation and access are not established.
last_reviewed: "2026-05-05"
""",

'u-inequality-growth-relationship.yaml': """id: u-inequality-growth-relationship
title: Does economic inequality promote or retard long-run economic growth, and at what level of inequality does the net effect change sign?
status: open
priority: high
disciplines:
  - economics
  - macroeconomics
  - development-economics
summary: >
  The relationship between inequality and growth is theoretically ambiguous: high
  inequality may promote growth through savings and investment incentives, or retard
  it through demand suppression, political instability, and reduced human capital
  investment. IMF research suggests moderate inequality promotes growth but high
  inequality retards it. The empirical evidence is highly sensitive to estimation
  method, country sample, and time horizon.
systematic_gaps:
  - Cross-country growth regressions with inequality suffer from severe endogeneity and omitted variable problems.
  - The non-linear relationship (inverted U or threshold effect) has been claimed but not robustly established.
  - The distributional position of inequality (bottom vs middle vs top share growth) matters for growth effects but models treat inequality as a single measure.
last_reviewed: "2026-05-05"
""",

'u-trade-war-equilibrium.yaml': """id: u-trade-war-equilibrium
title: What is the long-term equilibrium outcome of escalating trade wars, and under what conditions do countries converge to cooperation versus persistent protection?
status: open
priority: medium
disciplines:
  - economics
  - international-economics
  - game-theory
summary: >
  The 2018-2019 US-China trade war and subsequent escalation provide a natural
  experiment in trade war dynamics, but the long-run equilibrium has not been reached.
  Game-theoretic models predict tit-for-tat escalation converging to a cooperative
  equilibrium (supergame) or a protection trap. The role of domestic political economy
  (protection as voter signalling) versus strategic economic goals (technology
  decoupling) in determining equilibrium is not modelled jointly.
systematic_gaps:
  - The welfare effects of the US-China trade war are estimated with inconsistent methods across studies.
  - Long-run supply chain restructuring responses to tariffs have not been empirically tracked at the sectoral level.
  - The conditions under which trade war escalation de-escalates (negotiated versus unilateral) are not established from historical cases.
last_reviewed: "2026-05-05"
""",

'u-supply-chain-resilience-efficiency.yaml': """id: u-supply-chain-resilience-efficiency
title: What is the optimal tradeoff between supply chain efficiency and resilience, and how has COVID-19 revealed the limits of just-in-time production?
status: open
priority: medium
disciplines:
  - economics
  - operations-research
  - industrial-organisation
summary: >
  COVID-19 disrupted global supply chains in ways that exposed the fragility of
  just-in-time (JIT) production. Firms are re-evaluating inventory, supplier
  diversification, and nearshoring strategies. The optimal tradeoff between cost
  efficiency (lean inventory, long global supply chains) and resilience (buffer stocks,
  redundant suppliers) is not established at either the firm or macro level.
systematic_gaps:
  - The systemic risk premium required to justify supply chain resilience investments is not calculated from empirical disruption data.
  - Whether supply chain reshoring improves national economic security at acceptable cost is not established; estimates span a wide range.
  - Dynamic capabilities models of supply chain adaptation are theoretically developed but empirically tested only in specific industries.
last_reviewed: "2026-05-05"
""",

'u-platform-monopoly-welfare-effects.yaml': """id: u-platform-monopoly-welfare-effects
title: Do digital platform monopolies impose net welfare costs on consumers, and what is the appropriate regulatory framework for two-sided markets?
status: open
priority: high
disciplines:
  - economics
  - industrial-organisation
  - competition-policy
summary: >
  Digital platforms (Google, Amazon, Meta) exhibit strong network effects and economies
  of scale that produce natural monopoly tendencies. Two-sided market theory (Rochet
  and Tirole) shows that traditional antitrust analysis fails when one market side is
  subsidised. Whether platform monopoly power creates consumer harm is disputed:
  services are often free, but monopsony effects on workers and suppliers, and
  innovation suppression through acquisitions, are claimed.
systematic_gaps:
  - Measuring consumer surplus from digital platforms is methodologically contested; revealed preference approaches and contingent valuation diverge widely.
  - Whether killer acquisitions (buying potential competitors) are systematically harmful has not been established; the counterfactual is unobservable.
  - The appropriate market definition for digital platforms is disputed; definitions determine whether market power exists.
last_reviewed: "2026-05-05"
""",

'u-carbon-price-optimal-level.yaml': """id: u-carbon-price-optimal-level
title: What is the optimal carbon price for achieving climate stabilisation goals, and why do economic estimates vary by more than two orders of magnitude?
status: open
priority: high
disciplines:
  - economics
  - environmental-economics
  - climate-economics
summary: >
  Integrated assessment models (Nordhaus DICE, Stern) estimate the social cost of
  carbon (SCC) from $50 to $300+ per tonne, with very wide uncertainty bands. The
  estimates depend critically on discount rate assumptions, damage function
  specifications, and risk aversion parameters. US government SCC estimates vary
  dramatically across administrations. No consensus exists on the appropriate discount
  rate for long-term climate damages.
systematic_gaps:
  - The choice of discount rate alone explains most of the variance in SCC estimates across studies.
  - Damage functions in IAMs are poorly constrained at high temperature levels and are not validated against historical climate-economy relationships.
  - The distribution of climate damages across income groups and nations is not incorporated into social welfare functions in a principled way.
last_reviewed: "2026-05-05"
""",

'u-behavioral-economics-policy-effectiveness.yaml': """id: u-behavioral-economics-policy-effectiveness
title: Which behavioural economics interventions (nudges) generalise robustly across cultural and institutional contexts, and which fail to replicate?
status: open
priority: medium
disciplines:
  - economics
  - behavioural-economics
  - public-policy
summary: >
  Nudge theory (Thaler and Sunstein) proposes that choice architecture interventions
  (defaults, framing, social norms) can improve decisions without restricting freedom
  of choice. High-profile nudge programs (UK Behavioural Insights Team) report
  positive effects, but many laboratory findings fail to replicate at scale in field
  settings. The conditions predicting robust nudge effectiveness are not established.
systematic_gaps:
  - Effect sizes for nudge interventions shrink dramatically from laboratory to field settings, with no agreed explanation.
  - Adaptation and habituation effects reduce nudge effectiveness over time in ways not modelled in most evaluations.
  - The ethical limits of nudging — when does it cross into manipulation — are not agreed normatively or legally.
last_reviewed: "2026-05-05"
""",

'u-sovereign-debt-sustainability.yaml': """id: u-sovereign-debt-sustainability
title: What determines sovereign debt sustainability thresholds, and how can debt crises be predicted before they occur?
status: open
priority: high
disciplines:
  - economics
  - macroeconomics
  - international-finance
summary: >
  Sovereign debt crises occur when governments cannot service debt and lose market
  access. Reinhart and Rogoff's claimed 90 percent debt-to-GDP threshold was shown
  to have coding errors and is rejected by subsequent research. No reliable debt
  sustainability threshold exists; sustainability depends on growth rates, interest
  rates, fiscal balance, and creditor composition in complex ways.
systematic_gaps:
  - Debt sustainability analyses by IMF and World Bank have consistently failed to predict crises in advance.
  - The interest-growth differential (r minus g) is the theoretical driver of debt sustainability, but its future path is not predictable.
  - The distinction between illiquidity-driven and insolvency-driven sovereign crises is diagnostically difficult but determines appropriate policy response.
last_reviewed: "2026-05-05"
""",

'u-pension-demographic-stress.yaml': """id: u-pension-demographic-stress
title: How will demographic aging affect defined-benefit pension systems, and which reform strategies are fiscally sustainable and politically feasible?
status: open
priority: medium
disciplines:
  - economics
  - public-finance
  - demographics
summary: >
  Demographic aging (declining birth rates, rising longevity) threatens pay-as-you-
  go pension systems in most high-income countries. Reform options (raising retirement
  age, increasing contributions, moving to defined contribution, means-testing)
  involve distributional tradeoffs that are politically contested. The fiscal
  sustainability of public pensions under alternative demographic scenarios has been
  modelled but policy reform timelines are uncertain.
systematic_gaps:
  - Long-run demographic projections are sensitive to fertility and immigration assumptions that are inherently uncertain.
  - The political economy of pension reform (who bears costs determines feasibility) is modelled separately from fiscal sustainability.
  - The welfare effects of moving from defined benefit to defined contribution systems on worker lifetime consumption are not established across income groups.
last_reviewed: "2026-05-05"
""",

'u-degrowth-economic-viability.yaml': """id: u-degrowth-economic-viability
title: Can wealthy economies deliberately degrow GDP while maintaining or improving wellbeing, and what are the macroeconomic mechanisms required?
status: open
priority: medium
disciplines:
  - economics
  - ecological-economics
  - macroeconomics
summary: >
  Degrowth advocates argue that rich countries should deliberately reduce economic
  output to stay within planetary boundaries, replacing GDP growth as the policy
  objective with wellbeing metrics. Mainstream economists question whether stable
  no-growth or shrinking economies can maintain full employment, debt servicing,
  and pension obligations. No high-income country has managed a planned degrowth
  transition.
systematic_gaps:
  - Macroeconomic models of stable no-growth economies have been developed theoretically but not validated empirically against real country trajectories.
  - The employment and income distribution effects of targeted degrowth in specific high-footprint sectors are not modelled.
  - International competitiveness effects of unilateral degrowth in an open economy are not estimated.
last_reviewed: "2026-05-05"
""",

'u-innovation-diffusion-s-curve.yaml': """id: u-innovation-diffusion-s-curve
title: Why do some innovations follow S-curve diffusion while others plateau or fail, and can early adoption patterns predict long-run diffusion outcomes?
status: open
priority: medium
disciplines:
  - economics
  - technology-economics
  - innovation-studies
summary: >
  Technology diffusion often follows logistic S-curves (Rogers, 1962), but many
  technologies plateau below full adoption or fail entirely. The drivers of diffusion
  speed and ceiling — network effects, switching costs, complementary infrastructure,
  regulatory environment, and early adopter characteristics — interact in ways that
  make diffusion prediction difficult. Early adoption data has shown some predictive
  value for long-run diffusion but not reliably.
systematic_gaps:
  - Early adoption pattern metrics that reliably predict final market penetration have not been validated across technology domains.
  - The relationship between network effects strength and diffusion ceiling is theoretically predicted but empirically heterogeneous.
  - Why some technologies (electric vehicles, solar panels) suddenly accelerate after decades of slow adoption is not predicted by standard diffusion models.
last_reviewed: "2026-05-05"
""",

'u-post-scarcity-economics-feasibility.yaml': """id: u-post-scarcity-economics-feasibility
title: Can advanced technology enable post-scarcity economics, and what economic institutions are needed when marginal costs approach zero?
status: open
priority: medium
disciplines:
  - economics
  - technology-economics
  - political-economy
summary: >
  Digital goods already have near-zero marginal reproduction costs, creating challenges
  for market pricing. Advanced manufacturing (3D printing, synthetic biology) may
  extend near-zero marginal costs to physical goods. The institutional frameworks
  required to organise production, distribution, and innovation incentives in a
  world of material abundance are not developed beyond theoretical speculation.
systematic_gaps:
  - No economic model of post-scarcity transitions includes both the supply-side (falling marginal costs) and demand-side (evolving preferences) simultaneously.
  - The transition path from market economies to post-scarcity distribution is not modelled for any specific sector.
  - Intellectual property frameworks assume scarcity that is being undermined by digital goods and open-source production; replacement frameworks are not agreed.
last_reviewed: "2026-05-05"
""",

'u-multiplier-fiscal-policy.yaml': """id: u-multiplier-fiscal-policy
title: What is the fiscal multiplier under different economic conditions, and when does government spending crowd out versus crowd in private investment?
status: open
priority: high
disciplines:
  - economics
  - macroeconomics
  - fiscal-policy
summary: >
  The fiscal multiplier — the ratio of change in GDP to change in government
  spending — is central to policy debate but is estimated with wide uncertainty.
  Estimates range from negative (crowding out) to more than 2 depending on methodology,
  economic conditions, type of spending, and monetary policy regime. The multiplier is
  larger at the zero lower bound and in recessions; smaller in open economies and at
  full employment.
systematic_gaps:
  - Identification of fiscal multipliers from observational data requires instruments for government spending that are difficult to construct.
  - The multiplier varies by spending type (infrastructure, transfers, government consumption) but these are not consistently distinguished in empirical estimates.
  - Heterogeneous agent models predict different multipliers for different income groups receiving transfers; aggregate estimates miss this heterogeneity.
last_reviewed: "2026-05-05"
""",

'u-central-bank-independence-effectiveness.yaml': """id: u-central-bank-independence-effectiveness
title: Does central bank independence cause lower inflation, and what are the political economy limits of central bank independence under fiscal dominance?
status: open
priority: medium
disciplines:
  - economics
  - monetary-economics
  - political-economy
summary: >
  The inflation-fighting credentials of independent central banks are credited with
  the Great Moderation (1985-2007). Whether central bank independence causes low
  inflation or merely correlates with institutional quality is not resolved. The
  post-2008 balance sheet expansion and the post-COVID inflation surge raise questions
  about the limits of central bank independence when fiscal policy is dominant.
systematic_gaps:
  - Instrumental variable strategies to identify the causal effect of central bank independence on inflation are not convincing.
  - The conditions under which central bank independence is politically sustainable (financial repression, high debt) are not established.
  - The appropriate division of responsibilities between central banks and fiscal authorities for financial stability is not resolved after 2008.
last_reviewed: "2026-05-05"
""",

'u-financialisation-real-economy-effects.yaml': """id: u-financialisation-real-economy-effects
title: Has the growth of the financial sector relative to GDP produced net economic benefits, or has financialisation harmed real economy investment and growth?
status: open
priority: medium
disciplines:
  - economics
  - financial-economics
  - macroeconomics
summary: >
  Financial sector GDP share rose dramatically in advanced economies since the 1980s.
  Critics argue that financialisation redirected capital from productive investment
  to rent-seeking (Cecchetti and Kharroubi: "Too Much Finance"). Defenders argue
  financial deepening improves capital allocation. The net effect of financial sector
  growth on innovation, investment, and long-run growth is contested, and the causal
  identification challenges are severe.
systematic_gaps:
  - The threshold at which financial deepening turns from growth-enhancing to growth-retarding is estimated inconsistently across studies.
  - Distinguishing productive from rent-seeking financial activity empirically has not been done at the transaction level.
  - The effect of shareholder value maximisation norms (accelerated by financialisation) on long-term corporate investment has not been causally identified.
last_reviewed: "2026-05-05"
""",
}

print("Creating economics unknowns...")
for filename, content in economics_files.items():
    write(os.path.join(EC, filename), content)
print(f"  Total: {len(economics_files)} files\n")

# ────────────────────────────────────────────────────────────────
# 5. COMPUTER-SCIENCE gap fill (10 more)
# ────────────────────────────────────────────────────────────────
CS = os.path.join(BASE, 'unknowns-catalog', 'computer-science')

cs_gap_files = {
'u-p-vs-np-geometric-barrier.yaml': """id: u-p-vs-np-geometric-barrier
title: What geometric or algebraic barriers prevent proof of P != NP, and do known techniques suffice if correctly applied?
status: open
priority: high
disciplines:
  - computational-complexity
  - mathematics
  - theoretical-computer-science
summary: >
  P vs NP is the most famous open problem in computer science. Known barriers
  (relativisation, natural proofs, algebrisation) rule out large classes of proof
  techniques. Whether these barriers cover all conceivable approaches or leave
  a viable path to proof is debated. Recent approaches via circuit lower bounds
  and geometric complexity theory have made progress but no breakthrough.
systematic_gaps:
  - Whether geometric complexity theory can circumvent known barriers is unresolved.
  - The relationship between P vs NP and the structure of the polynomial hierarchy is not fully exploited.
  - No oracle separation completely captures the difficulty of the problem.
last_reviewed: "2026-05-05"
""",

'u-neural-network-generalisation-theory.yaml': """id: u-neural-network-generalisation-theory
title: Why do overparameterised neural networks generalise well despite interpolating training data, contradicting classical statistical learning theory?
status: open
priority: high
disciplines:
  - machine-learning
  - statistical-learning-theory
  - deep-learning
summary: >
  Classical statistical learning theory predicts that models memorising training data
  (interpolating) should not generalise. Deep neural networks routinely interpolate
  training data and still achieve excellent test performance. Proposed explanations
  include implicit regularisation from gradient descent, benign overfitting, double
  descent, and the inductive biases of specific architectures. No unified theory
  explains generalisation across network types and data regimes.
systematic_gaps:
  - Pac-Bayes and margin-based bounds are not tight enough to explain the generalisation of practical deep networks.
  - The implicit regularisation of gradient descent has been characterised for linear models but not for non-linear networks.
  - Double descent curves have been observed empirically but their theoretical explanation does not generalise across architectures.
last_reviewed: "2026-05-05"
""",

'u-transformer-scaling-law-limits.yaml': """id: u-transformer-scaling-law-limits
title: When and why do Chinchilla scaling laws break down, and what architectural innovations can improve compute efficiency beyond current scaling predictions?
status: open
priority: high
disciplines:
  - machine-learning
  - deep-learning
  - natural-language-processing
summary: >
  Chinchilla scaling laws (Hoffmann et al. 2022) predict optimal compute allocation
  between model size and training tokens. These laws have been widely adopted but their
  applicability beyond language modelling, their breakdown at extreme scales, and
  the architectural innovations that could break them are not well understood.
  Mixture-of-experts, state space models, and sparse attention challenge the
  dense-transformer assumption underlying current scaling predictions.
systematic_gaps:
  - Scaling laws for multimodal, embodied, and reinforcement learning models have not been established.
  - The quality of training data (not just quantity) breaks scaling law predictions in ways not formalised.
  - Whether architectural improvements can shift the compute-efficiency frontier beyond current predictions is not predictable.
last_reviewed: "2026-05-05"
""",

'u-robustness-distribution-shift.yaml': """id: u-robustness-distribution-shift
title: What training and architectural modifications make machine learning models robust to real-world distribution shift, and how much robustness is achievable?
status: open
priority: high
disciplines:
  - machine-learning
  - robust-statistics
  - computer-vision
summary: >
  ML models trained on one distribution fail on shifted test distributions (different
  hospitals, weather conditions, demographic groups). Proposed solutions include:
  data augmentation, domain adaptation, invariant risk minimisation, and causal
  methods. None achieves robustness across the range of shifts encountered in deployment.
  The gap between in-distribution and out-of-distribution performance is a fundamental
  limitation of current ML.
systematic_gaps:
  - No training method consistently improves OOD performance across diverse shift types (covariate, label, and concept shift) simultaneously.
  - Benchmarks for distribution robustness are not standardised; results are not comparable across papers.
  - The theoretical conditions under which a model trained on one distribution can generalise to another are known only for specific model classes.
last_reviewed: "2026-05-05"
""",

'u-algorithm-discovery-automation.yaml': """id: u-algorithm-discovery-automation
title: Can machine learning systems autonomously discover novel algorithms and mathematical proofs beyond human-designed heuristics?
status: open
priority: high
disciplines:
  - machine-learning
  - algorithms
  - automated-theorem-proving
summary: >
  AlphaCode, FunSearch, and AlphaProof demonstrate that ML can solve competition
  programming problems and formalise some mathematical proofs. Whether these systems
  generalise to discovering novel algorithms for previously unsolved problems — rather
  than interpolating patterns from training data — is unclear. The boundary between
  pattern matching and genuine algorithmic discovery has not been established.
systematic_gaps:
  - Current ML-based algorithm discovery systems do not generalise to problems structurally different from training instances.
  - The formal relationship between training data coverage and discoverable algorithm complexity has not been characterised.
  - Automated theorem proving has not cracked any of the major open mathematical conjectures despite advances.
last_reviewed: "2026-05-05"
""",

'u-federated-learning-privacy-utility.yaml': """id: u-federated-learning-privacy-utility
title: What is the fundamental tradeoff between differential privacy guarantees and model utility in federated learning, and how close are current implementations to the Pareto frontier?
status: open
priority: medium
disciplines:
  - machine-learning
  - privacy
  - distributed-computing
summary: >
  Federated learning enables training on distributed data without sharing raw data.
  Differential privacy (DP) provides formal privacy guarantees at the cost of model
  utility. The fundamental Pareto frontier between privacy budget (epsilon) and
  utility loss is not known for realistic federated learning settings. Current
  implementations achieve mediocre utility at reasonable privacy budgets compared
  to centralised training.
systematic_gaps:
  - The optimal noise mechanism for federated DP learning (Gaussian, Laplace, Skellam) depends on model architecture and has not been systematically compared.
  - Client-level versus sample-level DP have different privacy semantics and utility costs not jointly analysed across applications.
  - Inference attacks on federated models (gradient inversion, membership inference) have outpaced defence development in realistic settings.
last_reviewed: "2026-05-05"
""",

'u-graph-algorithm-quantum-speedup.yaml': """id: u-graph-algorithm-quantum-speedup
title: Which graph algorithms admit quantum speedup beyond classical near-linear time complexity, and what are the practical costs of quantum graph computation?
status: open
priority: medium
disciplines:
  - quantum-computing
  - algorithms
  - graph-theory
summary: >
  Quantum speedups for graph algorithms are known for specific problems (element
  distinctness, triangle finding) but the general picture is incomplete. For many
  fundamental graph problems (connectivity, shortest path, matching), quantum speedups
  are modest or unproven. The practical overhead of quantum graph computation
  (state preparation, readout) often overwhelms theoretical speedups at realistic
  graph sizes.
systematic_gaps:
  - Quantum speedup for maximum flow and minimum cut in general graphs has not been established beyond specific graph families.
  - The quantum query complexity of fundamental graph properties is unknown for several important cases.
  - Practical quantum graph computation requires efficient quantum RAM (QRAM) whose implementation is not feasible at scale.
last_reviewed: "2026-05-05"
""",

'u-program-synthesis-completeness.yaml': """id: u-program-synthesis-completeness
title: Can program synthesis systems automatically generate programs from specifications for any computable function, and what are the practical limits?
status: open
priority: medium
disciplines:
  - computer-science
  - formal-methods
  - machine-learning
summary: >
  Program synthesis — automatically generating code from a specification (input-output
  examples, natural language, formal assertions) — has advanced dramatically with
  LLMs. The theoretical question of whether synthesis is complete (can generate any
  program from sufficient specification) is trivially yes; the practical question
  of what specification detail and compute is required for useful programs in
  different domains is not answered.
systematic_gaps:
  - The sample complexity of synthesis (how many input-output examples are needed) as a function of program complexity is not characterised.
  - Verifying that synthesised programs are correct for all inputs rather than just specified examples requires formal verification not integrated into current synthesis pipelines.
  - Synthesised programs fail on distribution shift from the specification; robustness of synthesis is not measured.
last_reviewed: "2026-05-05"
""",

'u-cache-efficient-algorithm-design.yaml': """id: u-cache-efficient-algorithm-design
title: Can memory hierarchy-aware algorithm design principles be formalised to automatically optimise cache efficiency across heterogeneous hardware?
status: open
priority: medium
disciplines:
  - computer-science
  - algorithms
  - computer-architecture
summary: >
  Modern computer performance is increasingly dominated by memory access latency rather
  than arithmetic operations. Cache-oblivious algorithms are designed without knowledge
  of cache parameters and are provably optimal in cache complexity. However, for
  modern hardware with multiple cache levels, NUMA architectures, and GPU memory
  hierarchies, no unified framework automatically derives cache-optimal algorithms
  for general computations.
systematic_gaps:
  - Cache-oblivious analysis applies only to simple two-level memory models; generalisation to real multi-level hierarchies is unsolved.
  - Automatic code generation that is cache-efficient across x86, ARM, and GPU architectures requires hardware-specific knowledge not captured in any abstract model.
  - The tradeoff between cache efficiency and algorithmic parallelism in heterogeneous computing environments is not formalised.
last_reviewed: "2026-05-05"
""",

'u-emergent-capabilities-llm-prediction.yaml': """id: u-emergent-capabilities-llm-prediction
title: Are emergent capabilities in large language models predictable from scaling laws, or do they represent genuine phase transitions in capability space?
status: open
priority: high
disciplines:
  - machine-learning
  - deep-learning
  - natural-language-processing
summary: >
  Large language models exhibit emergent capabilities — abilities not present at
  smaller scale that appear abruptly as model size increases. Whether these are genuine
  phase transitions in model capability or artifacts of evaluation metric nonlinearity
  is debated (Schaeffer et al. argue they are metric artifacts). If emergent capabilities
  are real phase transitions, predicting which capabilities will emerge at what scale
  is critical for AI safety planning.
systematic_gaps:
  - The methodology for measuring emergence is disputed; Schaeffer et al. show many emergent capabilities disappear with continuous evaluation metrics.
  - No mechanistic theory predicts which capabilities will emerge at which scale.
  - Cross-model and cross-architecture comparisons of emergence are confounded by different training regimes and data.
last_reviewed: "2026-05-05"
""",
}

print("Creating computer-science gap files...")
for filename, content in cs_gap_files.items():
    write(os.path.join(CS, filename), content)
print(f"  Total: {len(cs_gap_files)} files\n")

# ────────────────────────────────────────────────────────────────
# 6. NEUROSCIENCE gap fill (10 more)
# ────────────────────────────────────────────────────────────────
NS = os.path.join(BASE, 'unknowns-catalog', 'neuroscience')

neuro_gap_files = {
'u-default-mode-network-function.yaml': """id: u-default-mode-network-function
title: What is the functional role of the default mode network, and why is it suppressed during externally directed tasks?
status: open
priority: medium
disciplines:
  - neuroscience
  - cognitive-science
  - neuroimaging
summary: >
  The default mode network (DMN) is a set of cortical regions (medial prefrontal
  cortex, posterior cingulate, angular gyrus) that are active during rest and suppressed
  during externally directed attention. Proposed functions include self-referential
  thought, mind-wandering, episodic memory retrieval, prospective thinking, and
  social cognition. The mechanistic role of DMN activity in these functions is
  not established.
systematic_gaps:
  - The causal role of DMN activity versus associated activity cannot be established by fMRI correlations alone.
  - DMN disruption in Alzheimer's, depression, and schizophrenia is documented but whether it is a cause or consequence is not known.
  - The relationship between DMN activity and conscious experience has not been formalised.
last_reviewed: "2026-05-05"
""",

'u-neuroplasticity-adult-limits.yaml': """id: u-neuroplasticity-adult-limits
title: What are the molecular and circuit mechanisms that limit neuroplasticity in the adult brain, and how can they be safely reopened?
status: open
priority: high
disciplines:
  - neuroscience
  - cellular-neuroscience
  - clinical-neuroscience
summary: >
  Critical periods of heightened plasticity close after early development, limiting
  recovery from sensory deprivation, brain injury, and psychiatric disorders. Molecular
  brakes on plasticity include PNNs (perineuronal nets), myelin-associated inhibitors,
  and reduced BDNF. Interventions that reopen plasticity windows (fluoxetine, dark
  rearing, tPA) have shown promise in animals but their mechanisms and safe clinical
  translation are not established.
systematic_gaps:
  - The molecular triggers for critical period closure vary across brain regions and have not been unified in a single mechanistic model.
  - Reopening plasticity in adult animals can improve function in some paradigms but cause regression in others; net effects are unpredictable.
  - Human critical period timing for different functions (language, face processing, social cognition) is not precisely mapped.
last_reviewed: "2026-05-05"
""",

'u-attention-neural-mechanisms.yaml': """id: u-attention-neural-mechanisms
title: What are the neural circuit mechanisms by which top-down attention selects and enhances sensory signals, and does attention act by gain, timing, or noise reduction?
status: open
priority: medium
disciplines:
  - neuroscience
  - cognitive-science
  - systems-neuroscience
summary: >
  Top-down attention improves perceptual performance, but the neural mechanisms
  are debated. Competing models posit: multiplicative gain enhancement (response
  scaling), synchronisation of neural oscillations (gamma range) enabling read-out,
  noise reduction through suppressing competing representations, and dynamic routing.
  Invasive recordings in non-human primates and human EEG/MEG show evidence for
  multiple mechanisms that may interact.
systematic_gaps:
  - The relative contributions of gain, noise reduction, and temporal synchronisation to attention effects have not been dissociated in a single experimental paradigm.
  - The attentional locus of selection (early sensory vs later decision stages) is disputed for different attentional types (spatial, feature, object).
  - Neuromodulatory basis of attention (acetylcholine, norepinephrine) has been established pharmacologically but circuit-level mechanisms are not known.
last_reviewed: "2026-05-05"
""",

'u-emotion-discrete-vs-constructed.yaml': """id: u-emotion-discrete-vs-constructed
title: Are emotions discrete natural kinds with distinct neural signatures, or are they constructed from more basic affective and cognitive building blocks?
status: open
priority: medium
disciplines:
  - neuroscience
  - psychology
  - affective-science
summary: >
  Basic emotion theory (Ekman) proposes that a small number of discrete emotions
  (fear, anger, happiness, sadness, disgust, surprise) have universal facial
  expressions and distinct neural circuits. Constructivist emotion theory (Barrett)
  argues emotions are constructed from core affect (valence + arousal) and cultural
  concepts, with no emotion-specific neural modules. The neuroimaging literature
  is inconsistent between theories.
systematic_gaps:
  - Meta-analyses of neuroimaging studies show no consistent emotion-specific patterns; regions claimed as emotion-specific activate across multiple functions.
  - Universal facial expression claims fail cross-cultural replication in some studies, supporting constructivist accounts.
  - A unified computational model of emotion that predicts both neural and behavioural data has not been developed.
last_reviewed: "2026-05-05"
""",

'u-cerebellum-cognitive-function.yaml': """id: u-cerebellum-cognitive-function
title: What cognitive functions does the cerebellum perform beyond motor coordination, and what is its computational principle?
status: open
priority: medium
disciplines:
  - neuroscience
  - cognitive-science
  - systems-neuroscience
summary: >
  The cerebellum contains more neurons than the rest of the brain and has long been
  considered purely motor. Recent evidence implicates cerebellum in working memory,
  language, attention, and social cognition. Cerebellar damage causes cognitive
  affective syndrome. The internal forward model (Wolpert) computational principle
  of the cerebellum may extend to predicting cognitive and emotional events, but
  this has not been established.
systematic_gaps:
  - The cognitive functions attributed to the cerebellum are based primarily on connectivity and lesion studies; the causal role is not established.
  - Cerebellar predictions of non-motor events have not been directly measured; the forward model is inferred from motor behaviour.
  - The role of the cerebellum in autism spectrum condition (cerebellar abnormalities are common) is not mechanistically understood.
last_reviewed: "2026-05-05"
""",

'u-engram-molecular-basis.yaml': """id: u-engram-molecular-basis
title: What are the molecular and synaptic mechanisms that store specific memories in engram cells, and how are they maintained over decades?
status: open
priority: high
disciplines:
  - neuroscience
  - cellular-neuroscience
  - molecular-biology
summary: >
  Engram cells — the sparse population of neurons that store a specific memory —
  have been identified using activity-based labelling (TRAP, CANE) in mice. The
  molecular mechanisms by which synaptic strength changes encode information in
  engram cells include AMPAR trafficking, spine morphology changes, and transcriptional
  programs. How these molecular changes persist for decades against protein turnover
  is not resolved.
systematic_gaps:
  - The problem of molecular maintenance (proteins turn over in weeks; memories last decades) has no agreed solution; candidates include RNA-binding proteins and PKMzeta.
  - Engram cell reactivation is sufficient to drive memory recall in mice, but the neural code translating engram activity into specific memory content is not known.
  - Whether engrams are localised to single cells or distributed across neural ensembles is not resolved for complex (semantic, episodic) memories.
last_reviewed: "2026-05-05"
""",

'u-interoception-consciousness-link.yaml': """id: u-interoception-consciousness-link
title: How does interoceptive signalling from body organs contribute to emotional experience and conscious self-awareness?
status: open
priority: medium
disciplines:
  - neuroscience
  - cognitive-science
  - affective-neuroscience
summary: >
  Interoception — sensing the physiological state of the body — is processed in
  insular cortex and cingulate cortex. Predictive interoception theories (Friston,
  Barrett) propose that the brain constantly predicts body states and that deviations
  from predictions generate conscious feelings. The causal role of interoceptive
  signals in generating subjective emotional experience versus merely accompanying
  it is not established.
systematic_gaps:
  - The predictive coding account of interoception makes quantitative predictions but lacks experimental designs that could falsify it.
  - Individual differences in interoceptive accuracy correlate with emotional and psychiatric outcomes, but causality has not been established.
  - How interoceptive signals are integrated with exteroceptive perception to generate a unified sense of self is not modelled computationally.
last_reviewed: "2026-05-05"
""",

'u-synapse-heterogeneity-function.yaml': """id: u-synapse-heterogeneity-function
title: What is the functional significance of the enormous molecular heterogeneity of synapses, and does synapse-type diversity encode information?
status: open
priority: medium
disciplines:
  - neuroscience
  - molecular-neuroscience
  - cellular-neuroscience
summary: >
  Synapses are now known to be molecularly heterogeneous even between the same
  neurons, with thousands of protein components varying in copy number. This
  heterogeneity may encode fine-grained synaptic strength differences, serve
  regulatory functions, or be irrelevant noise. Connectome studies in C. elegans
  show that synaptic number and strength between specific neurons correlates with
  behaviour, but mammalian synapse diversity exceeds worm synapses by orders of
  magnitude.
systematic_gaps:
  - High-throughput synaptic proteomics can measure molecular composition but cannot map this to physiological strength in living tissue.
  - The information storage capacity of synapse heterogeneity versus synaptic strength alone has not been estimated from experimental data.
  - Whether synapse molecular heterogeneity is actively regulated (a code) or a consequence of stochastic protein assembly is not established.
last_reviewed: "2026-05-05"
""",

'u-neuroinflammation-depression-causality.yaml': """id: u-neuroinflammation-depression-causality
title: Does neuroinflammation causally drive major depressive disorder, and can anti-inflammatory treatments reliably treat depression in inflammation-high patients?
status: open
priority: high
disciplines:
  - neuroscience
  - psychiatry
  - immunology
summary: >
  Elevated inflammatory markers (CRP, IL-6, TNF-alpha) are found in a subset of
  depressed patients, and the inflammatory cytokine hypothesis proposes that
  neuroinflammation drives depressive symptoms via sickness behaviour pathways
  (microglia, tryptophan catabolism, HPA axis). Anti-inflammatory trials (COX-2
  inhibitors, cytokine antagonists) show heterogeneous results. Whether inflammation
  is a cause or consequence of depression, and which patients benefit from
  anti-inflammatory treatment, is not established.
systematic_gaps:
  - Reverse causation (depression causing inflammation through behaviour, stress, obesity) cannot be ruled out in observational studies.
  - Anti-inflammatory trials show benefit only in inflammation-high subgroups; biomarker stratification is not standardised.
  - The neural circuit mechanisms by which peripheral inflammation alters mood are only partially characterised.
last_reviewed: "2026-05-05"
""",

'u-brain-organoid-validity.yaml': """id: u-brain-organoid-validity
title: How well do cerebral organoids model human brain development and disease, and what are the limits of their validity as research models?
status: open
priority: medium
disciplines:
  - neuroscience
  - developmental-biology
  - stem-cell-biology
summary: >
  Brain organoids grown from induced pluripotent stem cells recapitulate aspects of
  human cortical development including cell type diversity and lamination. They are
  proposed as models for autism, schizophrenia, microcephaly, and COVID-19
  neurological effects. The lack of vascularisation limits organoid size and creates
  hypoxic cores; the absence of glia, immune cells, and peripheral input limits
  functional similarity to real brains.
systematic_gaps:
  - The correspondence between organoid transcriptome and fetal brain transcriptome at equivalent developmental stages has been quantified but its functional implications are unclear.
  - Disease-relevant organoid phenotypes are often subtle and not reproducible across labs using different protocols.
  - The ethical status of organoids exhibiting neural activity patterns similar to preterm infants has not been resolved.
last_reviewed: "2026-05-05"
""",
}

print("Creating neuroscience gap files...")
for filename, content in neuro_gap_files.items():
    write(os.path.join(NS, filename), content)
print(f"  Total: {len(neuro_gap_files)} files\n")

# ────────────────────────────────────────────────────────────────
# 7. ECOLOGY gap fill (8 more)
# ────────────────────────────────────────────────────────────────
EL = os.path.join(BASE, 'unknowns-catalog', 'ecology')

ecology_gap_files = {
'u-species-abundance-distribution.yaml': """id: u-species-abundance-distribution
title: Why do species abundance distributions follow log-normal or log-series patterns across ecosystems, and what does this reveal about assembly rules?
status: open
priority: medium
disciplines:
  - ecology
  - macroecology
  - statistical-ecology
summary: >
  In most sampled ecological communities, a few species are abundant and most are
  rare, producing characteristic species abundance distributions (SADs). Whether SADs
  reflect neutral processes (Hubbell's unified neutral theory), niche differentiation,
  or statistical sampling is debated. The mechanistic origin of the near-universality
  of log-normal SADs across taxonomic groups and environments is not resolved.
systematic_gaps:
  - Neutral theory and niche theory predict similar SADs but have different species-area and species-time predictions not consistently tested.
  - Sampling effects (insufficient survey effort) confound SAD measurement in most community datasets.
  - How SADs change with environmental degradation and whether they serve as indicators of ecosystem health is not established.
last_reviewed: "2026-05-05"
""",

'u-range-shift-pace-climate-change.yaml': """id: u-range-shift-pace-climate-change
title: Can species track climate change fast enough to avoid extinction, and what determines the rate of range shifts?
status: open
priority: high
disciplines:
  - ecology
  - conservation-biology
  - climate-ecology
summary: >
  As climate warms, species ranges are predicted to shift poleward and to higher
  elevation. Observed range shifts average 6-17 km per decade but vary enormously.
  The factors determining whether species track climate (dispersal ability, habitat
  connectivity, plasticity, evolutionary adaptation) interact in ways that make
  prediction very uncertain at the species level.
systematic_gaps:
  - The relative contribution of dispersal limitation versus niche limitation to observed range shift rates has not been separated.
  - Rapid evolutionary adaptation (rather than range shift) to climate change has been documented in few species and its prevalence is unknown.
  - Connectivity of habitat for range shifting is projected to decline as land use and climate change interact, but threshold connectivity requirements are not established.
last_reviewed: "2026-05-05"
""",

'u-soil-microbiome-carbon-cycling.yaml': """id: u-soil-microbiome-carbon-cycling
title: How does soil microbial community composition determine carbon turnover rates, and can manipulating microbiomes enhance soil carbon sequestration?
status: open
priority: high
disciplines:
  - ecology
  - soil-ecology
  - biogeochemistry
summary: >
  Soils contain more carbon than the atmosphere and all living plants combined. Soil
  microbial communities decompose organic matter and determine whether carbon is
  mineralised to CO2 or stabilised in mineral-organic associations. The relationship
  between microbial diversity, community composition, and carbon cycling rates is
  poorly understood, limiting Earth system model predictions.
systematic_gaps:
  - The relative importance of microbial community composition versus environmental conditions (temperature, moisture, pH) in controlling carbon turnover rates is not resolved.
  - Microbial carbon use efficiency (fraction of consumed carbon retained in biomass vs respired) varies widely but its determinants are not established.
  - Whether targeted manipulation of soil microbiomes can reliably increase carbon sequestration without unintended consequences has not been demonstrated.
last_reviewed: "2026-05-05"
""",

'u-predator-prey-oscillation-damping.yaml': """id: u-predator-prey-oscillation-damping
title: Why do observed predator-prey cycles in nature dampen, shift phase, or stop, contrary to Lotka-Volterra predictions of persistent oscillations?
status: open
priority: medium
disciplines:
  - ecology
  - population-ecology
  - mathematical-biology
summary: >
  Lotka-Volterra equations predict persistent predator-prey oscillations, but
  real populations show damped, irregular, or absent cycles. Observed cycles (lynx-hare,
  wolf-elk) vary in amplitude and period across time and space in ways not predicted
  by simple models. Additions of spatial heterogeneity, age structure, multiple prey,
  and stochastic effects each partially explain deviations but a general theory is lacking.
systematic_gaps:
  - Distinguishing deterministic cycles from stochastic fluctuations with similar power spectra requires long time series not available for most systems.
  - The relative importance of trophic (food) versus non-trophic (habitat) factors in shaping cycle amplitude is not established.
  - Spatial coupling of populations through dispersal can synchronise or dampen cycles in ways that depend on landscape structure not captured in point models.
last_reviewed: "2026-05-05"
""",

'u-metacommunity-dispersal-diversity.yaml': """id: u-metacommunity-dispersal-diversity
title: How does dispersal rate interact with local and regional processes to determine metacommunity diversity, and when does dispersal enhance versus homogenise communities?
status: open
priority: medium
disciplines:
  - ecology
  - metacommunity-ecology
  - biogeography
summary: >
  Metacommunity theory predicts that intermediate dispersal rates maximise regional
  diversity (mass effects, rescue effects), while too little dispersal leads to local
  extinctions and too much dispersal homogenises communities. Empirical tests across
  different organism types and spatial scales show inconsistent support for these
  predictions. The conditions determining the dispersal regime of a given metacommunity
  are not well characterised.
systematic_gaps:
  - Estimating actual dispersal rates in natural metacommunities is methodologically very difficult; most tests use proxies.
  - The metacommunity theory framework assumes fixed environments; climate change dynamically alters dispersal-diversity relationships in unmodelled ways.
  - Different metacommunity paradigms (species sorting, patch dynamics, mass effects, neutral) make similar predictions in many scenarios; distinguishing them requires data not typically collected.
last_reviewed: "2026-05-05"
""",

'u-rewilding-ecosystem-outcomes.yaml': """id: u-rewilding-ecosystem-outcomes
title: Do rewilding initiatives restore ecosystem function and self-regulation, and which reintroduced species produce the largest trophic cascade effects?
status: open
priority: high
disciplines:
  - ecology
  - conservation-ecology
  - restoration-ecology
summary: >
  Rewilding — reintroducing large herbivores, predators, and natural disturbance
  regimes — is proposed as a scalable approach to ecological restoration. The
  reintroduction of wolves to Yellowstone produced documented trophic cascades, but
  whether these generalise to other rewilding contexts is debated. Outcomes depend
  on landscape context, prey community composition, and human land use conflicts
  that vary widely.
systematic_gaps:
  - The conditions under which top predator reintroduction produces measurable trophic cascades versus negligible effects are not predictable in advance.
  - Long-term (>20 year) outcomes of rewilding projects have not been systematically evaluated.
  - The socioeconomic conditions under which rewilding is politically sustainable are not established.
last_reviewed: "2026-05-05"
""",

'u-ocean-acidification-ecosystem-effects.yaml': """id: u-ocean-acidification-ecosystem-effects
title: How will ocean acidification affect marine ecosystem structure and functioning, and which species and communities are most vulnerable?
status: open
priority: high
disciplines:
  - ecology
  - marine-ecology
  - climate-ecology
summary: >
  Ocean pH has declined from 8.2 to 8.1 since the industrial revolution and is
  projected to reach 7.8-7.9 by 2100. Calcifying organisms (corals, molluscs, some
  plankton) are physiologically vulnerable, but responses vary widely across taxa
  and individuals. Community-level effects propagate through food webs in ways not
  captured by single-species experiments.
systematic_gaps:
  - The synergistic effects of acidification, warming, and deoxygenation on marine communities are not modelled; most experiments manipulate one variable.
  - Evolutionary adaptation to ocean acidification operates on timescales potentially comparable to the acidification rate but is not included in projections.
  - The economic valuation of marine ecosystem service losses from acidification is not established.
last_reviewed: "2026-05-05"
""",

'u-fire-regime-ecological-threshold.yaml': """id: u-fire-regime-ecological-threshold
title: What determines fire regime thresholds in different ecosystems, and at what fuel load and climate conditions do ecosystems cross from fire-maintained to fire-transformed states?
status: open
priority: high
disciplines:
  - ecology
  - fire-ecology
  - climate-ecology
summary: >
  Fire is a major driver of global vegetation distribution. Fire regimes (frequency,
  severity, spatial extent) are shifting with climate change. Threshold behaviour
  in fire regimes — abrupt transitions from low-frequency surface fire to high-
  frequency crown fire, or from fire-maintained savanna to closed forest — determines
  vegetation state and carbon storage. Predicting when and where these thresholds
  will be crossed under climate change is not possible with current models.
systematic_gaps:
  - The fuel accumulation rate and moisture deficit required for threshold transitions are ecosystem-specific and not generalised.
  - Feedback between fire, vegetation, and soil carbon alters fire regimes in ways that create non-linear dynamics not included in vegetation models.
  - Human fire suppression and prescribed burning interact with climate drivers in ways that are not predictable from physical models alone.
last_reviewed: "2026-05-05"
""",
}

print("Creating ecology gap files...")
for filename, content in ecology_gap_files.items():
    write(os.path.join(EL, filename), content)
print(f"  Total: {len(ecology_gap_files)} files\n")

# ────────────────────────────────────────────────────────────────
# 8. CHEMISTRY gap fill (6 more)
# ────────────────────────────────────────────────────────────────
CH = os.path.join(BASE, 'unknowns-catalog', 'chemistry')

chemistry_gap_files = {
'u-reaction-mechanism-automated-discovery.yaml': """id: u-reaction-mechanism-automated-discovery
title: Can automated computational methods reliably discover novel reaction mechanisms and predict activation barriers without experimental calibration?
status: open
priority: medium
disciplines:
  - chemistry
  - computational-chemistry
  - machine-learning
summary: >
  Automated reaction mechanism discovery (AFIR, RMSD-PP, CREST, machine-learning
  potentials) has advanced dramatically. Whether these methods can reliably explore
  reaction space for complex systems (enzymatic, heterogeneous catalysis, solvation)
  without human guidance or experimental calibration is not established. Neural
  network potentials trained on DFT data are fast but may fail for transition states
  not represented in training data.
systematic_gaps:
  - Machine learning potentials for reaction mechanism search extrapolate poorly to transition state geometries not well represented in training sets.
  - The combinatorial explosion of possible reaction pathways in complex mixtures makes exhaustive automated exploration computationally infeasible.
  - Validation of computationally predicted mechanisms against experiment is hampered by the difficulty of directly observing transition states.
last_reviewed: "2026-05-05"
""",

'u-supramolecular-self-assembly-prediction.yaml': """id: u-supramolecular-self-assembly-prediction
title: Can the self-assembly of supramolecular structures be predicted from molecular building block properties, and what determines assembly pathway selectivity?
status: open
priority: medium
disciplines:
  - chemistry
  - supramolecular-chemistry
  - materials-science
summary: >
  Supramolecular self-assembly produces structures with emergent properties from
  non-covalent interactions. Predicting which structures will form from a given set
  of building blocks, under what conditions, and through which kinetic pathway
  (thermodynamic vs kinetic product) is not reliable. Machine learning approaches
  have improved structural prediction but do not capture pathway selectivity.
systematic_gaps:
  - Kinetic versus thermodynamic control of self-assembly has been characterised for specific systems but no general rules exist.
  - The effect of minor impurities on self-assembly outcomes is not incorporated into predictive models.
  - Hierarchical self-assembly (nano- to macro-scale) cannot be predicted by any current simulation method due to timescale bridging challenges.
last_reviewed: "2026-05-05"
""",

'u-atmospheric-chemistry-aerosol-nucleation.yaml': """id: u-atmospheric-chemistry-aerosol-nucleation
title: What are the molecular mechanisms of atmospheric new particle formation, and which trace species drive nucleation under different atmospheric conditions?
status: open
priority: high
disciplines:
  - chemistry
  - atmospheric-chemistry
  - environmental-chemistry
summary: >
  New particle formation (NPF) in the atmosphere converts gaseous precursors into
  cloud condensation nuclei, affecting climate through cloud formation. Sulfuric acid
  plus amines and highly oxygenated molecules (HOMs) from terpene oxidation are
  known nucleation drivers, but the quantitative contributions of different precursor
  combinations under diverse atmospheric conditions are not established. CLOUD
  experiments at CERN have clarified some mechanisms but real-atmosphere conditions
  involve greater chemical complexity.
systematic_gaps:
  - The identity and concentration of all nucleating agents under ambient conditions are not measured in most atmospheric environments.
  - HOMs from biogenic versus anthropogenic sources contribute differently to NPF but are not distinguished by current atmospheric models.
  - The timescale from nucleation to cloud condensation nucleus activation is not accurately represented in global climate models.
last_reviewed: "2026-05-05"
""",

'u-electrochemical-co2-reduction-selectivity.yaml': """id: u-electrochemical-co2-reduction-selectivity
title: What determines product selectivity in electrochemical CO2 reduction, and can catalyst design achieve multicarbon product yields practical for carbon utilisation?
status: open
priority: high
disciplines:
  - chemistry
  - electrochemistry
  - catalysis
summary: >
  Electrochemical CO2 reduction (CO2RR) converts waste CO2 into useful chemicals
  (CO, formate, ethylene, ethanol) using renewable electricity. Copper catalysts can
  produce multicarbon products but with low selectivity. The atomic-scale mechanisms
  determining product selectivity — C-C coupling, proton-coupled electron transfer
  steps, local pH effects — are disputed. Achieving industrially relevant selectivity
  and current density simultaneously has not been demonstrated.
systematic_gaps:
  - The active site structure of copper under CO2RR conditions is dynamic and not fully characterised by operando spectroscopy.
  - Competing hydrogen evolution reduces faradaic efficiency for CO2RR products; the mechanism of HER suppression by CO2RR catalysts is not fully understood.
  - Scale-up from laboratory cell to industrial electrolyser introduces mass transport, flooding, and durability challenges not captured in small-scale experiments.
last_reviewed: "2026-05-05"
""",

'u-protein-protein-interaction-design.yaml': """id: u-protein-protein-interaction-design
title: Can computational protein-protein interface design reliably produce binders with nanomolar affinity to any target protein surface?
status: open
priority: high
disciplines:
  - chemistry
  - biochemistry
  - structural-biology
summary: >
  RFdiffusion and ProteinMPNN have dramatically improved computational protein
  binder design, achieving nanomolar binders against some targets without experimental
  screening. Whether these methods generalise to all target surfaces (including flat,
  flexible, or charged interfaces) and whether computationally designed binders retain
  affinity in cellular contexts is not established.
systematic_gaps:
  - Computational binder design success rates drop dramatically for non-concave target surfaces (flat or convex epitopes).
  - Designed binders validated in vitro often fail in cell-based assays due to off-target interactions, aggregation, or cellular uptake barriers.
  - Affinity maturation of computationally designed binders by directed evolution is still required for many targets; the role of starting sequence quality is not established.
last_reviewed: "2026-05-05"
""",

'u-battery-solid-electrolyte-stability.yaml': """id: u-battery-solid-electrolyte-stability
title: What determines the long-term electrochemical stability of solid electrolytes at electrode interfaces, and can this stability be predicted computationally?
status: open
priority: high
disciplines:
  - chemistry
  - electrochemistry
  - materials-science
summary: >
  All-solid-state batteries with oxide or sulfide solid electrolytes promise higher
  energy density and safety than liquid electrolyte batteries. A critical limitation
  is the electrochemical stability window at electrode interfaces: reactions between
  solid electrolytes and electrode active materials degrade performance. Computational
  prediction of interface stability using DFT-based thermodynamics has been developed
  but does not capture kinetic effects that dominate in practice.
systematic_gaps:
  - The equilibrium DFT stability predictions are inconsistent with experimental observations in many electrode-electrolyte pairs due to kinetic passivation.
  - Interface characterisation by cryo-electron microscopy and synchrotron techniques reveals unexpected phases not predicted by computational thermodynamics.
  - The mechanical constraints (stack pressure, volume change on cycling) on interface stability are not incorporated into stability predictions.
last_reviewed: "2026-05-05"
""",
}

print("Creating chemistry gap files...")
for filename, content in chemistry_gap_files.items():
    write(os.path.join(CH, filename), content)
print(f"  Total: {len(chemistry_gap_files)} files\n")

print("=== All unknown files created ===")
print(f"  quantum-physics: {len(quantum_files)}")
print(f"  linguistics: {len(linguistics_files)}")
print(f"  social-science: {len(social_files)}")
print(f"  economics: {len(economics_files)}")
print(f"  computer-science (gap): {len(cs_gap_files)}")
print(f"  neuroscience (gap): {len(neuro_gap_files)}")
print(f"  ecology (gap): {len(ecology_gap_files)}")
print(f"  chemistry (gap): {len(chemistry_gap_files)}")
total_unknowns = (len(quantum_files) + len(linguistics_files) + len(social_files) +
                  len(economics_files) + len(cs_gap_files) + len(neuro_gap_files) +
                  len(ecology_gap_files) + len(chemistry_gap_files))
print(f"  TOTAL NEW UNKNOWNS: {total_unknowns}")
