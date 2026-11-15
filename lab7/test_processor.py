from hypothesis import given, strategies as st, settings
from processor import (
    parse_transit_corridor,
    lookup_concession_discount,
    compute_passenger_density,
)


@given(st.text() | st.none())
@settings(max_examples=200)
def test_parse_transit_corridor_no_crash(s):
    """Property: parse_transit_corridor must never raise an exception."""
    try:
        result = parse_transit_corridor(s)
        # Result should be a string (either a valid route description or an error message)
        assert isinstance(result, str), f"Expected str, got {type(result)}"
    except Exception as e:
        assert False, f"parse_transit_corridor crashed with: {type(e).__name__}: {e}"


@given(st.text() | st.none())
@settings(max_examples=200)
def test_lookup_concession_discount_safe(s):
    """Property: lookup_concession_discount must never raise an exception."""
    try:
        result = lookup_concession_discount(s)
        # Result is either a float multiplier or an error string
        assert isinstance(result, (float, str)), f"Unexpected type: {type(result)}"
        if isinstance(result, float):
            assert 0.0 <= result <= 1.0, f"Multiplier out of expected range: {result}"
    except Exception as e:
        assert False, f"lookup_concession_discount crashed with: {type(e).__name__}: {e}"


@given(st.text() | st.none())
@settings(max_examples=200)
def test_compute_passenger_density_safe(s):
    """Property: compute_passenger_density must never raise an exception."""
    try:
        result = compute_passenger_density(s)
        # Result is either a float density or an error string
        assert isinstance(result, (float, str, int)), f"Unexpected type: {type(result)}"
        if isinstance(result, (float, int)):
            assert result >= 0, f"Density should not be negative: {result}"
    except Exception as e:
        assert False, f"compute_passenger_density crashed with: {type(e).__name__}: {e}"
