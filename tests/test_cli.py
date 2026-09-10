"""Smoke tests for the CLI entry point."""

import subprocess
import sys

import pytest


def run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "uniscript._cli", *args],
        capture_output=True,
        text=True,
    )


class TestCLI:
    def test_basic_render(self):
        result = run_cli("t_insp")
        assert result.returncode == 0
        assert "ᵢₙₛₚ" in result.stdout

    def test_sup_flag(self):
        result = run_cli("--sup", "2")
        assert result.returncode == 0
        assert "²" in result.stdout

    def test_sub_flag(self):
        result = run_cli("--sub", "insp")
        assert result.returncode == 0
        assert "ᵢₙₛₚ" in result.stdout

    def test_no_args_reads_stdin(self):
        result = subprocess.run(
            [sys.executable, "-m", "uniscript._cli"],
            input="CO_2",
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "₂" in result.stdout
