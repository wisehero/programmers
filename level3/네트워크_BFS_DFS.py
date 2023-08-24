def solution(n, computers):
    answer = 0

    def DFS(i):
        visited[i] = 1
        for a in range(n):
            if computers[i][a] and not visited[a]:
                DFS(a)

    visited = [0 for _ in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1

    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
