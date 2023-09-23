def solution(number):
    answer = 0
    l = len(number)
    for i in range(l - 2):
        for j in range(i + 1, l - 1):
            for k in range(j + 1, l):
                # print(number[i],number[j],number[k])
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer


from itertools import combinations


def solutionV2(number):
    answer = 0

    for case in list(combinations(number, 3)):
        if sum(case) == 0:
            answer += 1
    return answer
