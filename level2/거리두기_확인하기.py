from collections import deque


def solution(places):
    answer = []

    def bfs(p):
        start = []

        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    start.append([i, j])

        for s in start:
            q = deque()
            q.append(s)
            visited = [[0] * 5 for _ in range(5)]
            distance = [[0] * 5 for _ in range(5)]
            visited[s[0]][s[1]] = 1

            while q:
                cur_row, cur_col = q.popleft()
                direction = [
                    [0, 1],
                    [1, 0],
                    [-1, 0],
                    [0, -1]
                ]

                for i in range(4):
                    next_row = cur_row + direction[i][0]
                    next_col = cur_col + direction[i][1]

                    if 5 > next_row >= 0 == visited[next_row][next_col] and 0 <= next_col < 5:
                        if p[next_row][next_col] == "O":
                            q.append([next_row, next_col])
                            visited[next_row][next_col] = 1
                            distance[next_row][next_col] = distance[cur_row][cur_col] + 1

                        if p[next_row][next_col] == 'P' and distance[cur_row][cur_col] < 2:
                            return 0

        return 1

    for place in places:
        answer.append(bfs(place))

    return answer
