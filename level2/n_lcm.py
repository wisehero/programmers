def solution(arr):
    answer = 0
    arr.sort()
    i = 1
    while True:
        count = 0
        n = arr[-1] * i
        for k in arr:
            if n % k == 0:
                count += 1
        if count == len(arr):
            answer = n
            break
        i = i + 1
    return answer