def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        if str(num).count(str(k)):
            answer += 1
    return answer

print(solution(1,13,1))
