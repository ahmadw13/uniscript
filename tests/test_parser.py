"""Tests for _parser.py — render() notation parsing."""

import pytest
from uniscript import render


class TestRenderSubscript:
    def test_basic_subscript(self):
        assert render("t_insp") == "tᵢₙₛₚ"

    def test_chemical_formula(self):
        assert render("CO_2") == "CO₂"
        assert render("H_2O") == "H₂O"

    def test_subscript_at_end(self):
        assert render("x_0") == "x₀"

    def test_subscript_mid_string(self):
        # subscript ends at space
        assert render("x_0 and y_1") == "x₀ and y₁"


class TestRenderSuperscript:
    def test_basic_superscript(self):
        assert render("E=mc^2") == "E=mc²"

    def test_exponent_expression(self):
        assert render("x^(n+1)") == "xⁿ⁺¹"

    def test_ordinal(self):
        assert render("1^st") == "1ˢᵗ"


class TestRenderMixed:
    def test_sub_and_sup(self):
        assert render("x_0^2") == "x₀²"

    def test_no_markers(self):
        # plain text passes through unchanged
        assert render("hello") == "hello"

    def test_empty(self):
        assert render("") == ""


class TestRenderEdgeCases:
    def test_double_underscore(self):
        # treat literal underscore with no following word → passthrough
        result = render("a_")
        assert isinstance(result, str)

    def test_caret_at_end(self):
        result = render("a^")
        assert isinstance(result, str)
