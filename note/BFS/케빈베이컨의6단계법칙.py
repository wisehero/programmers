from collections import defaultdict, deque

n, m = map(int, input().split())

dic = dict()
result = dict()
for i in range(1, n + 1):
    dic[i] = []

print(dic)
for _ in range(m):
    key, friend = map(int, input().split(" "))
    if friend not in dic[key] and key not in dic[friend]:
        dic[key].append(friend)
        dic[friend].append(key)


def bfs(start):
    visited = [start]
    count = 0
    point = 0
    q = deque()
    q.append([start, point])

    while q:
        cur_node, point = q.popleft()
        for v in dic[cur_node]:
            if v not in visited:
                count += point + 1
                visited.append(v)
                q.append([v, point + 1])
    return count


for key in dic.keys():
    result[key] = bfs(key)

r = sorted(result.items(), key=lambda x: (x[1], x[0]))
print(r[0][0])
