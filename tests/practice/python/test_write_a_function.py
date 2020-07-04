import pytest
from src.practice.python.write_a_function import is_leap_year


@pytest.mark.parametrize(
    'year,expected',
    [
        (2000, True),
        (2400, True),
        (1992, True),
        (1800, False),
        (1900, False),
        (2100, False),
        (2200, False),
        (2300, False),
        (2500, False),
    ]
)
def test_is_leap_year(year, expected):
    assert is_leap_year(year) == expected
