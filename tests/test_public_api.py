def test_public_api_is_importable_from_package_root():
    from imei_validator import (
        APPLE_CLASSIC_FORMAT,
        InvalidIMEIError,
        InvalidLuhnInputError,
        InvalidSerialError,
        SerialFormat,
        compute_check_digit,
        is_valid_imei,
        is_valid_luhn,
        is_valid_serial,
        validate_imei,
        validate_serial,
    )

    assert is_valid_imei("490154203237518") is True
    assert isinstance(APPLE_CLASSIC_FORMAT, SerialFormat)
    assert issubclass(InvalidIMEIError, ValueError)
    assert issubclass(InvalidSerialError, ValueError)
    assert issubclass(InvalidLuhnInputError, ValueError)
    assert callable(compute_check_digit)
    assert callable(is_valid_luhn)
    assert callable(validate_imei)
    assert callable(is_valid_serial)
    assert callable(validate_serial)
