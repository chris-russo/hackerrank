from typing import List


# https://www.hackerrank.com/challenges/most-commons/problem
def most_commons(s: str) -> List[tuple]:
    char_counts = {k: 0 for k in set(s)}
    for char in s:
        char_counts[char] += 1

    output = []
    for i in range(3):
        max_value = max(char_counts.values())
        max_keys = sorted(
            [(k, v) for k, v in char_counts.items() if v == max_value],
            key=lambda x: x[0]
        )
        output.append(max_keys[0])
        char_counts.pop(max_keys[0][0], None)

    return output

