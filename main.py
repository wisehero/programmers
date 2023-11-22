from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))
    q = []
    for i in range(len(arr)):
        q.append([i, arr[i]])

    q = deque(q)

    priority = sorted(arr)

    cnt = 0
    while q:
        p = q.popleft()
        if p[1] == priority[-1]:
            priority.pop()
            cnt += 1
            if p[0] == m:
                print(cnt)
                break
        else:
            q.append(p)
