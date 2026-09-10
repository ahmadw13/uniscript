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
from uniscript._coverage import coverage, COMMON, ALPHANUMERIC, LOWERCASE, UPPERCASE, DIGITS


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
    mode.add_argument(
        "--coverage",
        action="store_true",
        help="Show which characters are supported as sub/superscript and exit.",
    )
    parser.add_argument(
        "--chars",
        default="common",
        choices=["common", "digits", "lower", "upper", "alpha"],
        help="Character set to check with --coverage (default: common).",
    )
    parser.add_argument(
        "--fallback",
        choices=["passthrough", "omit", "raise"],
        default="passthrough",
        help="What to do with characters that have no Unicode equivalent (default: passthrough).",
    )

    args = parser.parse_args()

    # --coverage: print report and exit
    if args.coverage:
        char_sets = {
            "common": COMMON,
            "digits": DIGITS,
            "lower": LOWERCASE,
            "upper": UPPERCASE,
            "alpha": ALPHANUMERIC,
        }
        chars = char_sets[args.chars]
        sub_report, sup_report = coverage(chars, mode="both")
        print(sub_report)
        print()
        print(sup_report)
        return

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

