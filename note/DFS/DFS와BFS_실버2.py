from collections import deque

n, m, v = map(int, input().split())

graph = [[] * (n + 1) for _ in range(n + 1)]
dfs_visit = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    dfs_visit.append(v)
    for i in sorted(graph[v]):
        if i not in dfs_visit:
            dfs(i)


def bfs(v):
    bfs_visit = [v]
    q = deque([v])
    while q:
        k = q.popleft()

        for i in sorted(graph[k]):
            if i not in bfs_visit:
                q.append(i)
                bfs_visit.append(i)
    print(*bfs_visit)


dfs(v)

print(*dfs_visit)
bfs(v)
