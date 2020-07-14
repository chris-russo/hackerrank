import pytest

from src.practice import two_strings


@pytest.mark.parametrize(
    's1,s2,expected',
    [
        ('hello', 'world', True),
        ('hi', 'world', False),
        ('wouldyoulikefries', 'abcabcabcabcabcabc', False),
        ('hackerrankcommunity', 'cdecdecdecde', True),
        ('jackandjill', 'wentupthehill', True),
        ('writetoyourparents', 'fghmqzldbc', False),
        ('aardvark', 'apple', True),
        ('beetroot', 'sandals', False),
    ]
)
def test_two_strings(s1: str, s2: str, expected: bool) -> None:
    assert two_strings(s1, s2) == expected
