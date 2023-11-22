from collections import deque

n, m = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(input()))

visited = [[False] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]


def bfs(row, col):
    visited[row][col] = True

    q = deque()
    cnt = 1
    distance[row][col] = cnt
    q.append([row, col, cnt])
    direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while q:
        cur_row, cur_col, cnt = q.popleft()

        for i in range(4):
            next_row = cur_row + direction[i][0]
            next_col = cur_col + direction[i][1]

            if 0 <= next_row < n and 0 <= next_col < m and maps[next_row][next_col] == "1":
                if not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    q.append([next_row, next_col, cnt + 1])
                    distance[next_row][next_col] = cnt + 1


for i in range(n):
    for j in range(m):
        if maps[i][j] == "1" and not visited[i][j]:
            bfs(i, j)
print(distance[n-1][m-1])
