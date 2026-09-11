"""
Core translation engine: sub(), sup(), translate().
"""

from uniscript._tables import SUB_MAP, SUP_MAP
from uniscript._fallback import FallbackMode
from uniscript._errors import SubstitutionError


def translate(text: str, table: dict[str, str], fallback: FallbackMode, mode: str = "subscript") -> str:
    """Translate *text* character-by-character using *table*.

    Parameters
    ----------
    text:
        The input string to translate.
    table:
        Lookup dict mapping plain chars to their Unicode equivalents.
    fallback:
        What to do when a character has no entry in *table*.
    mode:
        Human-readable name of the conversion mode, used in error messages.

    Returns
    -------
    str
        Translated string.

    Raises
    ------
    SubstitutionError
        If *fallback* is ``FallbackMode.RAISE`` and a character is missing.
    """
    out: list[str] = []
    for char in text:
        mapped = table.get(char)
        if mapped is not None:
            out.append(mapped)
        else:
            if fallback is FallbackMode.RAISE:
                raise SubstitutionError(char, mode)
            elif fallback is FallbackMode.OMIT:
                pass  # drop the character entirely
            else:  # PASSTHROUGH (default)
                out.append(char)
    return "".join(out)


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
    return translate(text, SUB_MAP, fallback, mode="subscript")


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
    return translate(text, SUP_MAP, fallback, mode="superscript")
