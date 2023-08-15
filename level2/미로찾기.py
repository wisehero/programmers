from collections import deque


def bfs(start, end, maps):
    m = len(maps[0])  # x좌표
    n = len(maps)  # y좌표
    visited = [[False] * m for _ in range(n)]
    direction = [
        [0, 1],
        [0, -1],
        [-1, 0],
        [1, 0]
    ]
    flag = False

    q = deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                q.append([i, j, 0])
                visited[i][j] = True
                flag = True
                break
        if flag:
            break

    while q:
        cur_x, cur_y, now_position = q.popleft()

        if maps[cur_x][cur_y] == end:
            return now_position

        for i in range(4):
            next_x = cur_x + direction[i][0]
            next_y = cur_y + direction[i][1]

            if 0 <= next_x < n and 0 <= next_y < m:
                if maps[next_x][next_y] != "X" and not visited[next_x][next_y]:
                    q.append([next_x, next_y, now_position + 1])
                    visited[next_x][next_y] = True

    return -1


def solution(maps):
    path1 = bfs("S", "L", maps)
    path2 = bfs("L", "E", maps)

    if path1 != -1 and path2 != -1:
        return path1 + path2
    return -1


print(solution(["OOOOOL",
                "OXOXOO",
                "OOSXOX",
                "OXXXOX",
                "EOOOOX"]))
