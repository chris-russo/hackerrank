from typing import List


# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthday_cake_candles(arr: List[int]) -> int:
    max_candle_height = max(arr)
    return arr.count(max_candle_height)
