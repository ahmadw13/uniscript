# uniscript

> Convert plain strings to Unicode subscript/superscript — no HTML, no LaTeX, no images. Just text.

```python
from uniscript import sub, sup, render

render("t_insp")   # → "tᵢₙₛₚ"
render("E=mc^2")   # → "E=mc²"
render("CO_2")     # → "CO₂"
render("x^(n+1)")  # → "xⁿ⁺¹"
```

Works anywhere plain text works: terminals, Slack, Markdown files, text editors, Python `print()`.

---

## Installation

```bash
pip install uniscript
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv add uniscript
```

---

## Usage

### `render(text)` — Auto-parse notation strings

Uses `_` for subscript and `^` for superscript, matching common scientific/math notation:

```python
from uniscript import render

render("t_insp")     # tᵢₙₛₚ
render("V_O2_max")   # VO₂ₘₐₓ
render("H_2O")       # H₂O
render("x^2 + y^2")  # x² + y²
render("x^(n+1)")    # xⁿ⁺¹
```

### `sub(text)` — Convert a string to subscript

```python
from uniscript import sub

sub("insp")   # ᵢₙₛₚ
sub("0123")   # ₀₁₂₃
sub("(n+1)")  # ₍ₙ₊₁₎
```

### `sup(text)` — Convert a string to superscript

```python
from uniscript import sup

sup("2")      # ²
sup("n+1")    # ⁿ⁺¹
sup("th")     # ᵗʰ
```

### Fallback behavior

Not all characters have Unicode equivalents. You can control what happens:

```python
from uniscript import sub, FallbackMode

sub("xyz", fallback=FallbackMode.PASSTHROUGH)  # unknown chars passed through as-is (default)
sub("xyz", fallback=FallbackMode.RAISE)        # raises UnicodeSubstitutionError
sub("xyz", fallback=FallbackMode.OMIT)         # unknown chars silently dropped
```

### CLI

```bash
echo "t_insp" | uniscript
# tᵢₙₛₚ

uniscript "E=mc^2"
# E=mc²
```

---

## Unicode Coverage

| Character set | Subscript | Superscript |
|---|---|---|
| Digits `0–9` | ✅ Full | ✅ Full |
| Letters `a–z` | ⚠️ Partial (~14) | ⚠️ Partial (~20) |
| Letters `A–Z` | ❌ None | ❌ Almost none |
| `+ − = ( )` | ✅ Full | ✅ Full |
| Greek letters | ⚠️ A few | ⚠️ A few |

The available subscript letters (`ₐₑᵢₒᵤₓₙₘₖₛₜₕₗₚ`) cover most common scientific notations in practice.

---

## Development

See [DEVELOPMENT.md](DEVELOPMENT.md) for setup, branch workflow, and contribution guidelines.

---

## License

MIT
