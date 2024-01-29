from collections import deque

row, col = map(int, input().split())

arr = []
visited = [[False] * col for _ in range(row)]
for _ in range(row):
    arr.append(list(input()))


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        cur_row, cur_col = q.popleft()

        if arr[cur_row][cur_col] == "-":
            next_row, next_col = cur_row, cur_col + 1
            if next_col >= col or arr[next_row][next_col] != "-":
                break

            visited[next_row][next_col] = True
            q.append([next_row, next_col])

        else:
            next_row, next_col = cur_row + 1, cur_col

            if next_row >= row or arr[next_row][next_col] != "|":
                break

            visited[next_row][next_col] = True
            q.append([next_row, next_col])

    return 1


answer = 0
for i in range(row):
    for j in range(col):
        if not visited[i][j]:
            answer += bfs(i, j)

print(answer)
