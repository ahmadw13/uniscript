"""
Notation parser: render().

Parses strings with _ (subscript) and ^ (superscript) markers,
similar to TeX notation but for plain Unicode output.

Supported syntax
----------------
t_insp      → tᵢₙₛₚ         (subscript until next space or end)
E=mc^2      → E=mc²          (superscript until next space or end)
x^(n+1)     → xⁿ⁺¹          (parentheses group the script region)
CO_2        → CO₂            (numeric subscript)
V_O2_max    → VO₂ₘₐₓ        (chained subscripts — not yet supported in v0.1)
"""

from __future__ import annotations

from uniscript._fallback import FallbackMode


def render(text: str, fallback: FallbackMode = FallbackMode.PASSTHROUGH) -> str:
    """Parse *text* for ``_`` and ``^`` markers and return Unicode-converted output.

    Parameters
    ----------
    text:
        Input string using ``_word`` for subscript and ``^word`` for superscript.
        Use parentheses to group: ``x^(n+1)``.
    fallback:
        Behaviour for characters with no Unicode equivalent.

    Returns
    -------
    str
        String with subscript/superscript regions converted to Unicode.

    Examples
    --------
    >>> from uniscript import render
    >>> render("t_insp")
    'tᵢₙₛₚ'
    >>> render("E=mc^2")
    'E=mc²'
    >>> render("x^(n+1)")
    'xⁿ⁺¹'
    """
    # TODO: implement
    raise NotImplementedError
