from typing import List, Tuple


# https://www.hackerrank.com/challenges/apple-and-orange/problem
def count_apples_and_oranges(
    s: int,
    t: int,
    a: int,
    b: int,
    apples: List[int],
    oranges: List[int]
) -> Tuple[int, int]:
    apples_positions = get_fruit_positions(a, apples)
    oranges_positions = get_fruit_positions(b, oranges)
    apple_count = len(filter_fruit(s, t, apples_positions))
    orange_count = len(filter_fruit(s, t, oranges_positions))
    return apple_count, orange_count


def get_fruit_positions(
    tree_position: int,
    distances_thrown: List[int]
) -> List[int]:
    return list(map(lambda x: tree_position + x, distances_thrown))


def filter_fruit(s: int, t: int, positions: List[int]) -> List[int]:
    return list(filter(lambda x: s <= x <= t, positions))
