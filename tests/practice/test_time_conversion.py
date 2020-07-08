import pytest
from src.practice import time_conversion


@pytest.mark.parametrize(
    't,expected',
    [
        ('07:05:45PM', '19:05:45'),
        ('12:05:59AM', '00:05:59'),
        ('12:00:00PM', '12:00:00'),
        ('11:00:00PM', '23:00:00'),
    ]
)
def test_time_conversion(t, expected):
    assert time_conversion(t) == expected
