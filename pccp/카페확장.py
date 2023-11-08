def solution(menu, order, k):
    answer = 0

    d = {}
    for i, v in enumerate(menu):
        d[i] = v

    timeline = []
    end = 0
    for i, v in enumerate(order):
        enter = i * k
        if end < enter:
            end = enter + d[v]
        else:
            end += d[v]

        timeline.append([enter, 0])
        timeline.append([end, 1])

    val = 0
    timeline.sort(key=lambda x: x[0])

    for i in range(len(timeline)):

        if timeline[i][1] == 0:
            val += 1
        else:
            val -= 1

        answer = max(answer, val)

    return answer


solution([5, 12, 30], [1, 2, 0, 1], 10)
