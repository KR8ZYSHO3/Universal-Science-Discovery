# Security policy

## Supported versions

This repository is primarily **documentation and research scaffolding**. “Versions” correspond to **git tags** or `main` at a given commit. Critical fixes apply to `main` going forward.

## Reporting a vulnerability

**Do not** open a public issue for undisclosed security vulnerabilities in automation, secrets handling, or maintainer tooling.

Instead:

1. Contact the repository maintainers through a **private channel** they advertise (for example organization security contact or email). If none is listed, use GitHub **private vulnerability reporting** for this repository if enabled.
2. Include reproduction steps, impact, and any suggested mitigation.

## Secrets and sensitive data

If you find committed secrets or **identifiable human data** in history, report privately. Rotating credentials and using `git filter-repo` or GitHub support for history cleanup may be required—follow maintainer guidance.

## Scope

In scope: GitHub Actions workflows, repository automation, dependency supply-chain issues affecting this repo, accidental publication of secrets. Out of scope: scientific debate, non-security content disagreements—use normal issues and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
