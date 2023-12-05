from collections import deque

n = int(input())
maps = []
for _ in range(n):
    maps.append(input())


def redgreen_bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            next_x = cur_x + direction[i][0]
            next_y = cur_y + direction[i][1]

            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
                if maps[next_x][next_y] in "RG":
                    visited[next_x][next_y] = True
                    q.append([next_x, next_y])

    return 1


def bfs(x, y, z):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            next_x = cur_x + direction[i][0]
            next_y = cur_y + direction[i][1]

            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
                if maps[next_x][next_y] == z:
                    visited[next_x][next_y] = True
                    q.append([next_x, next_y])
    return 1


weak = 0
non_weak = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (maps[i][j] == "R" or maps[i][j] == "G") and not visited[i][j]:
            weak += redgreen_bfs(i, j)
        if maps[i][j] == "B" and not visited[i][j]:
            weak += bfs(i, j, "B")

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if maps[i][j] == "R" and not visited[i][j]:
            non_weak += bfs(i, j, "R")
        elif maps[i][j] == "G" and not visited[i][j]:
            non_weak += bfs(i, j, "G")
        elif maps[i][j] == "B" and not visited[i][j]:
            non_weak += bfs(i, j, "B")

print(non_weak)
print(weak)
