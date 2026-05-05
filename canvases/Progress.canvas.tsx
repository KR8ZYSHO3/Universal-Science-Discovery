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
  lastUpdated: "2026-05-05 - **Content push toward 1,000 entries (603 total)**: 4 new domain directories (geoscience/28, philosophy-of-science/20, engineering/25, art-and-cognition/15) + 4 new bridges (b-seismology-percolation #41, b-philosophy-underdetermination-quantum #42, b-music-physics-resonance #43, b-engineering-reliability-extreme-value #44) + 10 new hypotheses. Knowledge graph rebuilt: 603 nodes, 628 edges. Dashboard updated. Validates clean.",
  currentFocus: [
    "**Content seeding**: running arXiv harvests (q-bio, cond-mat:stat-mech, nlin, bio-ph) to seed unknowns, hypotheses, and bridges.",
    "**Bridge discovery**: every harvest is checked against the bridge-discovery prompt in `docs/prompts/bridge_discovery.md`.",
    "**Contributor discoverability**: GitHub Issues to be created from open unknowns (next action).",
    "**Schema discipline**: all YAML validated by `scripts/validate_schemas.py` on every PR."
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
    "Create GitHub Issues from the most compelling open unknowns for contributor discoverability.",
    "Write `u-quantum-biology-decoherence` — the open question raised by b-quantum-biology-navigation.",
    "Run a `q-bio:q-bio:TO` (tissues and organs) harvest to seed the topology-morphogenesis bridge further.",
    "Update the developer dashboard stat counts after each PR that adds catalog entries.",
    "Keep `schemas/unknown.yaml`, `schemas/hypothesis.yaml`, `schemas/bridge.yaml` in sync when adding new optional fields."
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
