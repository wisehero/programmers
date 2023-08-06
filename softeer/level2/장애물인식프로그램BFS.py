import sys
from collections import deque

n = int(sys.stdin.readline())
blockMap = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
direction = [
    [0, 1],  # 상
    [0, -1],  # 하
    [-1, 0],  # 좌
    [1, 0]  # 우
]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    count = 1

    while q:
        row, col = q.popleft()
        for i in range(4):
            next_row = row + direction[i][1]
            next_col = col + direction[i][0]
            if (0 <= next_row < n and 0 <= next_col < n) and blockMap[next_row][next_col] == 1 and not visited[next_row][next_col]:
                q.append([next_row, next_col])
                visited[next_row][next_col] = True
                count += 1

    return count


result = []
for i in range(n):
    for j in range(n):
        if blockMap[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])
