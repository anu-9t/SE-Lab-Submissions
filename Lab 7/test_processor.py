from hypothesis import given, strategies as st
from processor import parse_transit_corridor, lookup_concession_discount, compute_passenger_density


@given(st.text() | st.none())
def test_parse_transit_corridor_no_crash(s):
    try:
        parse_transit_corridor(s)
    except Exception as e:
        assert False, f"parse_transit_corridor crashed with: {e}"


@given(st.text() | st.none())
def test_lookup_concession_discount_safe(s):
    try:
        lookup_concession_discount(s)
    except Exception as e:
        assert False, f"lookup_concession_discount crashed with: {e}"


@given(st.text() | st.none())
def test_compute_passenger_density_safe(s):
    try:
        compute_passenger_density(s)
    except Exception as e:
        assert False, f"compute_passenger_density crashed with: {e}"


# extra checks on other kinds of input

@given(st.integers() | st.floats() | st.lists(st.integers()) | st.booleans())
def test_parse_transit_corridor_non_string(x):
    try:
        parse_transit_corridor(x)
    except Exception as e:
        assert False, f"parse_transit_corridor crashed with: {e}"


@given(st.integers() | st.floats() | st.lists(st.integers()) | st.booleans())
def test_lookup_concession_discount_non_string(x):
    try:
        lookup_concession_discount(x)
    except Exception as e:
        assert False, f"lookup_concession_discount crashed with: {e}"


@given(st.integers() | st.floats() | st.lists(st.integers()) | st.booleans())
def test_compute_passenger_density_non_string(x):
    try:
        compute_passenger_density(x)
    except Exception as e:
        assert False, f"compute_passenger_density crashed with: {e}"


@given(st.integers(min_value=0, max_value=1000), st.integers(min_value=1, max_value=1000))
def test_compute_passenger_density_valid(p, km):
    assert compute_passenger_density(f"{p}/{km}") == round(p / km, 2)


@given(st.sampled_from(["standard", "student", "senior", "military", "child"]))
def test_lookup_concession_discount_known(name):
    assert lookup_concession_discount(f" {name} ") is not None
