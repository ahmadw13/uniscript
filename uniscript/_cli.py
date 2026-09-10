"""
CLI entry point for uniscript.

Usage
-----
    uniscript "t_insp"
    echo "E=mc^2" | uniscript
    uniscript --sub "insp"
    uniscript --sup "2"
"""

from __future__ import annotations

import argparse
import sys


def main() -> None:
    """Entry point registered in pyproject.toml [project.scripts]."""
    parser = argparse.ArgumentParser(
        prog="uniscript",
        description="Convert plain text to Unicode subscript/superscript.",
    )
    parser.add_argument(
        "text",
        nargs="?",
        help="Text to convert. Reads from stdin if omitted.",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--sub", action="store_true", help="Force all text to subscript.")
    mode.add_argument("--sup", action="store_true", help="Force all text to superscript.")

    args = parser.parse_args()

    # TODO: implement
    raise NotImplementedError("CLI not yet implemented")


if __name__ == "__main__":
    main()
