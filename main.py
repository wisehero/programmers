def solution(n):
    answer = []
    i = 2
    while True:
        if n % i == 0:
            n //= i
            answer.append(i)
        else:
            i += 1

        if n == 1:
            break
    return sorted(list(set(answer)))


print(solution(24))
