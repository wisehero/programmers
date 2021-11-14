def solution(n):
    answer = []
    answer = list(str(n))
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    answer.reverse()
    return answer

print(solution(12345))
