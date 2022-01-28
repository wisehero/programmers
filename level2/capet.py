import math


def issquare(n):
    temp = n ** 0.5

    if int(temp) == temp:
        return True
    else:
        return False


def solution(brown, yellow):
    answer = []
    if issquare(brown + yellow):
        answer.append(math.sqrt(brown + yellow))
        answer.append(math.sqrt(brown + yellow))
        return answer

    sum = brown + yellow

    result = []

    for i in range(1, sum // 2 + 1):
        if sum % i == 0:
            if (i - 2) * ((sum // i) - 2) == yellow:
                answer.append(i)
                answer.append(sum // i)
                break;

    answer.sort(reverse=True)
    return answer


print(solution(50, 22))


