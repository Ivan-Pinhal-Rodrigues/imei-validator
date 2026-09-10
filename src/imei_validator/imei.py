"""IMEI (International Mobile Equipment Identity) validation."""

from .luhn import is_valid_luhn

IMEI_LENGTH = 15


class InvalidIMEIError(ValueError):
    """Raised when a string is not a well-formed, checksum-valid IMEI."""


def is_valid_imei(imei: str) -> bool:
    """Return True if `imei` is exactly 15 digits and passes the Luhn check."""
    if len(imei) != IMEI_LENGTH or not (imei.isascii() and imei.isdigit()):
        return False
    return is_valid_luhn(imei)


def validate_imei(imei: str) -> None:
    """Raise InvalidIMEIError with a specific reason if `imei` is invalid."""
    if not (imei.isascii() and imei.isdigit()):
        raise InvalidIMEIError(f"IMEI must contain only digits, got {imei!r}")
    if len(imei) != IMEI_LENGTH:
        raise InvalidIMEIError(
            f"IMEI must be {IMEI_LENGTH} digits, got {len(imei)}: {imei!r}"
        )
    if not is_valid_luhn(imei):
        raise InvalidIMEIError(f"IMEI {imei!r} fails the Luhn checksum")
