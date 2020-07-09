import pytest
from src.practice import swap_case


@pytest.mark.parametrize(
    's,expected',
    [
        ('Www.HackerRank.com', 'wWW.hACKERrANK.COM'),
        ('Pythonist 2', 'pYTHONIST 2'),
        ("K96.5GI.sabDH3s.6iFzxMAh5IPtmWJ4w0uJ9MOWC45eoZkhaSs73gxKoQcd90Uge02cAxPnyMWtYW'TRVcO.0VnBq.sIQ5HFhkx", "k96.5gi.SABdh3S.6IfZXmaH5ipTMwj4W0Uj9mowc45EOzKHAsS73GXkOqCD90uGE02CaXpNYmwTyw'trvCo.0vNbQ.Siq5hfHKX"),
    ],
)
def test_swap_case(s, expected):
    assert swap_case(s) == expected
