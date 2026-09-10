from hypothesis import given, strategies as st

from imei_validator.imei import is_valid_imei
from imei_validator.luhn import compute_check_digit

payload_strategy = st.text(alphabet="0123456789", min_size=14, max_size=14)


@given(payload=payload_strategy)
def test_generated_imei_with_correct_check_digit_is_valid(payload):
    imei = payload + compute_check_digit(payload)
    assert is_valid_imei(imei) is True


@given(
    payload=payload_strategy,
    tamper_index=st.integers(min_value=0, max_value=13),
    new_digit=st.integers(min_value=0, max_value=9),
)
def test_single_digit_tamper_always_invalidates(payload, tamper_index, new_digit):
    check_digit = compute_check_digit(payload)
    valid_imei = payload + check_digit
    original_char = valid_imei[tamper_index]
    if str(new_digit) == original_char:
        new_digit = (new_digit + 1) % 10  # force an actual change
    tampered = valid_imei[:tamper_index] + str(new_digit) + valid_imei[tamper_index + 1:]
    assert is_valid_imei(tampered) is False
