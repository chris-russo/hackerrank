import pytest
from src.practice import a_very_big_sum


@pytest.mark.parametrize(
    'ar,expected',
    [
        (
            [1000000001, 1000000002, 1000000003, 1000000004, 1000000005],
            5000000015
        ),
        (
            [1001458909, 1004570889, 1007019111, 1003302837, 1002514638,
             1006431461, 1002575010, 1007514041, 1007548981, 1004402249],
            10047338126
        )
    ]
)
def test_a_very_big_sum(ar, expected):
    assert a_very_big_sum(ar) == expected

