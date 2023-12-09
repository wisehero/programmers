from collections import deque

while True:
    row, col = map(int, input().split())

    if row == 0 and col == 0:
        break
    maps = []
    visited = [[False] * row for _ in range(col)]

    for _ in range(col):
        maps.append(list(input().split()))


    def bfs(y, x):
        visited[y][x] = True
        q = deque()
        q.append([y, x])
        direction = [
            [0, 1], [1, 0],
            [0, -1], [-1, 0],
            [-1, 1], [1, -1],
            [-1, -1], [1, 1]
        ]

        while q:
            cur_y, cur_x = q.popleft()

            for i in range(8):
                next_x = cur_x + direction[i][0]
                next_y = cur_y + direction[i][1]

                if 0 <= next_x < row and 0 <= next_y < col and not visited[next_y][next_x]:
                    if maps[next_y][next_x] == "1":
                        q.append([next_y, next_x])
                        visited[next_y][next_x] = True

        return 1


    ans = 0
    for i in range(col):
        for j in range(row):
            if maps[i][j] == "1" and not visited[i][j]:
                ans += bfs(i, j)

    print(ans)
