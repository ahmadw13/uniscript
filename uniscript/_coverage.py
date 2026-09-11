"""
Coverage reporting for uniscript.

Answers the question: "which characters can actually be converted?"
"""

import string
from dataclasses import dataclass, field

from uniscript._tables import SUB_MAP, SUP_MAP


@dataclass
class CoverageReport:
    """Result of a coverage check for a given character set.

    Attributes
    ----------
    mode:
        Either ``"subscript"`` or ``"superscript"``.
    supported:
        Characters that have a Unicode equivalent.
    unsupported:
        Characters that do not have a Unicode equivalent.
    """

    mode: str
    supported: dict[str, str] = field(default_factory=dict)
    unsupported: list[str] = field(default_factory=list)

    @property
    def total(self) -> int:
        return len(self.supported) + len(self.unsupported)

    @property
    def percent(self) -> float:
        if self.total == 0:
            return 0.0
        return len(self.supported) / self.total * 100

    def __str__(self) -> str:
        lines = [
            f"uniscript coverage — {self.mode}",
            f"  Supported  : {len(self.supported)}/{self.total} ({self.percent:.0f}%)",
            f"  Unsupported: {len(self.unsupported)}/{self.total}",
            "",
            "  Supported characters:",
        ]
        for ch, uni in sorted(self.supported.items()):
            label = repr(ch) if ch.isspace() else ch
            lines.append(f"    {label!s:<4} -> {uni}  (U+{ord(uni):04X})")

        if self.unsupported:
            lines.append("")
            lines.append("  Unsupported characters (fallback applies):")
            lines.append(f"    {''.join(sorted(self.unsupported))}")

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Standard character sets you can pass to coverage()
# ---------------------------------------------------------------------------

DIGITS = string.digits                          # 0-9
LOWERCASE = string.ascii_lowercase             # a-z
UPPERCASE = string.ascii_uppercase             # A-Z
LETTERS = string.ascii_letters                  # a-z A-Z
ALPHANUMERIC = string.digits + string.ascii_letters
SYMBOLS = "+-=()."
COMMON = DIGITS + LOWERCASE + SYMBOLS           # most useful set


def coverage(
    chars: str = COMMON,
    mode: str = "both",
) -> "CoverageReport | tuple[CoverageReport, CoverageReport]":
    """Return a :class:`CoverageReport` showing which characters are supported.

    Parameters
    ----------
    chars:
        The characters to check. Defaults to :data:`COMMON` (digits + lowercase + symbols).
        Use ``uniscript.coverage.ALPHANUMERIC`` etc. for preset sets.
    mode:
        One of ``"subscript"``, ``"superscript"``, or ``"both"`` (default).
        When ``"both"``, returns a tuple of ``(sub_report, sup_report)``.

    Returns
    -------
    CoverageReport | tuple[CoverageReport, CoverageReport]
        A single report, or a tuple of (subscript, superscript) reports.

    Examples
    --------
    >>> from uniscript import coverage
    >>> sub_report, sup_report = coverage("abcdefghij")
    >>> print(sub_report)
    >>> print(sup_report)
    """
    if mode not in ("subscript", "superscript", "both"):
        raise ValueError(f"mode must be 'subscript', 'superscript', or 'both', got {mode!r}")

    def _build(table: dict[str, str], mode_name: str) -> CoverageReport:
        supported: dict[str, str] = {}
        unsupported: list[str] = []
        for ch in chars:
            if ch in table:
                supported[ch] = table[ch]
            else:
                unsupported.append(ch)
        return CoverageReport(mode=mode_name, supported=supported, unsupported=unsupported)

    if mode == "subscript":
        return _build(SUB_MAP, "subscript")
    elif mode == "superscript":
        return _build(SUP_MAP, "superscript")
    else:
        return _build(SUB_MAP, "subscript"), _build(SUP_MAP, "superscript")


def check(text: str) -> dict[str, dict[str, str | None]]:
    """Check every character in *text* for sub/sup support.

    Returns a dict mapping each unique char to its sub and sup equivalents
    (or ``None`` if unsupported).

    Useful for quickly auditing a specific string like ``"t_insp"``.

    Parameters
    ----------
    text:
        The string to audit.

    Returns
    -------
    dict
        ``{ char: { "sub": str | None, "sup": str | None } }``

    Examples
    --------
    >>> from uniscript._coverage import check
    >>> check("insp")
    {'i': {'sub': 'ᵢ', 'sup': 'ⁱ'}, 'n': {'sub': 'ₙ', 'sup': 'ⁿ'}, ...}
    """
    result: dict[str, dict[str, str | None]] = {}
    for ch in dict.fromkeys(text):  # unique chars, preserve order
        result[ch] = {
            "sub": SUB_MAP.get(ch),
            "sup": SUP_MAP.get(ch),
        }
    return result
