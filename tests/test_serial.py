import pytest

from imei_validator.serial import (
    APPLE_CLASSIC_FORMAT,
    InvalidSerialError,
    is_valid_serial,
    validate_serial,
)


def test_valid_apple_classic_serial_accepted():
    assert is_valid_serial("C02D12345678", APPLE_CLASSIC_FORMAT) is True


def test_wrong_length_rejected():
    assert is_valid_serial("SHORT", APPLE_CLASSIC_FORMAT) is False


def test_lowercase_rejected():
    assert is_valid_serial("c02d12345678", APPLE_CLASSIC_FORMAT) is False


def test_validate_serial_raises_on_wrong_length():
    with pytest.raises(InvalidSerialError, match="12 characters"):
        validate_serial("SHORT", APPLE_CLASSIC_FORMAT)


def test_validate_serial_raises_on_bad_characters():
    with pytest.raises(InvalidSerialError, match="invalid characters"):
        validate_serial("c02d1234567!", APPLE_CLASSIC_FORMAT)
