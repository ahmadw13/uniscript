"""Tests for _tables.py — verifies coverage and correctness of SUB_MAP / SUP_MAP."""

import pytest
from uniscript._tables import SUB_MAP, SUP_MAP


class TestSubMap:
    def test_all_digits_present(self):
        for d in "0123456789":
            assert d in SUB_MAP, f"Digit {d!r} missing from SUB_MAP"

    def test_all_digits_are_single_chars(self):
        for d in "0123456789":
            assert len(SUB_MAP[d]) == 1

    def test_symbols_present(self):
        for sym in "+-=()":
            assert sym in SUB_MAP, f"Symbol {sym!r} missing from SUB_MAP"

    def test_known_letters_present(self):
        # These are the letters Unicode guarantees subscript forms for
        for ch in "aehiklmnoprstuvx":
            assert ch in SUB_MAP, f"Letter {ch!r} missing from SUB_MAP"

    def test_no_empty_values(self):
        for k, v in SUB_MAP.items():
            assert v, f"Empty value for key {k!r} in SUB_MAP"

    def test_values_are_not_ascii(self):
        for k, v in SUB_MAP.items():
            assert ord(v) > 127, f"Value for {k!r} looks like plain ASCII: {v!r}"


class TestSupMap:
    def test_all_digits_present(self):
        for d in "0123456789":
            assert d in SUP_MAP, f"Digit {d!r} missing from SUP_MAP"

    def test_all_digits_are_single_chars(self):
        for d in "0123456789":
            assert len(SUP_MAP[d]) == 1

    def test_symbols_present(self):
        for sym in "+-=()":
            assert sym in SUP_MAP, f"Symbol {sym!r} missing from SUP_MAP"

    def test_known_letters_present(self):
        for ch in "abcdefghjklmnoprstuvwxyz":
            assert ch in SUP_MAP, f"Letter {ch!r} missing from SUP_MAP"

    def test_no_empty_values(self):
        for k, v in SUP_MAP.items():
            assert v, f"Empty value for key {k!r} in SUP_MAP"

    def test_values_are_not_ascii(self):
        for k, v in SUP_MAP.items():
            assert ord(v) > 127, f"Value for {k!r} looks like plain ASCII: {v!r}"
