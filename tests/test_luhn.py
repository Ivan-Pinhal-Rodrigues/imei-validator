import pytest

from imei_validator.luhn import compute_check_digit, is_luhn_valid


def test_known_valid_imei_passes_luhn():
    assert is_luhn_valid("490154203237518") is True


def test_single_digit_tamper_fails_luhn():
    tampered = "490154203237510"  # last digit changed 8 -> 0
    assert is_luhn_valid(tampered) is False


def test_compute_check_digit_matches_known_example():
    assert compute_check_digit("49015420323751") == "8"


def test_is_luhn_valid_rejects_non_digits():
    with pytest.raises(ValueError):
        is_luhn_valid("49015420323751X")
