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
  lastUpdated: "2026-05-05 - **Bridges 50-54 — astronomy orphan connections targeting largest cluster (633 nodes)**: 5 new bridges (b-blackhole-information-paradox #50, b-baryon-asymmetry-cp-violation #51, b-dark-matter-phase-transition-relics #52, b-cosmic-rays-mutagenesis #53, b-frb-random-matrix #54) with 5 new unknowns + 5 new hypotheses. Created 4 new cross-domain directories (astronomy-information, astronomy-physics, astronomy-biology, astronomy-mathematics). Connected 5 existing astronomy orphan unknowns (black hole info paradox, baryon asymmetry, dark matter identity, FRB origin, UHECR). Orphan count reduced from 329 → 324. Knowledge graph rebuilt: 633 nodes, 443 edges. Dashboard updated. Validates clean.",
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
