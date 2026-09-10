# Changelog

All notable changes to `uniscript` will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- `coverage(chars, mode)` — returns a `CoverageReport` showing which characters have Unicode sub/superscript equivalents, with percentage and full character-by-character breakdown
- `check(text)` — audits every character in a string and returns sub/sup equivalents (or `None` if unsupported)
- `CoverageReport` dataclass — `supported`, `unsupported`, `percent`, `total`, human-readable `__str__`
- Preset character set constants: `COMMON`, `DIGITS`, `LOWERCASE`, `UPPERCASE`, `ALPHANUMERIC`
- `--coverage` and `--chars` flags to the CLI
- `coverage`, `check`, `CoverageReport` exported from the public API in `__init__.py`
- 18 new tests in `tests/test_coverage.py`
- Initial implementation of `sub()`, `sup()`, `render()`, `translate()`, and CLI (from `feat/core-translate`)
- `SubstitutionError` with full error message including Unicode code point
- `FallbackMode` enum: `PASSTHROUGH`, `OMIT`, `RAISE`
- Full Unicode lookup tables in `_tables.py` with source comments per entry (Unicode block + code point)

### Changed
- Minimum Python version raised to `>=3.11` (dropped EOL 3.9 and 3.10)
- Added Python 3.13 classifier
- Dev deps bumped: `pytest>=9.1.1`, `pytest-cov>=7.1.0`
- Dropped `from __future__ import annotations` shim from all modules (not needed on 3.11+)
- GitHub repository URLs corrected to `ahmadw13/uniscript` across `pyproject.toml`, `README.md`, `DEVELOPMENT.md`
- PR template updated to match kurd-doc-intel structure (added Screenshots section, standardised wording)
