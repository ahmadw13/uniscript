# Changelog

All notable changes to `uniscript` will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- GitHub Actions PyPI Trusted Publishing workflow (`.github/workflows/publish.yml`)
- Badges and updated documentation in `README.md` for Greek shorthands and coverage CLI

---

## [0.1.0] - 2026-09-11

### Added
- Core sub/superscript translation engine: `sub()`, `sup()`, and `translate()`
- Smart notation parser: `render()` with support for `t_insp` -> `tᵢₙₛₚ`, `E=mc^2` -> `E=mc²`, `x^(n+1)` -> `xⁿ⁺¹`, and `CO_2` -> `CO₂`
- Complete Unicode lookup tables in `_tables.py` with code point documentation
- `FallbackMode` enum (`PASSTHROUGH`, `OMIT`, `RAISE`) and custom `SubstitutionError`
- Greek letter support: 48 shorthands in `_greek.py` (e.g. `\beta` -> `β`), 7 Greek superscripts in `SUP_MAP` (β, γ, δ, θ, ι, φ, χ), and auto-resolution in `render()`
- `GREEK_SHORTHANDS` and `resolve_shorthands` exported from public API
- Character coverage auditing: `coverage()` and `check()` APIs with `CoverageReport` dataclass
- CLI application: `uniscript` supporting args, stdin, `--sub`, `--sup`, `--coverage`, `--chars`, and `--fallback`
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) on Node.js 24 across Python 3.11, 3.12, and 3.13
- 100 comprehensive unit tests with 96% code coverage

### Changed
- Set modern Python baseline to `>=3.11` (dropped EOL 3.9 and 3.10)
- Added Python 3.13 classifier
- Updated dev dependencies: `pytest>=9.1.1`, `pytest-cov>=7.1.0`
- Normalized repository URLs to `ahmadw13/uniscript`


