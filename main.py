from itertools import product


def solution(n):
    answer = 0

    if n == 1:
        return 1

    for i in range(1, n + 1):
        li = list(product([1, 2], repeat=i))
        for l in li:
            if sum(l) == n:
                answer += 1
    return answer


print(solution(3))
