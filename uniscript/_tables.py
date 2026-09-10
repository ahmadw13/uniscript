"""
Unicode lookup tables for subscript and superscript conversion.

Sources
-------
- Superscripts and Subscripts block: U+2070–U+209F
  https://www.unicode.org/charts/PDF/U2070.pdf
- Spacing Modifier Letters block: U+02B0–U+02FF
  https://www.unicode.org/charts/PDF/U02B0.pdf
- Phonetic Extensions block: U+1D00–U+1D7F
  https://www.unicode.org/charts/PDF/U1D00.pdf
- Latin-1 Supplement (¹²³): U+00B2, U+00B3, U+00B9

Keys are plain ASCII characters.
Values are their Unicode subscript/superscript equivalents.
Missing keys = no Unicode equivalent exists.
"""

# ---------------------------------------------------------------------------
# SUBSCRIPT MAP
# ---------------------------------------------------------------------------
# Digits — fully covered by U+2080–U+2089
# Letters — only a subset exists in Unicode:
#   ₐₑᵢₒᵤₓₕₖₗₘₙₚₛₜ  (14 lowercase letters)
# Symbols — +, -, =, (, ) covered by U+208A–U+208E
# ---------------------------------------------------------------------------

SUB_MAP: dict[str, str] = {
    # --- Digits (U+2080–U+2089) ---
    "0": "\u2080",  # ₀
    "1": "\u2081",  # ₁
    "2": "\u2082",  # ₂
    "3": "\u2083",  # ₃
    "4": "\u2084",  # ₄
    "5": "\u2085",  # ₅
    "6": "\u2086",  # ₆
    "7": "\u2087",  # ₇
    "8": "\u2088",  # ₈
    "9": "\u2089",  # ₉
    # --- Symbols ---
    "+": "\u208A",  # ₊  U+208A SUBSCRIPT PLUS SIGN
    "-": "\u208B",  # ₋  U+208B SUBSCRIPT MINUS SIGN
    "=": "\u208C",  # ₌  U+208C SUBSCRIPT EQUALS SIGN
    "(": "\u208D",  # ₍  U+208D SUBSCRIPT LEFT PARENTHESIS
    ")": "\u208E",  # ₎  U+208E SUBSCRIPT RIGHT PARENTHESIS
    # --- Lowercase letters (Superscripts and Subscripts block + extensions) ---
    "a": "\u2090",  # ₐ  U+2090 LATIN SUBSCRIPT SMALL LETTER A
    "e": "\u2091",  # ₑ  U+2091 LATIN SUBSCRIPT SMALL LETTER E
    "o": "\u2092",  # ₒ  U+2092 LATIN SUBSCRIPT SMALL LETTER O
    "x": "\u2093",  # ₓ  U+2093 LATIN SUBSCRIPT SMALL LETTER X
    "h": "\u2095",  # ₕ  U+2095 LATIN SUBSCRIPT SMALL LETTER H
    "k": "\u2096",  # ₖ  U+2096 LATIN SUBSCRIPT SMALL LETTER K
    "l": "\u2097",  # ₗ  U+2097 LATIN SUBSCRIPT SMALL LETTER L
    "m": "\u2098",  # ₘ  U+2098 LATIN SUBSCRIPT SMALL LETTER M
    "n": "\u2099",  # ₙ  U+2099 LATIN SUBSCRIPT SMALL LETTER N
    "p": "\u209A",  # ₚ  U+209A LATIN SUBSCRIPT SMALL LETTER P
    "s": "\u209B",  # ₛ  U+209B LATIN SUBSCRIPT SMALL LETTER S
    "t": "\u209C",  # ₜ  U+209C LATIN SUBSCRIPT SMALL LETTER T
    "i": "\u1D62",  # ᵢ  U+1D62 LATIN SUBSCRIPT SMALL LETTER I (Phonetic Extensions)
    "u": "\u1D64",  # ᵤ  U+1D64 LATIN SUBSCRIPT SMALL LETTER U (Phonetic Extensions)
    "v": "\u1D65",  # ᵥ  U+1D65 LATIN SUBSCRIPT SMALL LETTER V (Phonetic Extensions)
    "r": "\u1D63",  # ᵣ  U+1D63 LATIN SUBSCRIPT SMALL LETTER R (Phonetic Extensions)
    "j": "\u2C7C",  # ⱼ  U+2C7C LATIN SUBSCRIPT SMALL LETTER J (Latin Extended-C)
    # --- Greek letters (limited availability) ---
    "\u03B2": "\u1D66",  # β → ᵦ  U+1D66 GREEK SUBSCRIPT SMALL LETTER BETA
    "\u03B3": "\u1D67",  # γ → ᵧ  U+1D67 GREEK SUBSCRIPT SMALL LETTER GAMMA
    "\u03C1": "\u1D68",  # ρ → ᵨ  U+1D68 GREEK SUBSCRIPT SMALL LETTER RHO
    "\u03C6": "\u1D69",  # φ → ᵩ  U+1D69 GREEK SUBSCRIPT SMALL LETTER PHI
    "\u03C7": "\u1D6A",  # χ → ᵪ  U+1D6A GREEK SUBSCRIPT SMALL LETTER CHI
}

# ---------------------------------------------------------------------------
# SUPERSCRIPT MAP
# ---------------------------------------------------------------------------
# Digits — all 10 exist, but 1/2/3 are in Latin-1 Supplement (U+00B9, U+00B2, U+00B3)
# Letters — ~20 exist across multiple blocks
# ---------------------------------------------------------------------------

SUP_MAP: dict[str, str] = {
    # --- Digits ---
    "0": "\u2070",  # ⁰  U+2070 SUPERSCRIPT ZERO
    "1": "\u00B9",  # ¹  U+00B9 SUPERSCRIPT ONE (Latin-1 Supplement)
    "2": "\u00B2",  # ²  U+00B2 SUPERSCRIPT TWO (Latin-1 Supplement)
    "3": "\u00B3",  # ³  U+00B3 SUPERSCRIPT THREE (Latin-1 Supplement)
    "4": "\u2074",  # ⁴  U+2074 SUPERSCRIPT FOUR
    "5": "\u2075",  # ⁵  U+2075 SUPERSCRIPT FIVE
    "6": "\u2076",  # ⁶  U+2076 SUPERSCRIPT SIX
    "7": "\u2077",  # ⁷  U+2077 SUPERSCRIPT SEVEN
    "8": "\u2078",  # ⁸  U+2078 SUPERSCRIPT EIGHT
    "9": "\u2079",  # ⁹  U+2079 SUPERSCRIPT NINE
    # --- Symbols ---
    "+": "\u207A",  # ⁺  U+207A SUPERSCRIPT PLUS SIGN
    "-": "\u207B",  # ⁻  U+207B SUPERSCRIPT MINUS SIGN
    "=": "\u207C",  # ⁼  U+207C SUPERSCRIPT EQUALS SIGN
    "(": "\u207D",  # ⁽  U+207D SUPERSCRIPT LEFT PARENTHESIS
    ")": "\u207E",  # ⁾  U+207E SUPERSCRIPT RIGHT PARENTHESIS
    "n": "\u207F",  # ⁿ  U+207F SUPERSCRIPT LATIN SMALL LETTER N
    "i": "\u2071",  # ⁱ  U+2071 SUPERSCRIPT LATIN SMALL LETTER I
    # --- Lowercase letters (Spacing Modifier Letters U+02B0–U+02FF) ---
    "b": "\u1D47",  # ᵇ  U+1D47
    "d": "\u1D48",  # ᵈ  U+1D48
    "e": "\u1D49",  # ᵉ  U+1D49
    "f": "\u1DA0",  # ᶠ  U+1DA0 (Phonetic Extensions Supplement)
    "g": "\u1D4D",  # ᵍ  U+1D4D
    "h": "\u02B0",  # ʰ  U+02B0
    "j": "\u02B2",  # ʲ  U+02B2
    "k": "\u1D4F",  # ᵏ  U+1D4F
    "l": "\u02E1",  # ˡ  U+02E1
    "m": "\u1D50",  # ᵐ  U+1D50
    "o": "\u1D52",  # ᵒ  U+1D52
    "p": "\u1D56",  # ᵖ  U+1D56
    "r": "\u02B3",  # ʳ  U+02B3
    "s": "\u02E2",  # ˢ  U+02E2
    "t": "\u1D57",  # ᵗ  U+1D57
    "u": "\u1D58",  # ᵘ  U+1D58
    "v": "\u1D5B",  # ᵛ  U+1D5B
    "w": "\u02B7",  # ʷ  U+02B7
    "x": "\u02E3",  # ˣ  U+02E3
    "y": "\u02B8",  # ʸ  U+02B8
    "z": "\u1DBB",  # ᶻ  U+1DBB
    "a": "\u1D43",  # ᵃ  U+1D43
    "c": "\u1D9C",  # ᶜ  U+1D9C (Phonetic Extensions Supplement)
    # --- Uppercase letters (very limited) ---
    "A": "\u1D2C",  # ᴬ  U+1D2C MODIFIER LETTER CAPITAL A
    "B": "\u1D2E",  # ᴮ  U+1D2E MODIFIER LETTER CAPITAL B
    "D": "\u1D30",  # ᴰ  U+1D30 MODIFIER LETTER CAPITAL D
    "E": "\u1D31",  # ᴱ  U+1D31 MODIFIER LETTER CAPITAL E
    "G": "\u1D33",  # ᴳ  U+1D33 MODIFIER LETTER CAPITAL G
    "H": "\u1D34",  # ᴴ  U+1D34 MODIFIER LETTER CAPITAL H
    "I": "\u1D35",  # ᴵ  U+1D35 MODIFIER LETTER CAPITAL I
    "J": "\u1D36",  # ᴶ  U+1D36 MODIFIER LETTER CAPITAL J
    "K": "\u1D37",  # ᴷ  U+1D37 MODIFIER LETTER CAPITAL K
    "L": "\u1D38",  # ᴸ  U+1D38 MODIFIER LETTER CAPITAL L
    "M": "\u1D39",  # ᴹ  U+1D39 MODIFIER LETTER CAPITAL M
    "N": "\u1D3A",  # ᴺ  U+1D3A MODIFIER LETTER CAPITAL N
    "O": "\u1D3C",  # ᴼ  U+1D3C MODIFIER LETTER CAPITAL O
    "P": "\u1D3E",  # ᴾ  U+1D3E MODIFIER LETTER CAPITAL P
    "R": "\u1D3F",  # ᴿ  U+1D3F MODIFIER LETTER CAPITAL R
    "T": "\u1D40",  # ᵀ  U+1D40 MODIFIER LETTER CAPITAL T
    "U": "\u1D41",  # ᵁ  U+1D41 MODIFIER LETTER CAPITAL U
    "V": "\u2C7D",  # ᱽ  U+2C7D MODIFIER LETTER CAPITAL V
    "W": "\u1D42",  # ᵂ  U+1D42 MODIFIER LETTER CAPITAL W
}
