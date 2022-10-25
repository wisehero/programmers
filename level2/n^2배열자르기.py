def solution(n, left, right):
    answer = []
    matrix = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i].append(max(i, j) + 1)

    for i in range(n):
        answer += matrix[i]

    return answer[left:right + 1]


def solutionV2(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n
        b = i % n
        answer.append(max(a, b) + 1)
    return answer
