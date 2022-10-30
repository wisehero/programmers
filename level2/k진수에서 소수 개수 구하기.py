import math


def solution(n, k):
    answer = 0
    converted = convert(n, k).split("0")

    for i in converted:
        if i.isdigit():
            if is_prime_number(int(i)):
                answer += 1
    print(answer)
    return answer


def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def convert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


solution(437674, 3)
