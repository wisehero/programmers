def solution(land):
    indexes = list(range(4))
    answer = 0
    exclusive = 0
    for i in range(len(land)):
        maximum = 0
        if exclusive:
            land[i].pop(exclusive)
            maximum += max(land[i])
            answer += maximum
            exclusive = land[i].index(maximum)
            continue
        maximum = max(land[i])
        answer += maximum
        exclusive = land[i].index(maximum)
    return answer


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
