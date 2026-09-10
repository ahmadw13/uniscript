"""
Fallback behavior for characters with no Unicode equivalent.
"""

from enum import Enum


class FallbackMode(Enum):
    """Controls what happens when a character has no subscript/superscript Unicode equivalent.

    PASSTHROUGH  — pass the original character through unchanged (default, safest)
    OMIT         — silently drop the character
    RAISE        — raise SubstitutionError immediately
    """

    PASSTHROUGH = "passthrough"
    OMIT = "omit"
    RAISE = "raise"
