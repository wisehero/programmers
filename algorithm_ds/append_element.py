def solution(L, x):
    answer = []
    L.append(x)
    L.sort()
    for i in L:
        answer.append(i)
    return answer
