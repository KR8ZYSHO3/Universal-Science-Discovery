/**
 * In-browser Crosscheck demo: 2D site percolation finite-size scaling (nu ~ 4/3).
 * Algorithm mirrors simulate_percolation_fss.py; uses a demo trial budget for speed.
 */
(function () {
  "use strict";

  const PC_INF = 0.59274621;
  const NU_THEORY = 4 / 3;
  const NU_TOLERANCE = 0.15;
  const SIZES = [16, 32, 64, 128];
  const TRIALS_PER_P = 120;
  const P_GRID = 30;

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

  function neighbors(r, c, n) {
    const out = [];
    if (r > 0) out.push([r - 1, c]);
    if (r + 1 < n) out.push([r + 1, c]);
    if (c > 0) out.push([r, c - 1]);
    if (c + 1 < n) out.push([r, c + 1]);
    return out;
  }

  function spans(grid) {
    const n = grid.length;
    const seen = Array.from({ length: n }, () => Array(n).fill(false));
    const stack = [];
    for (let c = 0; c < n; c++) {
      if (grid[0][c]) {
        stack.push([0, c]);
        seen[0][c] = true;
      }
    }
    while (stack.length) {
      const [r, c] = stack.pop();
      if (r === n - 1) return true;
      for (const [nr, nc] of neighbors(r, c, n)) {
        if (grid[nr][nc] && !seen[nr][nc]) {
          seen[nr][nc] = true;
          stack.push([nr, nc]);
        }
      }
    }
    return false;
  }

  async function crossingProbability(n, p, trials, seed) {
    const rng = mulberry32(seed);
    let hits = 0;
    for (let t = 0; t < trials; t++) {
      const grid = Array.from({ length: n }, () =>
        Array.from({ length: n }, () => rng() < p)
      );
      if (spans(grid)) hits += 1;
      if (t % 8 === 7) await yieldToBrowser();
    }
    return hits / trials;
  }

  async function estimatePc(n, trials, seed) {
    let lo = 0.45;
    let hi = 0.75;
    for (let step = 0; step < P_GRID; step++) {
      const mid = (lo + hi) / 2;
      const prob = await crossingProbability(n, mid, trials, seed + step);
      if (prob >= 0.5) hi = mid;
      else lo = mid;
      if (step % 4 === 3) await yieldToBrowser();
    }
    return (lo + hi) / 2;
  }

  function fitNu(sizes, pcs) {
    const xs = sizes.map((L) => Math.log(L));
    const ys = pcs.map((pc) => Math.log(Math.abs(pc - PC_INF) + 1e-9));
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
    const nu = slope ? -1 / slope : Infinity;
    let ssRes = 0;
    let ssTot = 0;
    for (let i = 0; i < n; i++) {
      const pred = yMean + slope * (xs[i] - xMean);
      ssRes += (ys[i] - pred) ** 2;
      ssTot += (ys[i] - yMean) ** 2;
    }
    const r2 = ssTot ? 1 - ssRes / ssTot : 0;
    return { nu, r2 };
  }

  async function runPercolationFss(emit) {
    emit({ type: "line", text: "Crosscheck: p-b-habitat-percolation-ecology-fss (in-browser demo)" });
    emit({
      type: "line",
      text: `Theory: p_c(inf)=${PC_INF}, nu=${NU_THEORY.toFixed(4)}`,
    });
    emit({
      type: "line",
      text: `Demo params: L in [${SIZES.join(", ")}], trials/L=${TRIALS_PER_P}`,
    });
    emit({ type: "line", text: "" });

    const pcs = [];
    const total = SIZES.length;
    for (let i = 0; i < SIZES.length; i++) {
      const L = SIZES[i];
      emit({ type: "progress", pct: 5 + (85 * i) / total });
      const pc = await estimatePc(L, TRIALS_PER_P, 42 + i * 1000);
      pcs.push(pc);
      emit({
        type: "line",
        text: `  L=${String(L).padStart(4)}  p_c_hat=${pc.toFixed(5)}  delta=${(pc - PC_INF >= 0 ? "+" : "")}${(pc - PC_INF).toFixed(5)}`,
      });
    }

    const { nu, r2 } = fitNu(SIZES, pcs);
    const relErr = Math.abs(nu - NU_THEORY) / NU_THEORY;
    const passed = relErr <= NU_TOLERANCE;
    const result = passed
      ? "CONFIRMED"
      : "INCONCLUSIVE (increase TRIALS_PER_P for higher precision)";

    emit({ type: "line", text: "" });
    emit({ type: "line", text: `Fitted nu = ${nu.toFixed(4)}  (R² = ${r2.toFixed(4)})` });
    emit({
      type: "line",
      text: `Relative error vs 4/3 = ${(100 * relErr).toFixed(1)}%  (tolerance ${(100 * NU_TOLERANCE).toFixed(0)}%)`,
    });
    emit({ type: "line", text: `RESULT: ${result}` });
    emit({ type: "progress", pct: 100 });
    emit({ type: "result", result: passed ? "CONFIRMED" : "INCONCLUSIVE" });
    return { passed, nu, r2 };
  }

  window.CrosscheckRuns = window.CrosscheckRuns || {};
  window.CrosscheckRuns["p-b-habitat-percolation-ecology-fss"] = runPercolationFss;
})();