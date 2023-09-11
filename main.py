def solution(storey):
    answer = 0
    storey = list(map(int, str(storey)))

    while storey:
        s = storey.pop()

        if len(storey) == 0:
            if s > 5:
                answer += 10 - s + 1
            else:
                answer += s
            break

        if s > 5:
            answer += 10 - s
            storey[-1] += 1
        elif s < 5:
            answer += s
        else:
            if storey[-1] >= 5:
                answer += 5
                storey[-1] += 1
            else:
                answer += 5

    return answer

print(solution(16))
