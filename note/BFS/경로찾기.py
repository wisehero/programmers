from collections import deque

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]


def bfs(start, end, graph):
    visited = [start]
    q = deque()
    q.append(start)

    while q:
        cur_v = q.popleft()
        for next_v in range(len(graph[cur_v])):
            if graph[cur_v][next_v] == 1 and next_v == end:
                return 1
            if next_v not in visited and graph[cur_v][next_v] == 1:
                visited.append(next_v)
                q.append(next_v)

    return 0


result = []
for i in range(n):
    sub_result = []
    for j in range(n):
        sub_result.append(bfs(i, j, map))
    result.append(sub_result)

for i in range(len(result)):
    for j in range(len(result)):
        print(result[i][j], end=' ')
    print()
