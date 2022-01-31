from itertools import combinations


# 내 풀이 -> 시간초과남
def solution(number, k):
    answer = list(combinations(list(number), len(number) - k))
    return ''.join(sorted(answer, reverse=True)[0])


def solutionV2(number, k):
    answer = []  # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])
