def solution(t, p):
    answer = 0
    length = len(p)
    for i in range(len(t) - length + 1):
        if int(p) >= int(t[i:i + length]):
            answer += 1
    return answer
