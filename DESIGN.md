# Design decisions

## Why Luhn, implemented from scratch

The IMEI check digit is defined by the Luhn algorithm (the same one behind
credit-card number validation). It would be easy to depend on a generic
`luhn` library from PyPI, but the point of this package is demonstrating an
understanding of the checksum, not just calling something that implements
it. `luhn.py` is about fifteen lines and every line is explainable: double
every second digit from the right, fold values over 9 by subtracting 9, sum
everything, check divisibility by 10.

## Why a separate `luhn.py` instead of inlining it into `imei.py`

The Luhn algorithm isn't IMEI-specific. Keeping it as a standalone module
with a generic `is_luhn_valid(number: str)` signature makes it reusable for
any other Luhn-checked identifier without touching IMEI-specific code.

## Why serial-number decoding stops at format validation

Older Apple serial numbers had a documented structure (plant, year, week,
unique ID, model code). Current-generation serials no longer follow a
publicly documented scheme — Apple has obscured it since around 2021, and
reverse-engineered mappings for older formats drift and go stale. Shipping
a decoder that quietly returns wrong manufacture dates would be worse than
not shipping one. `SerialFormat` validates structure only, and is left open
— a caller can define a new `SerialFormat` for any vendor without touching
this package's code — rather than hardcoding one vendor's internal encoding
as settled fact.

## Why `src/` layout

The package lives under `src/imei_validator/` rather than a top-level
`imei_validator/`. Without `src/`, running `pytest` from the repo root can
accidentally import the package from the working directory instead of the
installed one, silently hiding packaging bugs. `src/` layout forces tests
to exercise the actually-installed package, the same way a downstream
consumer would use it.

## Why Hatchling over setuptools

Both work for a pure-Python package. Hatchling needs less configuration
when there are no compiled extensions, and is what current Python
packaging documentation recommends for new projects.

## What I'd change at real scale

- Add a TAC (Type Allocation Code) lookup against a maintained database to
  resolve IMEI to device model, if a consumer actually needed it.
- Widen CI to a Python version matrix (currently pinned to one version to
  keep the pipeline simple for a package this size).
- Add mutation testing (e.g. `mutmut`) to verify the test suite would
  actually catch a broken Luhn implementation, not just pass a correct one.
