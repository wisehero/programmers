def solution(x):
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    answer = solution(x - 1) + solution(x - 2)
    return answer
