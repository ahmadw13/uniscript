"""
Core translation engine: sub(), sup(), translate().
"""

from __future__ import annotations

from uniscript._tables import SUB_MAP, SUP_MAP
from uniscript._fallback import FallbackMode
from uniscript._errors import SubstitutionError


def translate(text: str, table: dict[str, str], fallback: FallbackMode) -> str:
    """Translate *text* character-by-character using *table*.

    Parameters
    ----------
    text:
        The input string to translate.
    table:
        Lookup dict mapping plain chars to their Unicode equivalents.
    fallback:
        What to do when a character has no entry in *table*.

    Returns
    -------
    str
        Translated string.

    Raises
    ------
    SubstitutionError
        If *fallback* is ``FallbackMode.RAISE`` and a character is missing.
    """
    # TODO: implement
    raise NotImplementedError


def sub(text: str, fallback: FallbackMode = FallbackMode.PASSTHROUGH) -> str:
    """Convert *text* to Unicode subscript characters.

    Parameters
    ----------
    text:
        The string to convert. e.g. ``"insp"`` → ``"ᵢₙₛₚ"``
    fallback:
        Behaviour for characters with no subscript equivalent.
        Defaults to :attr:`FallbackMode.PASSTHROUGH`.

    Returns
    -------
    str
        Subscript-converted string.

    Examples
    --------
    >>> from uniscript import sub
    >>> sub("insp")
    'ᵢₙₛₚ'
    >>> sub("0123")
    '₀₁₂₃'
    """
    # TODO: implement
    raise NotImplementedError


def sup(text: str, fallback: FallbackMode = FallbackMode.PASSTHROUGH) -> str:
    """Convert *text* to Unicode superscript characters.

    Parameters
    ----------
    text:
        The string to convert. e.g. ``"2"`` → ``"²"``
    fallback:
        Behaviour for characters with no superscript equivalent.
        Defaults to :attr:`FallbackMode.PASSTHROUGH`.

    Returns
    -------
    str
        Superscript-converted string.

    Examples
    --------
    >>> from uniscript import sup
    >>> sup("2")
    '²'
    >>> sup("n+1")
    'ⁿ⁺¹'
    """
    # TODO: implement
    raise NotImplementedError
