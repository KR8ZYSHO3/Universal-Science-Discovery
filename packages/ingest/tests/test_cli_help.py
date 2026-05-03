"""CLI sanity check (offline)."""

from typer.testing import CliRunner

from usdr_ingest.cli import app


def test_help_exits_zero() -> None:
    runner = CliRunner()
    r = runner.invoke(app, ["harvest", "--help"])
    assert r.exit_code == 0
    assert "--from" in r.output
    assert "--max-records" in r.output


def test_top_level_lists_subcommands() -> None:
    runner = CliRunner()
    r = runner.invoke(app, ["--help"])
    assert r.exit_code == 0
    assert "harvest" in r.output.lower()
