from itertools import combinations


def solution(nums):
    answer = 0

    for comb in list(combinations(nums, 3)):
        m = sum(comb)
        flag = True
        for i in range(2, m):
            if m % i == 0:
                flag = False

        if flag:
            answer += 1

    return answer
