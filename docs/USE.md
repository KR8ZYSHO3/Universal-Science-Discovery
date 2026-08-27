# How to use USDR

**One flow. Three doors.** If another “start here” page disagrees with this file, this file wins for *how to use the repo*. Product path (what we build next) is still [ROADMAP.md](../ROADMAP.md).

Pick **one** door. Do not read the rest of the documentation first.

![Catalog in git, hub as a view, Crosscheck as a runnable experiment](figures/what-usdr-is.svg)

![Three doors: Look, Add, Run](figures/use-three-doors.svg)

| Door | You are… | Do this | Then stop |
|------|----------|---------|-----------|
| **1. Look** | A researcher in the room (no git) | Open the [hub](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/). Search your field. Click a graph node. Run **one** [Crosscheck](CROSSCHECK.md) in the browser. | You have seen the catalog, a bridge, and a live experiment. |
| **2. Add** | Willing to edit one YAML file | Search first (same hub). Copy one seed file. Edit **one** unknown *or* hypothesis *or* bridge. `python scripts/validate_schemas.py`. Open a PR. | Detail: [HAPPY_PATH_FIRST_RECORDS.md](HAPPY_PATH_FIRST_RECORDS.md) |
| **3. Run** | Operating a clone (student / maintainer) | Clone. One ordered command list (v1.3 **ROBUST-01**). Hub numbers must match git. | Detail: [DEV_DASHBOARD.md](DEV_DASHBOARD.md) until the single playbook lands |

## Look

No clone. Open the [hub `#start`](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/#start) and click **Look**, or go straight to [catalog search](https://kr8zysho3.github.io/Universal-Science-Discovery/dashboard/#catalog-search).

## Add

One YAML file. On the hub, click **Add** (opens the five steps) or follow [HAPPY_PATH_FIRST_RECORDS.md](HAPPY_PATH_FIRST_RECORDS.md).

## Run

Clone, then the ordered maintainer list. Until **ROBUST-01** ships, use [DEV_DASHBOARD.md](DEV_DASHBOARD.md) § catalog-batch command order.

## What not to do

- Do not start at launch sprint, outreach, or arXiv docs (parked).
- Do not read ONBOARDING, PATH_TO_SUCCESS, and INTERFACE before using a door.
- Do not add a catalog wave, a Crosscheck protocol, *and* a hub redesign in one sitting.
- Do not treat hub recommendations or xref lists as scientific rankings.

## Where the long docs sit

| Need | File |
|------|------|
| What we build next | [ROADMAP.md](../ROADMAP.md) |
| First YAML records (Door 2 detail) | [HAPPY_PATH_FIRST_RECORDS.md](HAPPY_PATH_FIRST_RECORDS.md) |
| Crosscheck generate / promote / run | [CROSSCHECK.md](CROSSCHECK.md) |
| Policy (claims vs speculation) | [METHODOLOGY.md](METHODOLOGY.md), [VISION_AND_SCOPE.md](VISION_AND_SCOPE.md) |
| Maintainer catalog batch | [DEV_DASHBOARD.md](DEV_DASHBOARD.md), [PATH_TO_SUCCESS.md](PATH_TO_SUCCESS.md) |
| Full contribution types | [CONTRIBUTING.md](../CONTRIBUTING.md) |
| Maintainer policy tour | [ONBOARDING.md](ONBOARDING.md) |
| These pictures | [figures/what-usdr-is.svg](figures/what-usdr-is.svg), [figures/use-three-doors.svg](figures/use-three-doors.svg) |

v1.3 makes Door 1 honest (UI-01, WORK-01) and Door 3 a single list (ROBUST-01, WORK-02). This page is the flow those phases must keep simple.
