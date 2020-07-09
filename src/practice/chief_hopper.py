from typing import List
import math


# https://www.hackerrank.com/challenges/chief-hopper/problem
def chief_hopper(arr: List[int]):
    energy = max(arr)
    i = 0
    tables = {}
    last_delta = 1  # Pick any arbitrary positive number
    while last_delta >= 0:
        tables[i] = []
        for height in arr:
            tables[i].append([energy, height, energy - height])
            energy = update_energy(energy, height)

        last_delta = tables[i][-1][-1]
        energy = math.ceil(tables[i][0][0] / 2)
        i += 1

    return tables[i - 2][0][0] if last_delta < 0 else tables[i - 1][0][0]


def update_energy(energy: int, height: int) -> int:
    return (
        energy - (height - energy) if energy < height
        else energy + (energy - height)
    )

