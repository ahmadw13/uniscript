# Changelog

All notable changes to `uniscript` will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) — runs `pytest` across Python 3.11, 3.12, 3.13 on both Ubuntu and Windows on every push and PR
- CI required as a passing status check on `main` and `dev` branch protection rules — all 6 matrix jobs must pass before merge

- `coverage(chars, mode)` — returns a `CoverageReport` showing which characters have Unicode sub/superscript equivalents
- `check(text)` — audits every character in a string and returns sub/sup equivalents (or `None` if unsupported)
- `CoverageReport` dataclass with `supported`, `unsupported`, `percent`, `total`, and human-readable `__str__`
- Preset character set constants: `COMMON`, `DIGITS`, `LOWERCASE`, `UPPERCASE`, `ALPHANUMERIC`
- `--coverage` and `--chars` flags to the CLI
- `coverage`, `check`, `CoverageReport` exported from public API
- 18 new tests in `tests/test_coverage.py`
- `sub()`, `sup()`, `render()`, `translate()` — core implementation
- `SubstitutionError` with full error message including Unicode code point
- `FallbackMode` enum: `PASSTHROUGH`, `OMIT`, `RAISE`
- Full Unicode lookup tables in `_tables.py` with source comments per entry
- CLI with `--sub`, `--sup`, `--fallback`, `--coverage`, `--chars` flags and stdin support

### Changed
- Minimum Python version raised to `>=3.11` (dropped EOL 3.9 and 3.10)
- Added Python 3.13 classifier
- Dev deps bumped: `pytest>=9.1.1`, `pytest-cov>=7.1.0`
- Dropped `from __future__ import annotations` shim (not needed on 3.11+)
- GitHub repository URLs corrected to `ahmadw13/uniscript`
- PR template updated to match kurd-doc-intel structure

