# Security Policy

## Supported Versions

We take the security of the Universal Science Discovery Repository seriously. The following versions are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly.

**Please do NOT open a public GitHub issue.**

Instead, report vulnerabilities by:

1. Opening a **private vulnerability report** on GitHub (if available for this repo), or
2. Emailing **security@usdr.dev** with the subject line: `[SECURITY] Vulnerability Report`

### What to Include in Your Report

Please provide as much information as possible, including:

- Type of vulnerability (e.g., code injection, data exposure, dependency issue)
- Steps to reproduce the issue
- Potential impact (especially if it affects scientific data integrity or user trust)
- Any suggested fixes or mitigations

### Response Timeline

- **Initial Response**: Within 48 hours (we will acknowledge receipt)
- **Status Update**: Within 7 days (we will provide an initial assessment)
- **Resolution**: We aim to resolve critical vulnerabilities within 30 days

We will keep you informed throughout the process and credit you in the release notes (unless you prefer to remain anonymous).

## Scope

This policy covers:

- The main repository code and tools (`code/`)
- CI/CD workflows (`.github/workflows/`)
- Data validation and ingestion scripts
- Any published packages or Docker images (if applicable)

It does **not** cover:

- Vulnerabilities in third-party dependencies (report those to the upstream project)
- Social engineering or physical security issues
- Issues in external linked resources (papers, datasets, websites)

## Responsible Disclosure

We follow responsible disclosure principles. We ask that you:

- Give us reasonable time to investigate and fix the issue before public disclosure
- Do not exploit the vulnerability for any purpose
- Do not access or modify data that does not belong to you

Thank you for helping keep the Universal Science Discovery Repository and its community safe!