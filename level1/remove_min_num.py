def solution(arr):
    answer = []
    if len(arr) == 1:
        return answer + [-1]
    arr.remove(min(arr))
    answer += arr
    return answer

