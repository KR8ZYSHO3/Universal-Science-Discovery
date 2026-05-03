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
  lastUpdated: "2026-05-03 — Dev dashboard scaffolding (`feat/dev-dashboard`); MkDocs strict build gate.",
  currentFocus: [
    "Phase B ingestion package (`packages/ingest`): CLI ergonomics, manifest validation, and docs alignment with [DATA_PLAN.md](../docs/DATA_PLAN.md).",
    "Keeping [mkdocs.yml](../mkdocs.yml) + GitHub Pages (`site_url` / `edit_uri`) consistent with the default branch and fork workflow.",
    "Phase A plan artifacts under `.planning/` and cross-links to methodology docs (no new scientific claims in meta files)."
  ],
  activeBranches: [
    "`main` — default; policy and docs source of truth.",
    "`feat/phase-b-ingest` — [compare to `main`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/phase-b-ingest) — ingest CLI and tests.",
    "`feat/mkdocs-gh-pages` — [compare to `main`](https://github.com/KR8ZYSHO3/Universal-Science-Discovery/compare/main...feat/mkdocs-gh-pages) — site publishing and nav (when active).",
    "Open PRs: use GitHub **Pull requests** tab; add compare links here when reviewing."
  ],
  shippedRecently: [
    "Agent execution rule (`.cursor/rules/agent-execution.mdc`) — run installs, tests, and git in-environment.",
    "MkDocs Material site with doc map, methodology, and ethics pages.",
    "Repository manifest and Phase A data plan documentation."
  ],
  blocked: [
    "None — replace this bullet when something requires credentials, legal review, or maintainer decision outside the repo."
  ],
  nextActions: [
    "Land Phase B ingest MVP with tests and `mkdocs build --strict` clean.",
    "Confirm GitHub Pages branch/env matches `site_url` in `mkdocs.yml`.",
    "Add or refresh UAT notes for ingest when the CLI surface stabilizes.",
    "Keep [LEGAL.md](../LEGAL.md) and science-integrity docs in mind before any new data paths or claims.",
    "After merging this dashboard PR, run the sync script once so canvas constants match this file."
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
