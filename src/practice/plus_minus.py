from typing import List


# https://www.hackerrank.com/challenges/plus-minus/problem
def plus_minus(arr: List[int]) -> List[str]:
    n = len(arr)
    counts = {
        'plus': 0,
        'minus': 0,
        'zero': 0
    }

    for i in arr:
        if i > 0:
            counts['plus'] += 1
        elif i < 0:
            counts['minus'] += 1
        else:
            counts['zero'] += 1

    return ['{:.6f}'.format(v / n) for v in counts.values()]
