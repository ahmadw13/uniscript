"""Tests for _coverage.py — coverage(), check(), CoverageReport."""

import pytest
from uniscript import coverage, check, CoverageReport
from uniscript._coverage import DIGITS, LOWERCASE, UPPERCASE, COMMON, ALPHANUMERIC


class TestCoverageReport:
    def test_returns_tuple_for_both_mode(self):
        result = coverage(DIGITS, mode="both")
        assert isinstance(result, tuple)
        assert len(result) == 2
        sub_r, sup_r = result
        assert isinstance(sub_r, CoverageReport)
        assert isinstance(sup_r, CoverageReport)

    def test_returns_single_for_subscript_mode(self):
        result = coverage(DIGITS, mode="subscript")
        assert isinstance(result, CoverageReport)
        assert result.mode == "subscript"

    def test_returns_single_for_superscript_mode(self):
        result = coverage(DIGITS, mode="superscript")
        assert isinstance(result, CoverageReport)
        assert result.mode == "superscript"

    def test_invalid_mode_raises(self):
        with pytest.raises(ValueError, match="mode must be"):
            coverage(DIGITS, mode="invalid")

    def test_digits_fully_covered_subscript(self):
        report = coverage(DIGITS, mode="subscript")
        assert len(report.unsupported) == 0
        assert report.percent == 100.0

    def test_digits_fully_covered_superscript(self):
        report = coverage(DIGITS, mode="superscript")
        assert len(report.unsupported) == 0
        assert report.percent == 100.0

    def test_uppercase_mostly_unsupported_subscript(self):
        report = coverage(UPPERCASE, mode="subscript")
        # No uppercase subscripts exist in Unicode
        assert len(report.unsupported) == 26
        assert len(report.supported) == 0

    def test_percent_calculation(self):
        # 10 digits, all supported = 100%
        report = coverage(DIGITS, mode="subscript")
        assert report.percent == 100.0
        assert report.total == 10

    def test_empty_chars(self):
        report = coverage("", mode="subscript")
        assert report.total == 0
        assert report.percent == 0.0

    def test_str_output_contains_mode(self):
        report = coverage(DIGITS, mode="subscript")
        output = str(report)
        assert "subscript" in output
        assert "10/10" in output

    def test_str_output_lists_unsupported(self):
        report = coverage(UPPERCASE, mode="subscript")
        output = str(report)
        assert "Unsupported" in output


class TestCheck:
    def test_returns_dict(self):
        result = check("insp")
        assert isinstance(result, dict)

    def test_known_sub_char(self):
        result = check("i")
        assert result["i"]["sub"] == "\u1D62"  # ᵢ

    def test_known_sup_char(self):
        result = check("2")
        assert result["2"]["sup"] == "\u00B2"  # ²

    def test_unknown_char_returns_none(self):
        result = check("Q")
        assert result["Q"]["sub"] is None
        assert result["Q"]["sup"] is None

    def test_unique_chars_only(self):
        # "aaa" should give only one entry
        result = check("aaa")
        assert list(result.keys()) == ["a"]

    def test_preserves_order(self):
        result = check("insp")
        assert list(result.keys()) == ["i", "n", "s", "p"]

    def test_full_string(self):
        result = check("t_insp")
        # _ has no sub/sup
        assert result["_"]["sub"] is None
        assert result["_"]["sup"] is None
        assert result["i"]["sub"] is not None
