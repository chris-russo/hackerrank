from typing import List


# https://www.hackerrank.com/challenges/staircase/problem
def staircase(n: int) -> List[str]:
    steps = [f'{" " * (n - i)}{"#" * i}' for i in range(1, n + 1)]
    for step in steps:
        print(step)
    return steps
