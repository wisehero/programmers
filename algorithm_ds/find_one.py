def solution(L, x):
    answer = []
    count = 0
    for i in L:
        if i == x:
            answer.append(count)
        count += 1
    if len(answer) == 0:
        answer.append(-1)

    return answer
