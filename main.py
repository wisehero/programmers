def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i] == True:
            for k in range(arr[i] * 2):
                answer.append(arr[i])
        else:
            if len(answer) != 0:
                for j in range(arr[i]):
                    answer.pop()
    return answer