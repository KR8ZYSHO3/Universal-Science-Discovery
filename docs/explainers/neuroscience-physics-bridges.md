# Neuroscience ↔ Physics: Three Surprising Bridges

Physics and neuroscience grew up in different buildings. One studies magnets, circuits, and phase transitions; the other studies spikes, synapses, and memory. The Universal Science Discovery Repository (USDR) catalogs places where the two fields are not merely analogous but the same problem in different clothes. Three bridges are old enough to be textbooks and strange enough that specialists on one side still miss them. This explainer is for journalists, communicators, and researchers who know one language and need a tour of the other — no equations required.

## 1. Criticality and avalanches

Heat a magnet toward its Curie point and it stops being a tidy compass. Below that temperature, atomic “spins” lock into a shared direction. Above it, they jitter independently. Right at the boundary, disturbances of every size become possible, and statistics follow power laws rather than a typical scale.

Cortical networks look uncomfortably like that boundary. Experimenters watching multi-electrode arrays see *neuronal avalanches*: cascades of spikes that die after a few cells, or sweep a whole dish. Size and duration histograms are heavy-tailed. The branching ratio — how many downstream cells a spike recruits, on average — sits near one. Too far below, activity fizzles. Too far above, it seizes. Near the edge, dynamic range and information transmission are both large.

The same scaling relations that describe earthquakes and magnets near criticality appear in cultured cortex and, more contentiously, in waking brain. Whether living tissue *self-organizes* to that point, or merely lives nearby, is still argued. USDR files the claim as established and the mechanism as open (`b-neural-avalanches-criticality`).

**Why it matters:** If healthy computation is a phase of matter, then anesthesia, seizure, and some psychiatric states may be departures from that phase — changes of collective regime, not just chemical mishaps.

## 2. Hodgkin–Huxley and conductance models

An action potential looks like a biological miracle: a millisecond voltage spike that travels meters without fading. In 1952, Alan Hodgkin and Andrew Huxley showed it is an electrical circuit made of protein.

Treat the membrane as a capacitor. Treat each ion species as a battery behind a voltage-dependent resistor — the channel. Sodium and potassium gates open and close on different timescales. The result is a nonlinear oscillator of the same family as a van der Pol circuit: push it past a threshold and it fires a stereotyped pulse, then resets. Voltage clamp made the resistors measurable. The squid giant axon made the numbers honest.

Every modern conductance-based model is that circuit with more ion species. Reduced cousins — FitzHugh–Nagumo, Morris–Lecar — keep the geometry: excitability is a bifurcation; bursting is a slow variable dragging a fast spike generator across a threshold. The neuron is not a logic gate with a messy implementation. It is a dynamical system first (`b-hodgkin-huxley-conductance`).

**Why it matters:** Drugs, channelopathies, and neuromodulation change circuit parameters. Once the spike is an oscillator, those interventions become knobs on a known dynamical system rather than unexplained pharmacology.

## 3. Spin glasses and Hopfield networks

A spin glass is a magnet whose couplings cannot all be satisfied: some neighbor pairs want to align, others to anti-align. The energy landscape is a wrinkled highland of valleys. The system falls into one valley and stays.

In 1982 John Hopfield noticed that a network of binary neurons with symmetric synapses has *the same energy*. Store a pattern by a Hebbian rule — cells that fire together wire together — and that pattern becomes a valley. A partial cue is a point on the slope; the dynamics roll downhill and reconstruct the whole memory. Content-addressable recall is descent on a spin-glass landscape.

Statistical mechanics then computed a storage ceiling of about 0.14 memories per neuron before valleys smash into a glass of nonsense. Overload the network and retrieval does not degrade gracefully; it collapses. USDR tracks the original bridge (`b-hopfield-spin-glass`), whether hippocampus lives near that limit (`u-hopfield-capacity-cortex`), and a hypothesis that synapse loss in Alzheimer’s is a glass transition (`h-hopfield-alzheimers-glass-transition`).

**Why it matters:** Memory is not a filing cabinet. It is an energy landscape. Capacity, confabulation, and catastrophic forgetting are phases of that landscape, not metaphors for them.

## Where to go next

These three bridges — a phase transition in collective activity, a circuit oscillator in the membrane, and a spin glass in associative memory — are among the most cited neuroscience–physics links in USDR. Each catalog entry points to supporting papers, contested claims, and testable unknowns. Start at the [Universal Science Discovery Repository](https://github.com/KR8ZYSHO3/Universal-Science-Discovery), then open `cross-domain/neuroscience-physics/` and `cross-domain/physics-neuroscience/`. The catalog’s point is not a slogan. It is to show where a journalist can borrow a physicist’s word — criticality, oscillator, energy landscape — and still be talking about the brain.
