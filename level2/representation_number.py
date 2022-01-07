def solution(n):
    answer = 0
    numbers = [x for x in range(1, n + 1)]
    sum = 0
    start = 0
    i = 0
    while True:
        if sum > n:
            start += 1
            i = start
            sum = 0
            continue
        if numbers[start] == n:
            answer += 1
            break;
        sum += numbers[i]
        if sum == n:
            answer += 1
            start += 1
            sum = 0
            i = start
        i += 1
    return answer
