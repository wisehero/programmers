def solution(k, m, score):
    answer = 0
    score.sort()
    score = score[::-1]
    box = []
    for i in range(len(score)):
        box.append(score[i])
        if len(box) == m:
            answer += min(box) * m
            box = []
    if len(box) < m:
        return answer


score = [1, 2, 3, 1, 2, 3, 1]
print(solution(3, 4, score))
