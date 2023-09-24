from collections import deque


def solution(arr):
    answer = []

    q = deque(arr)

    while q:
        if not answer:
            answer.append(q.popleft())
        else:
            c = q.popleft()
            if c == answer[-1]:
                continue
            else:
                answer.append(c)

    return answer
