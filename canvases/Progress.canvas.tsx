/**
 * Regenerate constants from `.planning/STATE.md` when agent refreshes — run: python scripts/sync-dashboard-from-state.py
 */
import {
  Callout,
  Card,
  CardBody,
  CardHeader,
  Divider,
  Grid,
  H1,
  H2,
  mergeStyle,
  Pill,
  Row,
  Spacer,
  Stack,
  Text,
  useHostTheme,
} from "cursor/canvas";

// @sync-dashboard-begin
const dashboardSnapshot = {
  lastUpdated: "2026-05-03 — Contributor **hub** links **docs/GSD_INTEGRATION.md**; manifest row added. **docs/index** Meta link.",
  currentFocus: [
    "Docs + **dashboard** discipline: milestones and ongoing work update `README`, `CHANGELOG` (Unreleased), `docs/` as needed, `dashboard/index.html`, and spot-check **`http://localhost:8765/dashboard/`** (see `.cursor/rules/documentation-and-dashboard.mdc`).",
    "**usdr-ingest** (`packages/ingest`): arXiv OAI-PMH metadata only — extend CLI/manifest as needed per [DATA_PLAN.md](../docs/DATA_PLAN.md).",
    "Keeping [mkdocs.yml](../mkdocs.yml) + GitHub Pages (`site_url` / `edit_uri`) consistent with the default branch and fork workflow.",
    "Phase A plan artifacts under `.planning/` and cross-links to methodology docs (no new scientific claims in meta files)."
  ],
  activeBranches: [
    "`main` — default; policy and docs source of truth.",
    "`feat/dev-dashboard` — [compare to `main`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/dev-dashboard) — contributor HTML hub, doc rules, **usdr-ingest**, mkdocs/Pages CI.",
    "`feat/mkdocs-gh-pages` — [compare to `main`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/mkdocs-gh-pages) — site publishing and nav (when active).",
    "Open PRs: use GitHub **Pull requests** tab; add compare links here when reviewing."
  ],
  shippedRecently: [
    "Contributor **HTML hub** (`dashboard/index.html`) and README onboarding path.",
    "Cursor **documentation-and-dashboard** rule (milestones + ongoing docs + `http://localhost:8765/dashboard/` verification).",
    "MkDocs Material site with doc map, methodology, and ethics pages.",
    "**JSON Schema** for ingest: `schemas/ingestion-envelope-1.0.0.json` + pytest validation of harvest JSONL rows.",
    "Repository manifest and Phase A data plan documentation."
  ],
  blocked: [
    "None — replace this bullet when something requires credentials, legal review, or maintainer decision outside the repo."
  ],
  nextActions: [
    "Open **one integration PR** from `feat/dev-dashboard` → `main` (hub + docs rules + ingest + mkdocs/Pages) when ready.",
    "Confirm GitHub Pages branch/env matches `site_url` in `mkdocs.yml`.",
    "Add or refresh UAT notes for ingest when the CLI surface stabilizes.",
    "Keep [LEGAL.md](../LEGAL.md) and science-integrity docs in mind before any new data paths or claims.",
    "Apply **documentation-and-dashboard** rule on each merge: update CHANGELOG Unreleased, sync Canvas from `STATE.md` when using `canvases/Progress.canvas.tsx`, re-check contributor hub if links changed."
  ],
} as const;
// @sync-dashboard-end

function BulletLines({ lines }: { lines: readonly string[] }) {
  return (
    <Stack gap={6}>
      {lines.map((line, i) => (
        <Text key={i} tone="secondary" size="small">
          — {line}
        </Text>
      ))}
    </Stack>
  );
}

export default function ProgressDashboard() {
  const theme = useHostTheme();
  const s = dashboardSnapshot;

  return (
    <Stack gap={20}>
      <Stack
        gap={8}
        style={mergeStyle(
          { paddingBottom: 14 },
          { borderBottom: `1px solid ${theme.stroke.secondary}` },
        )}
      >
        <Row gap={12} align="center">
          <H1 style={{ margin: 0 }}>USDR dev dashboard</H1>
          <Spacer />
          <Pill tone="info" size="sm">
            Embedded snapshot
          </Pill>
        </Row>
        <Text tone="tertiary" size="small">
          Mirror of `.planning/STATE.md` — constants are inlined; Canvas does not read the file at runtime.
        </Text>
        <Text tone="secondary" size="small" weight="medium">
          {s.lastUpdated}
        </Text>
      </Stack>

      <Grid columns={"1fr 1fr"} gap={24} align="start" style={{ minWidth: 0 }}>
        <Stack gap={10}>
          <Row gap={10} align="center" wrap={false}>
            <H2 style={{ margin: 0 }}>Current focus</H2>
            <Pill tone="info" size="sm">
              Active work
            </Pill>
          </Row>
          <BulletLines lines={s.currentFocus} />
        </Stack>
        <Stack gap={10}>
          <Row gap={10} align="center" wrap={false}>
            <H2 style={{ margin: 0 }}>Next actions</H2>
            <Pill tone="neutral" size="sm">
              {String(s.nextActions.length)} items
            </Pill>
          </Row>
          <BulletLines lines={s.nextActions} />
        </Stack>
      </Grid>

      <Divider />

      <Card>
        <CardHeader trailing={<Pill tone="neutral">Compare links</Pill>}>
          Branches and PR pointers
        </CardHeader>
        <CardBody>
          <BulletLines lines={s.activeBranches} />
        </CardBody>
      </Card>

      <Grid columns={"1fr 1fr"} gap={24} align="start" style={{ minWidth: 0 }}>
        <Stack gap={10}>
          <Row gap={10} align="center">
            <H2 style={{ margin: 0 }}>Shipped recently</H2>
            <Pill tone="success" size="sm">
              ok
            </Pill>
          </Row>
          <BulletLines lines={s.shippedRecently} />
        </Stack>
        <Stack gap={10}>
          <Row gap={10} align="center">
            <H2 style={{ margin: 0 }}>Blocked / needs human</H2>
            <Pill tone="warning" size="sm">
              watch
            </Pill>
          </Row>
          <BulletLines lines={s.blocked} />
        </Stack>
      </Grid>

      <Callout tone="info" title="Complementary tooling">
        <Text tone="secondary" size="small">
          See docs/DEV_DASHBOARD.md. Use GSD `/gsd-progress` for automated phase tracking alongside this checklist.
        </Text>
      </Callout>
    </Stack>
  );
}
