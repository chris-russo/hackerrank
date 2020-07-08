import pytest
from src.practice import minimax_sum


@pytest.mark.parametrize(
    'arr,expected',
    [
        ([1, 3, 5, 7, 9], (16, 24)),
    ]
)
def test_minimax_sum(arr, expected):
    assert minimax_sum(arr) == expected
