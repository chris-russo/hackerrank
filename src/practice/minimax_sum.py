from typing import List, Tuple


# https://www.hackerrank.com/challenges/mini-max-sum/problem
def minimax_sum(arr: List[int]) -> Tuple[int, int]:
    n = len(arr)
    arr.sort()
    min_sum = sum(arr[:n-1])
    arr.sort(reverse=True)
    max_sum = sum(arr[:n-1])
    return min_sum, max_sum
