def solution(sides):
    answer = 0

    for i in range(1, sides[0] + sides[1]):
        now = [] + sides
        now.append(i)
        now.sort()

        if now[0] + now[1] > now[-1]:
            answer += 1

    return answer


print(solution([3, 6]))
