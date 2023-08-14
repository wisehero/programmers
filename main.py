from collections import deque

n, m = map(int, input().split(" "))
graph = []

for _ in range(n):
    graph.append(list(input()))

visited = [[False] * m for _ in range(n)]
direction = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]


def bfs(x, y):
    global answer
    visited[x][y] = True
    queue = deque()
    queue.append([x, y])

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + direction[i][0]
            next_y = cur_y + direction[i][1]
            if 0 <= next_x < n and 0 <= next_y < m:
                if graph[next_x][next_y] == "P" and not visited[next_x][next_y]:
                    answer += 1
                    visited[next_x][next_y] = True
                    queue.append([next_x, next_y])
                if graph[next_x][next_y] == "O" and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append([next_x, next_y])


answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            bfs(i, j)
if answer >= 1:
    print(answer)
else:
    print("TT")
