"""Tests for the CLI — calls main() directly so pytest-cov instruments _cli.py."""

import sys
import pytest
from unittest.mock import patch
from io import StringIO

from uniscript._cli import main


def run_cli(args: list[str], stdin: str = "") -> tuple[str, int]:
    """Call main() with patched sys.argv and captured stdout. Returns (output, exit_code)."""
    with patch("sys.argv", ["uniscript"] + args), \
         patch("sys.stdin", StringIO(stdin)), \
         patch("sys.stdout", new_callable=StringIO) as mock_out:
        try:
            main()
            return mock_out.getvalue(), 0
        except SystemExit as e:
            return mock_out.getvalue(), int(str(e))


class TestCLI:
    def test_basic_render(self):
        out, code = run_cli(["t_insp"])
        assert code == 0
        assert "ᵢₙₛₚ" in out

    def test_sup_flag(self):
        out, code = run_cli(["--sup", "2"])
        assert code == 0
        assert "²" in out

    def test_sub_flag(self):
        out, code = run_cli(["--sub", "insp"])
        assert code == 0
        assert "ᵢₙₛₚ" in out

    def test_no_args_reads_stdin(self):
        out, code = run_cli([], stdin="CO_2")
        assert code == 0
        assert "₂" in out

    def test_fallback_omit(self):
        out, code = run_cli(["--sub", "--fallback", "omit", "qqq"])
        assert code == 0
        assert out.strip() == ""

    def test_fallback_raise_exits_nonzero(self):
        with patch("sys.argv", ["uniscript", "--sub", "--fallback", "raise", "Q"]), \
             patch("sys.stderr", new_callable=StringIO):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 1

    def test_plain_text_passthrough(self):
        out, code = run_cli(["hello"])
        assert code == 0
        assert "hello" in out
