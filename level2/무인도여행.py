from collections import deque


def bfs(x, y, maps):
    total = 0
    row = len(maps)
    col = len(maps[0])
    direction = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ]

    q = deque()
    q.append([x, y])
    total += int(maps[x][y])
    maps[x][y] = "X"
    while q:
        cur_row, cur_col = q.popleft()

        for i in range(4):
            next_row = cur_row + direction[i][0]
            next_col = cur_col + direction[i][1]

            if 0 <= next_col < col and 0 <= next_row < row and maps[next_row][next_col] != 'X':
                total += int(maps[next_row][next_col])
                maps[next_row][next_col] = "X"
                q.append([next_row, next_col])
    return total


def solution(maps):
    answer = []
    graph = []
    for i in range(len(maps)):
        graph.append(list(maps[i]))

    print(graph)

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] != "X":
                answer.append(bfs(i, j, graph))

    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
