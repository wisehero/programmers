import math


def solution(numer1, denom1, numer2, denom2):
    answer = []
    l = int(lcm(denom1, denom2))
    n = numer1 * (l // denom1) + numer2 * (l // denom2)
    answer.append(n)
    answer.append(l)

    while math.gcd(answer[0], answer[1]) != 1:
        z = math.gcd(answer[0], answer[1])
        answer[0] = answer[0] // z
        answer[1] = answer[1] // z
    return answer


def lcm(a, b):
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            return i


print(solution(4,4,4,4))
