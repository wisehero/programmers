from collections import deque


# bfs 트리 순회
def bfs1(root):
    visited = []
    if root is None:
        return 0
    q = deque()
    q.append(root)

    # 여기까지가 초기 세팅

    # 큐가 비워질때까지 순회
    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

# 그래프 순회 BFS
def bfs2(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited
