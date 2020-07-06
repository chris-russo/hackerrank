import pytest
from src.practice import plus_minus


@pytest.mark.parametrize(
    'arr,expected',
    [
        (
            [-4, 3, -9, 0, 4, 1],
            ['0.500000', '0.333333', '0.166667']
        ),
        (
            [-92, -21, -93, -27, -45, -63, 53, 45, 0, 6, -67, 84, 96, 86, 18,
             36, 53, 0, 47, 88, 91, -59, 65, 62, 3, 13, 0, -49, -47, 94, -63,
             65, -23, 48, -5, 0, -10, 67, -23, 19, -11, 46, 80, -83, 0, -40, 74,
             -63, -20, -72, 98, -72, 66, 0, -58, -1, 67, -22, 8, -45, 32, -65,
             0, -10, -65, -81, -36, -55, -99, -18, -82],
            ['0.408451', '0.492958', '0.098592']
        ),
    ],
)
def test_plus_minus(arr, expected):
    assert plus_minus(arr) == expected
