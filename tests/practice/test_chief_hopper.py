import pytest
from typing import List

from src.practice import chief_hopper, update_energy


@pytest.mark.parametrize(
    'arr,expected',
    [
        ([3, 4, 3, 2, 4], 4),
        ([4, 4, 4], 4),
    ],
)
def test_chief_hopper(arr: List[int], expected: int) -> None:
    assert chief_hopper(arr) == expected


@pytest.mark.parametrize(
    'energy,height,expected',
    [
        (10, 5, 15),
        (3, 5, 1),
        (2, 2, 2),
    ],
)
def test_new_energy(energy: int, height: int, expected: int) -> None:
    assert update_energy(energy, height) == expected
