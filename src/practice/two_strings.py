from typing import Set


# https://www.hackerrank.com/challenges/two-strings/problem
def two_strings(s1: str, s2: str) -> bool:
    s1_chars: Set[str] = set([char for char in s1])
    s2_chars: Set[str] = set([char for char in s2])
    common_chars: Set[str] = s1_chars.intersection(s2_chars)
    return True if len(common_chars) > 0 else False
