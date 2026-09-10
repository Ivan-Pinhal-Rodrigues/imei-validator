"""Regression tests: non-ASCII digit characters must never be treated as valid.

`str.isdigit()` returns True for a much broader set of characters than the
ASCII '0'-'9' this package's checksum math actually assumes:

- Real-valued Unicode decimal digits (fullwidth, Arabic-Indic, Devanagari,
  ...) are accepted by `int()`, so a naive `.isdigit()` guard lets them
  through as a false accept.
- Non-decimal digit-like characters (e.g. superscript '2') are accepted by
  `.isdigit()` but rejected by `int()`, so a naive guard lets them reach code
  that raises an uncaught ValueError instead of failing validation cleanly.

`is_valid_imei` must return False (never raise) for all of these.
"""

from imei_validator.imei import is_valid_imei

FULLWIDTH_IMEI = "４９０１５４２０３２３７５１８"
ARABIC_INDIC_IMEI = "٤٩٠١٥٤٢٠٣٢٣٧٥١٨"
SUPERSCRIPT_TWOS = "²" * 15


def test_is_valid_imei_rejects_fullwidth_digits():
    assert is_valid_imei(FULLWIDTH_IMEI) is False


def test_is_valid_imei_rejects_arabic_indic_digits():
    assert is_valid_imei(ARABIC_INDIC_IMEI) is False


def test_is_valid_imei_rejects_superscript_digits():
    assert is_valid_imei(SUPERSCRIPT_TWOS) is False
