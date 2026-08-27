/**
 * In-browser Crosscheck *smoke test* for 2D site percolation FSS.
 *
 * Same named estimator as simulate_percolation_fss.py (Newman–Ziff, periodic,
 * mean occupation at first either-direction wrapping) but a cheap L set and
 * sample count. This runner must not emit CONFIRMED: it is underpowered for ν.
 */
(function () {
  "use strict";

  const PC_INF = 0.59274621;
  const NU_THEORY = 4 / 3;
  const SIZES = [16, 32, 48, 64];
  const N_SAMPLES = 48;
  const SEED = 42;

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

  function shuffle(arr, rng) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(rng() * (i + 1));
      const tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
    }
  }

  function firstWrapEither(L, rng) {
    const n = L * L;
    const parent = new Int32Array(n);
    const dx = new Int32Array(n);
    const dy = new Int32Array(n);
    const rank = new Int32Array(n);
    const occupied = new Uint8Array(n);
    for (let i = 0; i < n; i++) parent[i] = i;

    function find(x) {
      if (parent[x] !== x) {
        const orig = parent[x];
        const root = find(orig);
        dx[x] += dx[orig];
        dy[x] += dy[orig];
        parent[x] = root;
        return root;
      }
      return x;
    }

    const order = new Int32Array(n);
    for (let i = 0; i < n; i++) order[i] = i;
    shuffle(order, rng);

    let wrapH = false;
    let wrapV = false;
    for (let k = 0; k < n; k++) {
      const s = order[k];
      occupied[s] = 1;
      const r = (s / L) | 0;
      const c = s - r * L;
      const bonds = [
        [(r - 1 + L) % L, c, -1, 0],
        [(r + 1) % L, c, 1, 0],
        [r, (c - 1 + L) % L, 0, -1],
        [r, (c + 1) % L, 0, 1],
      ];
      for (const [nr, nc, by, bx] of bonds) {
        const t = nr * L + nc;
        if (!occupied[t]) continue;
        const rs = find(s);
        const rt = find(t);
        if (rs === rt) {
          const wx = dx[s] + bx - dx[t];
          const wy = dy[s] + by - dy[t];
          if (wx !== 0) wrapH = true;
          if (wy !== 0) wrapV = true;
        } else if (rank[rs] < rank[rt]) {
          parent[rs] = rt;
          dx[rs] = dx[t] - bx - dx[s];
          dy[rs] = dy[t] - by - dy[s];
        } else {
          parent[rt] = rs;
          dx[rt] = dx[s] + bx - dx[t];
          dy[rt] = dy[s] + by - dy[t];
          if (rank[rs] === rank[rt]) rank[rs] += 1;
        }
      }
      if (wrapH || wrapV) return (k + 1) / n;
    }
    return 1.0;
  }

  function meanSe(ps) {
    const m = ps.length;
    const mean = ps.reduce((a, b) => a + b, 0) / m;
    let varSum = 0;
    for (const p of ps) varSum += (p - mean) ** 2;
    const sigma = Math.sqrt(varSum / (m - 1));
    return { mean, se: sigma / Math.sqrt(m), sigma };
  }

  async function runPercolationFss(emit) {
    emit({
      type: "line",
      text: "Crosscheck: p-b-habitat-percolation-ecology-fss (in-browser SMOKE TEST)",
    });
    emit({
      type: "line",
      text: "Lattice: L×L square | 4-neighbor | periodic BC | Newman–Ziff",
    });
    emit({
      type: "line",
      text: "Estimator: mean occupation at first either-direction wrapping",
    });
    emit({
      type: "line",
      text: `Theory: p_c(inf)=${PC_INF}, nu=${NU_THEORY.toFixed(4)}`,
    });
    emit({
      type: "line",
      text: `Smoke params: L in [${SIZES.join(", ")}], samples/L=${N_SAMPLES} — cannot confirm nu`,
    });
    emit({ type: "line", text: "" });

    const rng = mulberry32(SEED);
    const rows = [];
    for (let i = 0; i < SIZES.length; i++) {
      const L = SIZES[i];
      emit({ type: "progress", pct: 5 + (85 * i) / SIZES.length });
      const ps = [];
      for (let t = 0; t < N_SAMPLES; t++) {
        ps.push(firstWrapEither(L, rng));
        if (t % 4 === 3) await yieldToBrowser();
      }
      const { mean, se, sigma } = meanSe(ps);
      const delta = mean - PC_INF;
      const sign = delta >= 0 ? "+" : "";
      emit({
        type: "line",
        text:
          `  L=${String(L).padStart(4)}  p_c_hat=${mean.toFixed(5)} ± ${se.toFixed(5)}  ` +
          `delta=${sign}${delta.toFixed(5)}  sigma=${sigma.toFixed(5)}`,
      });
      rows.push({ L, mean, se, delta });
    }

    emit({ type: "line", text: "" });
    emit({
      type: "line",
      text:
        "This browser run is a smoke test. INCONCLUSIVE here means the demo is " +
        "too small to measure ν — not that percolation is wrong.",
    });
    emit({
      type: "line",
      text:
        "Canonical measurement: python simulate_percolation_fss.py  " +
        "(L=32,64,128,256, 400 Newman–Ziff samples/L, weighted fit).",
    });
    const approaching = rows.every((row, idx) => {
      if (idx === 0) return true;
      return Math.abs(row.delta) <= Math.abs(rows[idx - 1].delta) + 2 * (row.se + rows[idx - 1].se);
    });
    if (approaching) {
      emit({
        type: "line",
        text:
          "Smoke check: |p_c(L) − p_c(∞)| shrinks as L grows (within error bars). " +
          "That is the habitat-area shift this test is about.",
      });
    }
    emit({ type: "line", text: "" });
    emit({
      type: "line",
      text: "RESULT: INCONCLUSIVE (browser smoke test; cannot confirm nu)",
    });
    emit({ type: "progress", pct: 100 });
    emit({ type: "result", result: "INCONCLUSIVE" });
    return { passed: false, smoke: true, rows };
  }

  window.CrosscheckRuns = window.CrosscheckRuns || {};
  window.CrosscheckRuns["p-b-habitat-percolation-ecology-fss"] = runPercolationFss;
})();
