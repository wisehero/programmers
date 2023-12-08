# 2667
from collections import deque

n = int(input())
maps = []
for _ in range(n):
    maps.append(input())
visited = [[False] * n for _ in range(n)]


def bfs(x, y):
    visited[x][y] = True
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = deque()
    q.append([x, y])
    cnt = 1

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            next_x = cur_x + direction[i][0]
            next_y = cur_y + direction[i][1]

            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y] and maps[next_x][next_y] == "1":
                q.append([next_x, next_y])
                visited[next_x][next_y] = True
                cnt += 1

    return cnt


ans = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == "1" and not visited[i][j]:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
for a in ans:
    print(a)
