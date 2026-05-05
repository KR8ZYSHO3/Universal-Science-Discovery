# Cross-domain bridges: mathematics / game theory ↔ evolution ↔ ML

## Active bridges

### b-game-theory-evolution — Nash equilibrium = evolutionary stable strategy

John Nash proved in 1950 that every finite game has at least one equilibrium
where no player can improve by switching strategy unilaterally.  He got the
Nobel Prize in Economics for it in 1994.

John Maynard Smith — a biologist — independently derived the same concept in
1973 and called it the "evolutionary stable strategy" (ESS).  He had never read
Nash.  Natural selection on heritable strategies, with no rationality, no
planning, and no communication between individuals, converges to exactly the
same equilibrium.

The mathematics is identical.  The **replicator equation**:

> **dx_i/dt = x_i · (f_i(x) − f̄(x))**

describes how strategy frequencies change under selection.  Its fixed points
are Nash equilibria.  This is the same equation that governs:

- hawk-dove dynamics in animal conflict
- antibiotic resistance evolution
- GAN training (generator vs discriminator is a zero-sum game)
- RLHF reward model fine-tuning (Nash equilibrium reward models)
- cultural evolution of scientific paradigms

**The Price equation** (George Price, 1970) goes deeper still — it is a
pure algebraic identity that decomposes any change in mean trait value into
selection and transmission components.  It unifies Fisher's fundamental theorem,
Hamilton's inclusive fitness, Maynard Smith's ESS, and — in recent work —
gradient descent in machine learning.

**The 70-year gap:** Nash 1950 → Maynard Smith 1973 → GANs 2014 → RLHF 2022.
Each community rediscovered the same mathematical structure independently,
each time delayed by ~20 years of disciplinary siloing.

---

## Related bridges

- `b-fisher-information-evolution` — Fisher information connects statistics to evolution
- `b-ising-social-dynamics` — social strategy dynamics as spin systems
- `b-spin-glass-neural-networks` — deep learning loss landscapes as Nash-seeking games
