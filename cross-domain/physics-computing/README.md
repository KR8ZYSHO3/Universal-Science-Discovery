# Cross-domain bridges: physics ↔ computing / neuroscience

## Active bridges

### b-spin-glass-neural-networks — Spin-glass statistical mechanics ↔ associative memory

In 1975, Edwards and Anderson described "spin glasses" — disordered magnets
where spins cannot simultaneously satisfy all their conflicting interactions.
The system freezes into one of an exponentially large number of metastable
states.  Solving these models required the "replica method," a brilliant and
mathematically unusual tool from statistical physics.

In 1982, John Hopfield wrote a paper showing that a network of neurons with
symmetric connections has *exactly the same energy function* as a spin glass:

> **E = −½ · Σᵢⱼ Wᵢⱼ · sᵢ · sⱼ**

The network stores memories as energy minima.  Retrieval is energy minimization.
And — here is the bridge — the *capacity* of the network (how many memories
it can store before failing) can be calculated *exactly* using the replica
method developed for spin glasses:

> **α_c = p/N < 0.138**

This number — 0.138 memories per neuron — is an exact result from physics,
derived from a statistical mechanics calculation, applied to a brain model.

**The Alzheimer's connection:** if Alzheimer's disease reduces effective synaptic
connectivity by ~63%, a network that was operating safely at α ~ 0.05 gets pushed
above α_c = 0.138 into the *spin-glass phase* — a regime where the network
converges to spurious memory states rather than the correct one.  This may
explain why Alzheimer's patients *confabulate* (retrieve wrong-but-plausible
memories) rather than simply drawing blanks.

---

## The deeper connection: loss landscape in deep learning

Modern deep neural networks have billions of parameters and a loss landscape
that is nearly impossible to visualize.  Spin-glass theory predicts that above
a certain parameter density, exponentially many near-degenerate minima exist
at low loss — and gradient descent gets trapped in them.  This is the
**same glass transition** as the Hopfield capacity, just in a higher-dimensional
space.

Choromanska et al. (2015) showed that, under certain assumptions, the loss
surface of a deep network is equivalent to the energy surface of a
Sherrington-Kirkpatrick spin glass.  The replica theory then predicts
when training will converge and when it will get stuck — without tuning
any hyperparameters.

## Open unknowns seeded by this bridge

- `u-hopfield-capacity-cortex` — does the human cortex operate near α_c?
- `u-spin-glass-deep-learning-loss-landscape` — do deep network loss landscapes
  obey the SK replica predictions?
