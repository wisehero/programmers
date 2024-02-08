from itertools import permutations
import math


def is_prime(n):
    if n in [0, 1]:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    sett = set()
    for i in range(1, len(numbers) + 1):
        for p in list(permutations(numbers, i)):
            prime = is_prime(int("".join(p)))
            if prime:
                sett.add(int("".join(p)))

    answer = len(sett)
    return answer
