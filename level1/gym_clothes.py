def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    for i in range(len(reserve)):
        if reserve[i] in lost:
            lost.remove(reserve[i])
            reserve[i] = ' '
    for i in range(len(lost)):
        if lost[i] == 1:
            if lost[i] + 1 in reserve:
                reserve.remove(lost[i] + 1)
                continue
            else:
                answer -= 1
                continue
        if lost[i] == n:
            if lost[i] - 1 in reserve:
                reserve.remove(lost[i] - 1)
                continue
            else:
                answer -= 1
                continue
        if lost[i] + 1 in reserve or lost[i] - 1 in reserve:
            if lost[i] - 1 in reserve:
                reserve.remove(lost[i] - 1)
                continue
            reserve.remove(lost[i] + 1)
        else:
            answer -= 1
    return answer
