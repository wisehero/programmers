from collections import deque


def solution(priorities, location):
    arr = []
    for i in range(len(priorities)):
        arr.append([i, priorities[i]])

    q = deque(arr)
    priorities.sort()
    priorities = priorities[::-1]
    cnt = 0

    while q:
        p = q.popleft()
        if p[1] == priorities[0]:
            cnt += 1
            priorities.pop(0)
            if p[0] == location:
                break
        else:
            q.append(p)

    return cnt
