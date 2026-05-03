# Developer dashboard (USDR meta)

Human- and agent-editable checklist for **repository operations** — not scientific output. Canonical text lives in [.planning/STATE.md](../../.planning/STATE.md) at the repo root.

## Editing workflow

1. **Update state** — Open `.planning/STATE.md` and adjust the stable sections (`Last updated`, `Current focus`, branches/PR bullets with compare URLs, shipped items, blockers, next actions).

2. **Refresh the Cursor Canvas** — Constants in [`canvases/Progress.canvas.tsx`](../../canvases/Progress.canvas.tsx) are a snapshot mirror of STATE (Canvas cannot read disk). After editing STATE, regenerate that block:

   ```bash
   python scripts/sync-dashboard-from-state.py
   ```

3. **Open the Canvas in Cursor** — Open `canvases/Progress.canvas.tsx` in the editor and use Cursor’s Canvas affordance (“Open Canvas” / canvas panel beside the chat) so the dashboard renders live. If the Canvas entry point is unavailable, editing STATE plus the snippet in the canvas source still keeps the checklist useful.

## Complementary tooling

The GSD **`/gsd-progress`** command (via your Cursor GSD workspace setup) complements this file set: `/gsd-progress` answers situational workflow status; `.planning/STATE.md` is the narrative checklist you trim next to MkDocs policy docs.

Integrity and licensing expectations for substantive work remain in [LEGAL.md](../LEGAL.md), the [documentation map](DOC_MAP.md), and Cursor rules — this dashboard stays **meta** (branches, docs, ingestion milestones).
