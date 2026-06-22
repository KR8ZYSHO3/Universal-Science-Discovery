/**
 * Shared in-browser Crosscheck runner UI for GitHub Pages repro landing pages.
 * Expects window.CrosscheckRuns[protocolId] = async (emit) => result
 * where emit({ type, text?, pct?, result? }) streams progress/output.
 */
(function () {
  "use strict";

  function init() {
    const root = document.getElementById("crosscheck-runner");
    if (!root) return;

    const protocolId = root.dataset.protocol;
    const runFn = window.CrosscheckRuns && window.CrosscheckRuns[protocolId];
    if (!runFn) return;

    const btn = root.querySelector("[data-action=run]");
    const output = root.querySelector("[data-role=output]");
    const progress = root.querySelector("[data-role=progress]");
    const progressBar = root.querySelector("[data-role=progress-bar]");
    const badge = root.querySelector("[data-role=result-badge]");
    let running = false;

    function setProgress(pct) {
      if (!progress || !progressBar) return;
      const clamped = Math.max(0, Math.min(100, pct));
      progress.hidden = clamped <= 0 || clamped >= 100;
      progressBar.style.width = clamped + "%";
    }

    function setBadge(result) {
      if (!badge) return;
      badge.hidden = !result;
      if (!result) return;
      badge.textContent = result;
      badge.className = "result-badge " + result.toLowerCase();
    }

    btn.addEventListener("click", async () => {
      if (running) return;
      running = true;
      btn.disabled = true;
      output.textContent = "";
      setBadge(null);
      setProgress(1);

      const lines = [];
      const emit = (evt) => {
        if (evt.type === "line" && evt.text) {
          lines.push(evt.text);
          output.textContent = lines.join("\n");
          output.scrollTop = output.scrollHeight;
        }
        if (evt.type === "progress" && typeof evt.pct === "number") {
          setProgress(evt.pct);
        }
        if (evt.type === "result" && evt.result) {
          setBadge(evt.result);
        }
      };

      try {
        await runFn(emit);
      } catch (err) {
        lines.push("ERROR: " + (err && err.message ? err.message : String(err)));
        output.textContent = lines.join("\n");
        setBadge("ERROR");
      } finally {
        setProgress(100);
        running = false;
        btn.disabled = false;
        setTimeout(() => setProgress(0), 600);
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();