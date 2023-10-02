def solution(left, right):
    answer = 0
    arr = list(range(left, right + 1))

    for a in arr:
        count = 0
        for i in range(1, a + 1):
            if a % i == 0:
                count += 1

        if count % 2 == 0:
            answer += a
        else:
            answer -= a

    return answer
