import pytest

from src.practice import kangaroo


@pytest.mark.parametrize(
    'x1,v1,x2,v2,expected',
    [
        (0, 2, 5, 3, False),
        (0, 3, 4, 2, True),
        (240, 575, 9179, 9986, False),
        (2564, 5393, 5121, 2836, True),
    ]
)
def test_kangaroo(x1: int, v1: int, x2: int, v2: int, expected: bool) -> None:
    assert kangaroo(x1, v1, x2, v2) is expected
