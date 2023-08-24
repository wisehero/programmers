def solution(n, m, section):
    answer = 0
    painted = 0

    for s in section:
        if s > painted:
            painted = s + m - 1
            answer += 1

    return answer
