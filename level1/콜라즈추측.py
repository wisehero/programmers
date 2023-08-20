def solution(num):
    answer = 0
    target = num
    while True:
        if target == 1:
            break;
        if target % 2 == 0:
            target //= 2
            answer += 1
        else:
            target = target * 3 + 1
            answer += 1
        if answer == 500:
            return -1
    return answer

print(solution(6))