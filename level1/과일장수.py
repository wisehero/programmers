def solution(k, m, score):
    answer = 0
    score.sort()
    box = []
    while score:
        box.append(score.pop())
        if len(box) == m:
            answer += min(box) * m
            box = []

    return answer
