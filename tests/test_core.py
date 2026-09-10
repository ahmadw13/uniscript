"""Tests for _core.py — sub(), sup(), translate()."""

import pytest
from uniscript import sub, sup, FallbackMode
from uniscript._errors import SubstitutionError


class TestSub:
    def test_digits(self):
        assert sub("0123456789") == "₀₁₂₃₄₅₆₇₈₉"

    def test_known_letters(self):
        assert sub("insp") == "ᵢₙₛₚ"

    def test_symbols(self):
        assert sub("(n+1)") == "₍ₙ₊₁₎"

    def test_empty_string(self):
        assert sub("") == ""

    def test_fallback_passthrough(self):
        # 'q' has no subscript — should pass through unchanged
        result = sub("q", fallback=FallbackMode.PASSTHROUGH)
        assert result == "q"

    def test_fallback_omit(self):
        result = sub("q", fallback=FallbackMode.OMIT)
        assert result == ""

    def test_fallback_raise(self):
        with pytest.raises(SubstitutionError):
            sub("q", fallback=FallbackMode.RAISE)

    def test_mixed_known_unknown(self):
        # 'a' is known, 'q' is not — passthrough keeps 'q'
        result = sub("aq", fallback=FallbackMode.PASSTHROUGH)
        assert result == "ₐq"


class TestSup:
    def test_digits(self):
        assert sup("0123456789") == "⁰¹²³⁴⁵⁶⁷⁸⁹"

    def test_common_exponent(self):
        assert sup("2") == "²"
        assert sup("3") == "³"

    def test_letters(self):
        assert sup("n") == "ⁿ"
        assert sup("th") == "ᵗʰ"

    def test_expression(self):
        assert sup("n+1") == "ⁿ⁺¹"

    def test_empty_string(self):
        assert sup("") == ""

    def test_fallback_passthrough(self):
        # 'Q' (uppercase) has no superscript — should pass through
        result = sup("Q", fallback=FallbackMode.PASSTHROUGH)
        assert result == "Q"

    def test_fallback_raise(self):
        with pytest.raises(SubstitutionError):
            sup("Q", fallback=FallbackMode.RAISE)
