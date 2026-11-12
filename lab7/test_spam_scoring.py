"""Property-based fuzz tests for the spam-scoring helpers.

Run from this directory with: python -m pytest -q
"""
from hypothesis import given, strategies as st

from spam_scoring import sender_domain, first_link, shout_ratio


@given(st.one_of(st.text(), st.none(), st.integers(), st.binary()))
def test_sender_domain_never_crashes(value):
    result = sender_domain(value)
    assert isinstance(result, str)


@given(st.one_of(st.text(), st.none(), st.integers(), st.binary()))
def test_first_link_never_crashes(value):
    result = first_link(value)
    assert isinstance(result, str)


@given(st.one_of(st.text(), st.none(), st.integers(), st.binary()))
def test_shout_ratio_never_crashes(value):
    result = shout_ratio(value)
    assert isinstance(result, float)
    assert 0.0 <= result <= 1.0


@given(st.text())
def test_sender_domain_is_lowercase_and_has_no_at(value):
    result = sender_domain(value)
    assert result == result.lower()
    assert "@" not in result


@given(st.text())
def test_first_link_is_empty_or_starts_with_http(value):
    result = first_link(value)
    assert result == "" or result.lower().startswith(("http://", "https://"))


@given(st.text())
def test_shout_ratio_is_bounded(value):
    result = shout_ratio(value)
    assert 0.0 <= result <= 1.0


@given(st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu")), min_size=1))
def test_shout_ratio_matches_uppercase_fraction(value):
    expected = sum(char.isupper() for char in value) / len(value)
    assert shout_ratio(value) == expected


def test_sender_domain_valid_examples():
    assert sender_domain("offers@Deals.com") == "deals.com"
    assert sender_domain(" user@EXAMPLE.ORG ") == "example.org"


def test_first_link_valid_examples():
    assert first_link("Visit https://example.com now") == "https://example.com"
    assert first_link("http://example.org/path.") == "http://example.org/path"


def test_shout_ratio_examples_and_no_letters():
    assert shout_ratio("FREE prize NOW") == 8 / 12
    assert shout_ratio("123 !?") == 0.0
