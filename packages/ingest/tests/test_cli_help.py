"""CLI sanity check (offline)."""

import os

from typer.testing import CliRunner

from usdr_ingest.cli import app


def _cli_env() -> dict[str, str]:
    """Rich-backed Typer help omits option tables when TERM=linux (common in CI)."""
    env = os.environ.copy()
    env["TERM"] = "dumb"
    return env


def test_help_exits_zero() -> None:
    runner = CliRunner()
    r = runner.invoke(app, ["harvest", "--help"], env=_cli_env())
    assert r.exit_code == 0
    assert "--from" in r.output
    assert "--max-records" in r.output


def test_top_level_lists_subcommands() -> None:
    runner = CliRunner()
    r = runner.invoke(app, ["--help"], env=_cli_env())
    assert r.exit_code == 0
    assert "harvest" in r.output.lower()
