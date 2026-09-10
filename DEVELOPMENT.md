# Development Guide

## Setup

**Prerequisites:** Python 3.9+, `uv` (recommended) or `pip`

```bash
# Clone
git clone https://github.com/ahmadw13/uniscript.git
cd uniscript

# Create venv and install dev deps (with uv)
uv venv
uv pip install -e ".[dev]"

# Or with plain pip
python -m venv .venv
.venv\Scripts\activate     # Windows
pip install -e ".[dev]"
```

---

## Branch Workflow

We follow the same branch model used across our projects:

| Branch | Purpose |
|---|---|
| `main` | Stable, always releasable |
| `dev` | Integration branch — PRs merge here first |
| `feat/<name>` | New feature work |
| `fix/<name>` | Bug fixes |
| `chore/<name>` | Tooling, deps, CI |
| `docs/<name>` | Documentation only |

**Flow:**
```
feat/tables → dev → main (on release)
```

Never push directly to `main`.

---

## Running Tests

```bash
pytest                          # run all tests
pytest --cov=uniscript          # with coverage
pytest tests/test_core.py -v    # single file
```

---

## Project Structure

```
uniscript/
├── uniscript/
│   ├── __init__.py      # Public API: sub, sup, render, FallbackMode
│   ├── _tables.py       # Unicode lookup dicts (SUB_MAP, SUP_MAP)
│   ├── _core.py         # translate(), sub(), sup()
│   ├── _parser.py       # parse "t_insp", "E=mc^2" syntax → render()
│   ├── _fallback.py     # FallbackMode enum + resolution logic
│   └── _cli.py          # CLI entry point
├── tests/
│   ├── test_tables.py   # Coverage & correctness of lookup tables
│   ├── test_core.py     # sub(), sup(), translate()
│   ├── test_parser.py   # render() parsing, edge cases
│   └── test_cli.py      # CLI smoke tests
├── .github/
│   └── pull_request_template.md
├── pyproject.toml
├── README.md
├── DEVELOPMENT.md
└── CHANGELOG.md
```

---

## Adding New Unicode Mappings

When adding characters to `_tables.py`, always include:
- The Unicode code point (e.g., `U+2099`)
- The Unicode block it comes from
- A comment if the source is non-obvious

Example:
```python
# ₙ U+2099 — LATIN SUBSCRIPT SMALL LETTER N (Superscripts and Subscripts block)
'n': '\u2099',
```

---

## Changelog

We follow [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.
Update `CHANGELOG.md` with every PR.
