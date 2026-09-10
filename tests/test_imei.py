import pytest

from imei_validator.imei import InvalidIMEIError, is_valid_imei, validate_imei

VALID_IMEI = "490154203237518"


def test_is_valid_imei_accepts_known_good_number():
    assert is_valid_imei(VALID_IMEI) is True


def test_is_valid_imei_rejects_bad_checksum():
    assert is_valid_imei("490154203237510") is False


def test_is_valid_imei_rejects_wrong_length():
    assert is_valid_imei("1234") is False


def test_is_valid_imei_rejects_non_digit_characters():
    assert is_valid_imei("49015420323751A") is False


def test_validate_imei_accepts_valid_imei():
    assert validate_imei(VALID_IMEI) is None


def test_validate_imei_raises_with_specific_message_on_bad_checksum():
    with pytest.raises(InvalidIMEIError, match="Luhn checksum"):
        validate_imei("490154203237510")


def test_validate_imei_raises_with_specific_message_on_wrong_length():
    with pytest.raises(InvalidIMEIError, match="15 digits"):
        validate_imei("1234")
