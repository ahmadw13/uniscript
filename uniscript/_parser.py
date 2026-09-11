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
V_O2_max    → VO₂ₘₐₓ        (chained subscripts)
"""

from uniscript._core import sub, sup
from uniscript._fallback import FallbackMode


def _collect_token(text: str, start: int) -> str:
    """Collect a script token starting at *start*.

    - If the next char is ``(``, collect everything up to the matching ``)``.
    - Otherwise collect a contiguous run of non-space, non-``_``, non-``^`` chars.

    Returns the token string (without surrounding parens if grouped).
    """
    if start >= len(text):
        return ""

    if text[start] == "(":
        # Find matching closing paren
        depth = 0
        i = start
        while i < len(text):
            if text[i] == "(":
                depth += 1
            elif text[i] == ")":
                depth -= 1
                if depth == 0:
                    # Return content between parens
                    return text[start + 1 : i]
            i += 1
        # Unclosed paren — treat remainder as token
        return text[start + 1 :]

    # Collect until whitespace, _, or ^
    i = start
    while i < len(text) and text[i] not in (" ", "\t", "\n", "_", "^"):
        i += 1
    return text[start:i]


def _token_end(text: str, start: int) -> int:
    """Return the index just past the token that starts at *start*."""
    if start >= len(text):
        return start

    if text[start] == "(":
        depth = 0
        i = start
        while i < len(text):
            if text[i] == "(":
                depth += 1
            elif text[i] == ")":
                depth -= 1
                if depth == 0:
                    return i + 1  # past the closing paren
            i += 1
        return len(text)

    i = start
    while i < len(text) and text[i] not in (" ", "\t", "\n", "_", "^"):
        i += 1
    return i


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
    out: list[str] = []
    i = 0
    n = len(text)

    while i < n:
        ch = text[i]

        if ch == "_":
            # subscript: collect token after _
            token = _collect_token(text, i + 1)
            if token:
                out.append(sub(token, fallback=fallback))
                i = _token_end(text, i + 1)
            else:
                # bare _ with nothing after it — pass through
                out.append(ch)
                i += 1

        elif ch == "^":
            # superscript: collect token after ^
            token = _collect_token(text, i + 1)
            if token:
                out.append(sup(token, fallback=fallback))
                i = _token_end(text, i + 1)
            else:
                out.append(ch)
                i += 1

        else:
            out.append(ch)
            i += 1

    return "".join(out)

