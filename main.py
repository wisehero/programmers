def solution(x, n):
    answer = []

    num = x

    while n > 0:
        answer.append(num)
        num += x
        n -= 1
    return answer
