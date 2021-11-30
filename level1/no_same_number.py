def solution(arr):
    answer = []
    n = 0
    for i in range(len(arr)):
        if i != 0:
            if arr[i] == answer[n]:
                continue
            answer.append(arr[i])
            n += 1
        else:
            answer.append(arr[i])
    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
