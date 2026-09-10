"""
Custom exceptions for uniscript.
"""


class UniScriptError(Exception):
    """Base exception for all uniscript errors."""


class SubstitutionError(UniScriptError):
    """Raised when a character has no Unicode subscript/superscript equivalent
    and FallbackMode.RAISE is active."""

    def __init__(self, char: str, mode: str) -> None:
        self.char = char
        self.mode = mode
        super().__init__(
            f"No Unicode {mode} equivalent for character {char!r} (U+{ord(char):04X}). "
            f"Use FallbackMode.PASSTHROUGH or FallbackMode.OMIT to suppress this error."
        )
