from itertools import combinations


def solution(numbers):
    answer = []

    for case in list(combinations(numbers, 2)):
        answer.append(sum(case))

    answer = set(answer)
    answer = list(answer)
    answer.sort()

    return answer
