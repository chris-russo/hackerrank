import pytest
from typing import List

from src.practice import grading_students


@pytest.mark.parametrize(
    'grades,expected',
    [
        ([73, 67, 38, 33], [75, 67, 40, 33]),
        ([37, 38], [37, 40]),
    ]
)
def test_grading_students(grades: List[int], expected: List[int]) -> None:
    assert grading_students(grades) == expected
