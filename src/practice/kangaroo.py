#https://www.hackerrank.com/challenges/kangaroo/problem
def kangaroo(x1: int, v1: int, x2: int, v2: int) -> bool:
    while x1 <= 10000 and x2 <= 10000:
        x1 = x1 + v1
        x2 = x2 + v2
        if x1 == x2:
            return True
    return False



