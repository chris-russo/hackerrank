import pytest
from typing import List, Tuple

from src.practice import count_apples_and_oranges


@pytest.mark.parametrize(
    's,t,a,b,apples,oranges,expected',
    [
        (7, 10, 4, 12, [2, 3, -4], [3, -2, -4], (1, 2)),
        (7, 11, 5, 15, [-2, 2, 1], [5, -6], (1, 1)),
    ]
)
def test_count_apples_and_oranges(
    s: int,
    t: int,
    a: int,
    b: int,
    apples: List[int],
    oranges: List[int],
    expected: Tuple[int, int],
) -> None:
    assert count_apples_and_oranges(s, t, a, b, apples, oranges) == expected
