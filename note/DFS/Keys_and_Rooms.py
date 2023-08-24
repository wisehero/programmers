rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]


def canVisitAllRooms(rooms):
    visited = set()

    def dfs(v):
        visited.add(v)
        for next_v in rooms[v]:
            if next_v not in visited:
                dfs(next_v)

    dfs(0)

    if len(visited) == len(rooms):
        return True
    else:
        return False
