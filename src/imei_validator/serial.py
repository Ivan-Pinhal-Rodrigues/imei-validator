"""Device serial-number format validation.

Vendor-specific decoding (e.g. recovering a manufacture date or plant code
from an Apple serial) is deliberately out of scope — see DESIGN.md.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SerialFormat:
    name: str
    length: int
    charset: frozenset[str]


APPLE_CLASSIC_FORMAT = SerialFormat(
    name="apple-classic",
    length=12,
    charset=frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"),
)


class InvalidSerialError(ValueError):
    """Raised when a string does not match the expected SerialFormat."""


def is_valid_serial(serial: str, fmt: SerialFormat) -> bool:
    """Return True if `serial` matches `fmt`'s length and character set."""
    return len(serial) == fmt.length and all(char in fmt.charset for char in serial)


def validate_serial(serial: str, fmt: SerialFormat) -> None:
    """Raise InvalidSerialError with a specific reason if `serial` doesn't match `fmt`."""
    if len(serial) != fmt.length:
        raise InvalidSerialError(
            f"{fmt.name} serial must be {fmt.length} characters, got {len(serial)}: {serial!r}"
        )
    bad_chars = sorted(set(serial) - fmt.charset)
    if bad_chars:
        raise InvalidSerialError(
            f"{fmt.name} serial has invalid characters {bad_chars}: {serial!r}"
        )
