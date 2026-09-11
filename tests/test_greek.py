"""Tests for Greek letter support — _greek.py, _tables.py, and render() integration."""

import pytest
from uniscript import sub, sup, render
from uniscript._greek import resolve_shorthands, GREEK_SHORTHANDS


class TestGreekShorthands:
    def test_all_24_lowercase_present(self):
        lowercase = [
            "alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta",
            "theta", "iota", "kappa", "lambda", "mu", "nu", "xi", "omicron",
            "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega",
        ]
        for name in lowercase:
            assert name in GREEK_SHORTHANDS, f"\\{name} missing from GREEK_SHORTHANDS"

    def test_all_24_uppercase_present(self):
        uppercase = [
            "Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta",
            "Theta", "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron",
            "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega",
        ]
        for name in uppercase:
            assert name in GREEK_SHORTHANDS, f"\\{name} missing from GREEK_SHORTHANDS"

    def test_values_are_greek_unicode(self):
        for name, char in GREEK_SHORTHANDS.items():
            cp = ord(char)
            assert 0x0391 <= cp <= 0x03C9, (
                f"\\{name} maps to U+{cp:04X} which is outside the Greek block"
            )


class TestResolveShorthands:
    def test_single_shorthand(self):
        assert resolve_shorthands(r"\beta") == "β"

    def test_shorthand_in_subscript_notation(self):
        assert resolve_shorthands(r"x_\beta") == "x_β"

    def test_shorthand_in_superscript_notation(self):
        assert resolve_shorthands(r"x^\gamma") == "x^γ"

    def test_multiple_shorthands(self):
        result = resolve_shorthands(r"\alpha + \beta")
        assert result == "α + β"

    def test_no_shorthands_passthrough(self):
        assert resolve_shorthands("t_insp") == "t_insp"

    def test_fast_path_no_backslash(self):
        # Should return same object (fast path) when no backslash present
        text = "hello world"
        assert resolve_shorthands(text) == text

    def test_unknown_shorthand_passthrough(self):
        assert resolve_shorthands(r"\unknown") == r"\unknown"

    def test_theta_does_not_match_tau_prefix(self):
        # Greedy match: \theta should resolve fully, not stop at \t
        assert resolve_shorthands(r"\theta") == "θ"

    def test_uppercase_shorthand(self):
        assert resolve_shorthands(r"\Sigma") == "Σ"
        assert resolve_shorthands(r"\Omega") == "Ω"

    def test_shorthand_followed_by_alpha_char_not_matched(self):
        # \betas should NOT match \beta because 's' is alpha — it's a longer word
        result = resolve_shorthands(r"\betas")
        assert result == r"\betas"

    def test_empty_string(self):
        assert resolve_shorthands("") == ""


class TestGreekSubSup:
    """Test that Greek chars pass through sub()/sup() correctly."""

    def test_sub_beta(self):
        assert sub("β") == "ᵦ"

    def test_sub_gamma(self):
        assert sub("γ") == "ᵧ"

    def test_sub_rho(self):
        assert sub("ρ") == "ᵨ"

    def test_sub_phi(self):
        assert sub("φ") == "ᵩ"

    def test_sub_chi(self):
        assert sub("χ") == "ᵪ"

    def test_sup_beta(self):
        assert sup("β") == "ᵝ"

    def test_sup_gamma(self):
        assert sup("γ") == "ᵞ"

    def test_sup_delta(self):
        assert sup("δ") == "ᵟ"

    def test_sup_theta(self):
        assert sup("θ") == "ᶿ"

    def test_sup_phi(self):
        assert sup("φ") == "ᵠ"

    def test_sup_chi(self):
        assert sup("χ") == "ᵡ"


class TestGreekRenderIntegration:
    def test_shorthand_subscript(self):
        assert render(r"x_\beta") == "xᵦ"

    def test_shorthand_superscript(self):
        assert render(r"x^\gamma") == "xᵞ"

    def test_greek_base_latin_subscript(self):
        assert render(r"\sigma_x") == "σₓ"

    def test_greek_base_digit_subscript(self):
        assert render(r"\rho_0") == "ρ₀"

    def test_direct_greek_subscript(self):
        # Raw Greek char in subscript position
        assert render("x_β") == "xᵦ"

    def test_direct_greek_superscript(self):
        assert render("x^δ") == "xᵟ"

    def test_mixed_latin_greek(self):
        assert render(r"E_\gamma^2") == "Eᵧ²"
