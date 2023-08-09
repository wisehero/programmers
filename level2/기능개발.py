from collections import deque


def solution(progresses, speeds):
    answer = []

    ps = []

    for p, s in zip(progresses, speeds):
        ps.append([p, s])
    progresses = deque(ps)

    count = 0
    while progresses:
        for i in range(len(progresses)):
            progresses[i][0] += progresses[i][1]

        while progresses and progresses[0][0] >= 100:
            count += 1
            progresses.popleft()
        if count >= 1:
            answer.append(count)
            count = 0

    return answer