from collections import deque

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    maps = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        maps[b][a] = 1

    visited = [[False] * m for _ in range(n)]


    def bfs(y ,x):
        q = deque()
        q.append([y, x])
        visited[y][x] = True
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while q:
            cur_y, cur_x = q.popleft()
            for i in range(4):
                next_x = cur_x + direction[i][0]
                next_y = cur_y + direction[i][1]

                if 0 <= next_x < m and 0 <= next_y < n and not visited[next_y][next_x] and maps[next_y][next_x] == 1:
                    visited[next_y][next_x] = True
                    q.append([next_y, next_x])

        return 1


    ans = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and not visited[i][j]:
                ans += bfs(i, j)
    print(visited)
    print(ans)
