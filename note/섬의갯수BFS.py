from collections import deque


def numIslands(graph):
    number_of_islands = 0
    m = len(graph)
    n = len(graph[0])
    visited = [[False] * n for _ in range(m)]
    direction = [
        [0, 1],
        [0, -1],
        [-1, 0],
        [1, 0]
    ]

    def bfs(x, y):
        visited[x][y] = True
        queue = deque([x, y])
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + direction[i][0]
                next_y = cur_y + direction[i][1]
                if 0 <= next_x < m and 0 <= next_y < n:
                    if graph[i][j] == "1" and not visited[i][j]:
                        visited[next_x][next_y] = True
                        queue.append([next_x, next_y])

    for i in range(m):
        for j in range(n):
            if graph[i][j] == "1" and not visited[i][j]:
                bfs(i, j)

    return number_of_islands
