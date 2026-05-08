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
  lastUpdated: "2026-05-07 — **Waves 72–73 — 24 new bridges (940 bridges catalog / 3,306 graph nodes)**:",
  currentFocus: [
    "**arXiv preprint**: `docs/preprint/usdr_preprint.md` is ready; next step is PDF conversion and submission to cs.DL (author: Brandon Shoemaker).",
    "**Bridge count toward 1,000**: promote `drafts/bridges/` stubs; continue wave-based build.",
    "**Dashboard graph reliability**: D3 interactive graph must load consistently on GitHub Pages.",
    "**Contributor on-ramps**: good-first-issues, `docs/QUICK_START_CONTRIBUTING.md`.",
    "**Community outreach**: Reddit r/OpenScience post ready at `docs/outreach/reddit_openscience_post.md`."
  ],
  activeBranches: [
    "`main` — default; all PRs squash-merged here; CI: validate-schemas + mkdocs + markdown-link-check.",
    "Any active feature branch: `feat/...` — check GitHub Pull Requests tab."
  ],
  shippedRecently: [
    
  ],
  blocked: [
    "None."
  ],
  nextActions: [
    
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
