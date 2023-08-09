from collections import deque


def solution(priorities, location):
    answer = 0

    pi = []
    count = 1
    for i, p in enumerate(priorities):
        pi.append([p, i])

    pi = deque(pi)
    while pi:
        p, i = pi.popleft()

        if p == max(priorities):
            if i == location:
                return count
            else:
                count += 1
            priorities.remove(max(priorities))
        else:
            pi.append([p, i])

    return answer