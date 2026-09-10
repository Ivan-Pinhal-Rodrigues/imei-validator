"""Generic Luhn checksum algorithm (ISO/IEC 7812), reused by IMEI validation."""


class InvalidLuhnInputError(ValueError):
    """Raised when input to a Luhn function isn't a valid digit string."""


def _luhn_digit_sum(digits: str) -> int:
    """Sum of digits after doubling every second digit counted from the right.

    The rightmost digit is left untouched; the digit immediately to its left
    is doubled, then every second digit after that. A doubled digit over 9
    has its own two digits summed (equivalent to subtracting 9).
    """
    total = 0
    for index, char in enumerate(reversed(digits)):
        value = int(char)
        if index % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value
    return total


def is_valid_luhn(number: str) -> bool:
    """Return True if `number` (digits, check digit included) passes Luhn."""
    if not (number.isascii() and number.isdigit()):
        raise InvalidLuhnInputError(f"expected only digits, got {number!r}")
    return _luhn_digit_sum(number) % 10 == 0


def compute_check_digit(payload: str) -> str:
    """Return the Luhn check digit for `payload` (digits, check digit excluded)."""
    if not (payload.isascii() and payload.isdigit()):
        raise InvalidLuhnInputError(f"expected only digits, got {payload!r}")
    # Appending "0" lines up the indices exactly as if the check digit were
    # already there but equal to zero, so the payload's own rightmost digit
    # falls on the doubled position — same math `is_valid_luhn` uses.
    total = _luhn_digit_sum(payload + "0")
    return str((10 - total % 10) % 10)
