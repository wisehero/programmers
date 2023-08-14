from collections import deque

n, m = map(int, input().split(" "))
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split(" "))))

visited = [[False] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]
direction = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]


def bfs(x, y):
    visited[x][y] = True
    distance[x][y] = 0
    queue = deque()
    queue.append([x, y, 0])

    while queue:
        cur_x, cur_y, now_position = queue.popleft()
        for i in range(4):
            next_x = cur_x + direction[i][0]
            next_y = cur_y + direction[i][1]
            if 0 <= next_x < n and 0 <= next_y < m:
                if graph[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    distance[next_x][next_y] = now_position + 1
                    queue.append([next_x, next_y, distance[next_x][next_y]])


for i in range(n):
    for j in range(m):
        # 출발 지점인 경우 bfs 호출
        if graph[i][j] == 2:
            bfs(i, j)
        # 갈 수 있지만 방문되지 않은 경우
        if graph[i][j] == 1 and not visited[i][j]:
            distance[i][j] = -1

for i in range(len(distance)):
    for j in range(len(distance[0])):
        print(distance[i][j], end=' ')
    print()
