def solution(a, b):
    answer = 0

    for a1, b1 in zip(a, b):
        answer += a1 * b1
    return answer
