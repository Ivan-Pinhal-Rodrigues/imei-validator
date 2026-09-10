# imei-validator

Correctness-focused validation for IMEI numbers (Luhn checksum) and device
serial numbers, extracted and generalized from a real internal tool that
reads iPhone serial numbers and IMEIs.

## Why this exists

Device-intake and asset-tracking workflows need to reject bad IMEIs and
malformed serial numbers before they reach a database or ERP system. Getting
the checksum math right — and being able to prove it's right — matters more
than getting something that looks plausible.

## Install

```bash
pip install imei-validator
```

## Usage

```python
from imei_validator import is_valid_imei, validate_imei, InvalidIMEIError

is_valid_imei("490154203237518")  # True

try:
    validate_imei("490154203237510")
except InvalidIMEIError as exc:
    print(exc)  # IMEI '490154203237510' fails the Luhn checksum
```

```python
from imei_validator import APPLE_CLASSIC_FORMAT, is_valid_serial

is_valid_serial("C02D12345678", APPLE_CLASSIC_FORMAT)  # True
```

## What this does and doesn't do

- Validates IMEI structure and Luhn checksum. Does not look up the device
  model from the TAC (first 8 digits) — that needs a maintained external
  database, out of scope here.
- Validates serial-number *format* (length + character set) against a named
  `SerialFormat`. Does not decode manufacture date or plant from the serial
  — see [DESIGN.md](DESIGN.md) for why that's a deliberate limitation, not
  an oversight.

## Testing

```bash
pip install -e ".[dev]"
pytest
```

Includes both example-based tests and property-based tests (via
`hypothesis`) that check an invariant of the Luhn algorithm directly: any
single-digit change to a valid IMEI always invalidates it.

## Design decisions

See [DESIGN.md](DESIGN.md).
