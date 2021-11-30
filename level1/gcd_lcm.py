import math


def solution(n, m):
    answer = []
    answer.append(math.gcd(n, m))
    answer.append(lcm(n, m))
    return answer


def lcm(x, y):
    result = (x * y) // math.gcd(x, y)
    return result
