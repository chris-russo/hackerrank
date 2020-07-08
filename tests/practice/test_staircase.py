import pytest
from src.practice.staircase import staircase


@pytest.mark.parametrize(
    'n,expected',
    [
        (2, [' #', '##']),
        (5, ['    #', '   ##', '  ###', ' ####', '#####'])
    ]
)
def test_staircase(n, expected):
    assert staircase(n) == expected
