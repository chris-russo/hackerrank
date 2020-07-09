from typing import List
import math


# https://www.hackerrank.com/challenges/grading/problem
def grading_students(grades: List[int]) -> List[int]:
    return list(map(apply_grading_rules, grades))


def apply_grading_rules(score: int) -> int:
    if score < 38:
        return score
    elif abs(score - base_ceil(score)) < 3:
        return base_ceil(score)
    else:
        return score


def base_ceil(x: int, base: int = 5) -> int:
    return base * math.ceil(x / base)


