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

from uniscript._core import sub, sup
from uniscript._parser import render
from uniscript._fallback import FallbackMode
from uniscript._errors import SubstitutionError


def main() -> None:
    """Entry point registered in pyproject.toml [project.scripts]."""
    parser = argparse.ArgumentParser(
        prog="uniscript",
        description="Convert plain text to Unicode subscript/superscript.",
        epilog="Use _ for subscript and ^ for superscript: uniscript 't_insp' → tᵢₙₛₚ",
    )
    parser.add_argument(
        "text",
        nargs="?",
        help="Text to convert. Reads from stdin if omitted.",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--sub",
        action="store_true",
        help="Convert entire input to subscript (no _ / ^ parsing).",
    )
    mode.add_argument(
        "--sup",
        action="store_true",
        help="Convert entire input to superscript (no _ / ^ parsing).",
    )
    parser.add_argument(
        "--fallback",
        choices=["passthrough", "omit", "raise"],
        default="passthrough",
        help="What to do with characters that have no Unicode equivalent (default: passthrough).",
    )

    args = parser.parse_args()

    # Read text from argument or stdin
    if args.text is not None:
        text = args.text
    else:
        text = sys.stdin.read().rstrip("\n")

    fallback = FallbackMode(args.fallback)

    try:
        if args.sub:
            result = sub(text, fallback=fallback)
        elif args.sup:
            result = sup(text, fallback=fallback)
        else:
            result = render(text, fallback=fallback)
    except SubstitutionError as exc:
        print(f"uniscript: error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(result)


if __name__ == "__main__":
    main()

