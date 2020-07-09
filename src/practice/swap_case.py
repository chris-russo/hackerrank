# https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s: str) -> str:
    chars = [char for char in s]
    transformed_chars = list(
        map(lambda x: x.lower() if x.lower() != x else x.upper(), chars)
    )
    return ''.join(transformed_chars)
