n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()

cnt = 0


def DFS(v):
    global cnt
    visited.add(v)
    for i in graph[v]:
        if i not in visited:
            cnt += 1
            DFS(i)

    return cnt


ans = DFS(1)
print(ans)
