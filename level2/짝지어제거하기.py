from collections import deque


def solution(s):
    s = deque(list(s))
    arr = []

    while s:
        if arr:
            sp = s.popleft()
            if sp == arr[-1]:
                arr.pop()
            else:
                arr.append(sp)
        else:
            arr.append(s.popleft())

    if len(s) == 0 and len(arr) == 0:
        return 1
    else:
        return 0
