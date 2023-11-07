from collections import Counter


def solution(want, number, discount):
    answer = 0
    d1 = {}

    for i in range(len(want)):
        d1[want[i]] = number[i]

    for i in range(len(discount)):
        d2 = Counter(discount[i:i + 10])

        if d1 == d2:
            answer += 1

    return answer
