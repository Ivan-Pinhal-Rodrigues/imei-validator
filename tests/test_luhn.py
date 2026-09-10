import pytest

from imei_validator.luhn import InvalidLuhnInputError, compute_check_digit, is_valid_luhn


def test_known_valid_imei_passes_luhn():
    assert is_valid_luhn("490154203237518") is True


def test_single_digit_tamper_fails_luhn():
    tampered = "490154203237510"  # last digit changed 8 -> 0
    assert is_valid_luhn(tampered) is False


def test_compute_check_digit_matches_known_example():
    assert compute_check_digit("49015420323751") == "8"


def test_is_valid_luhn_rejects_non_digits():
    with pytest.raises(InvalidLuhnInputError):
        is_valid_luhn("49015420323751X")


def test_is_valid_luhn_rejects_fullwidth_digits():
    # Fullwidth digits pass str.isdigit() but are not ASCII '0'-'9'; they must
    # be rejected as invalid input, not silently accepted as digits.
    with pytest.raises(InvalidLuhnInputError):
        is_valid_luhn("４９０１５４２０３２３７５１８")
