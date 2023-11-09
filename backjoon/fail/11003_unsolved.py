from collections import deque

n, l = map(int, input().split())
q = deque()

now = list(map(int, input().split()))

for i in range(n):
    # q에 원소가 있고 q의 마지막 원소가 현재의 원소보다 크면
    while q and q[-1][0] > now[i]:
        q.pop()
    q.append((now[i], i))

    # 슬라이딩 윈도우가 i - L 보다 크면 맨 왼쪽 제거
    if q[0][1] <= i - l:
        q.popleft()

    print(q[0][0], end=' ')

