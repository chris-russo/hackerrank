from typing import List
import numpy as np


# https://www.hackerrank.com/challenges/diagonal-difference/problem
def diagonal_difference(arr: List[List[int]]) -> int:
    n = len(arr)
    diagonals = []
    reverse_diagonals = []

    for i in range(n):
        diagonals.append(arr[i][i])
        reverse_diagonals.append(arr[i][n - 1 - i])

    return abs(sum(diagonals) - sum(reverse_diagonals))


# Can't use numpy on HackerRank, but this solution also works
def diagonal_difference_with_np(arr: List[List[int]]) -> int:
    diagonal_trace = int(np.trace(arr))
    reverse_diagonal_trace = int(np.trace(np.rot90(arr)))
    return abs(diagonal_trace - reverse_diagonal_trace)
