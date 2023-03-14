import heapq


def solution(N, coffee_times):
    if N == 1:
        return [x for x in range(1, len(coffee_times) + 1)]
    answer = []
    q = []
    stand = 0
    second = 0
    while True:
        while 0 in q:
            q.remove(0)

        if len(q) < N and stand <= len(coffee_times) - 1:
            if stand >= N:
                heapq.heappush(q, (stand, coffee_times[stand] + second))
                stand += 1
                continue
            else:
                heapq.heappush(q, (stand, coffee_times[stand]))
                stand += 1
                continue
        second += 1
        for i in range(len(q)):
            if q[i][1] == second:
                answer.append(q[i][0] + 1)
                q[i] = 0
        if len(coffee_times) == len(answer):
            break
    return answer


solution(3, [4, 2, 2, 5, 3])
