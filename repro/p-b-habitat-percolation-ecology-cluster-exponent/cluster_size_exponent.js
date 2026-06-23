/**
 * In-browser Crosscheck demo: cluster size distribution exponent below p_c.
 * Algorithm mirrors cluster_size_exponent.py (lighter lattice for responsiveness).
 */
(function () {
  "use strict";

  const P = 0.592;
  const L = 128;
  const SEEDS = 20;
  const FIT_LO = 8;
  const FIT_HI = Math.floor(L / 4);
  const TAU_THEORY = 187 / 91;
  const TAU_TOLERANCE = 0.1;

  function mulberry32(seed) {
    return function () {
      seed |= 0;
      seed = (seed + 0x6d2b79f5) | 0;
      let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function yieldToBrowser() {
    return new Promise((resolve) => setTimeout(resolve, 0));
  }

  class UnionFind {
    constructor(n) {
      this.parent = Array.from({ length: n }, (_, i) => i);
      this.size = Array(n).fill(1);
    }

    find(x) {
      while (this.parent[x] !== x) {
        this.parent[x] = this.parent[this.parent[x]];
        x = this.parent[x];
      }
      return x;
    }

    union(a, b) {
      let ra = this.find(a);
      let rb = this.find(b);
      if (ra === rb) return;
      if (this.size[ra] < this.size[rb]) [ra, rb] = [rb, ra];
      this.parent[rb] = ra;
      this.size[ra] += this.size[rb];
    }
  }

  function clusterSizes(grid) {
    const n = grid.length;
    const uf = new UnionFind(n * n);
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < n; c++) {
        if (!grid[r][c]) continue;
        const idx = r * n + c;
        if (r + 1 < n && grid[r + 1][c]) uf.union(idx, (r + 1) * n + c);
        if (c + 1 < n && grid[r][c + 1]) uf.union(idx, r * n + c + 1);
      }
    }
    const roots = new Map();
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < n; c++) {
        if (!grid[r][c]) continue;
        const root = uf.find(r * n + c);
        roots.set(root, (roots.get(root) || 0) + 1);
      }
    }
    return [...roots.values()].filter((s) => s >= 2);
  }

  function fitTau(sizes) {
    const hist = new Map();
    for (const s of sizes) hist.set(s, (hist.get(s) || 0) + 1);
    const xs = [];
    const ys = [];
    for (const [s, count] of [...hist.entries()].sort((a, b) => a[0] - b[0])) {
      if (s >= FIT_LO && s <= FIT_HI) {
        xs.push(Math.log(s));
        ys.push(Math.log(count));
      }
    }
    if (xs.length < 3) return { tau: NaN, r2: 0 };
    const n = xs.length;
    const xMean = xs.reduce((a, b) => a + b, 0) / n;
    const yMean = ys.reduce((a, b) => a + b, 0) / n;
    let num = 0;
    let den = 0;
    for (let i = 0; i < n; i++) {
      num += (xs[i] - xMean) * (ys[i] - yMean);
      den += (xs[i] - xMean) ** 2;
    }
    const slope = den ? num / den : 0;
    const tau = -slope;
    let ssRes = 0;
    let ssTot = 0;
    for (let i = 0; i < n; i++) {
      const pred = yMean + slope * (xs[i] - xMean);
      ssRes += (ys[i] - pred) ** 2;
      ssTot += (ys[i] - yMean) ** 2;
    }
    const r2 = ssTot ? 1 - ssRes / ssTot : 0;
    return { tau, r2 };
  }

  async function runClusterExponent(emit) {
    emit({
      type: "line",
      text: "Crosscheck: p-b-habitat-percolation-ecology-cluster-exponent (in-browser demo)",
    });
    emit({
      type: "line",
      text: `Theory: tau = 187/91 = ${TAU_THEORY.toFixed(4)} below p_c at p = ${P}`,
    });
    emit({
      type: "line",
      text: `Lattice ${L}x${L}, ${SEEDS} seeds, pooled histogram, scaling s in [${FIT_LO}, ${FIT_HI}]`,
    });
    emit({ type: "line", text: "" });

    const pooledSizes = [];
    for (let seed = 0; seed < SEEDS; seed++) {
      emit({ type: "progress", pct: 5 + (85 * seed) / SEEDS });
      const rng = mulberry32(seed);
      const grid = Array.from({ length: L }, () =>
        Array.from({ length: L }, () => rng() < P)
      );
      const sizes = clusterSizes(grid);
      pooledSizes.push(...sizes);
      const { tau, r2 } = fitTau(sizes);
      if (Number.isFinite(tau)) {
        emit({
          type: "line",
          text: `  seed=${String(seed).padStart(2)}  tau_hat=${tau.toFixed(4)}  R²=${r2.toFixed(3)}  clusters=${sizes.length}`,
        });
      }
      if (seed % 2 === 1) await yieldToBrowser();
    }

    if (pooledSizes.length < 3) {
      emit({ type: "line", text: "ERROR: insufficient clusters for fit" });
      emit({ type: "result", result: "ERROR" });
      return { passed: false };
    }

    const { tau: pooledTau, r2: pooledR2 } = fitTau(pooledSizes);
    const relErr = Math.abs(pooledTau - TAU_THEORY) / TAU_THEORY;
    const passed = relErr <= TAU_TOLERANCE;
    const result = passed
      ? "CONFIRMED"
      : "INCONCLUSIVE (adjust P or L for clearer scaling)";

    emit({ type: "line", text: "" });
    emit({
      type: "line",
      text: `Pooled tau = ${pooledTau.toFixed(4)}  (R² = ${pooledR2.toFixed(3)})  over ${pooledSizes.length} finite clusters`,
    });
    emit({
      type: "line",
      text: `Relative error vs 187/91 = ${(100 * relErr).toFixed(1)}%  (tolerance ${(100 * TAU_TOLERANCE).toFixed(0)}%)`,
    });
    emit({ type: "line", text: `RESULT: ${result}` });
    emit({ type: "progress", pct: 100 });
    emit({ type: "result", result: passed ? "CONFIRMED" : "INCONCLUSIVE" });
    return { passed, meanTau: pooledTau };
  }

  window.CrosscheckRuns = window.CrosscheckRuns || {};
  window.CrosscheckRuns["p-b-habitat-percolation-ecology-cluster-exponent"] =
    runClusterExponent;
})();