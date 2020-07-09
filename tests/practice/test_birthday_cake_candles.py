import pytest
from typing import List
from src.practice import birthday_cake_candles


@pytest.mark.parametrize(
    'arr,expected',
    [
        ([3, 2, 1, 3], 2),
        ([5, 5, 1, 9, 10, 11, 10], 1),
        ([10, 18, 90, 90, 13, 90, 75, 90, 8, 90, 43], 5),
    ],
)
def test_birthday_cake_candles(arr: List[int], expected: int) -> None:
    assert birthday_cake_candles(arr) == expected

