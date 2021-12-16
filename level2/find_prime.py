import itertools
import math


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    dup = []
    for i in range(1, len(numbers) + 1):
        print(i)
        li = list(itertools.permutations(numbers, i))

        for j in range(len(li)):
            if is_prime_number(int("".join(li[j]))) and int("".join(li[j])) not in dup:
                answer += 1
                dup.append(int("".join(li[j])))
        print(answer)
    return answer


def is_prime_number(x):
    if x == 1 or x == 0:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):

        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임
