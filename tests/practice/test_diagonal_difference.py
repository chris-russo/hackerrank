import pytest
from src.practice import diagonal_difference, diagonal_difference_with_np


@pytest.mark.parametrize(
    'arr,expected',
    [
        (
            [[11, 2, 4],
             [4, 5, 6],
             [10, 8, - 12]],
            15
        ),
        (
            [[6, 8],
             [-6, 9]],
            13
        )
    ]
)
def test_diagonal_difference(arr, expected):
    assert diagonal_difference(arr) == expected
    assert diagonal_difference_with_np(arr) == expected
