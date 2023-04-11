def solution(board):
    answer = 0
    N = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    z = []

    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:
                z.append((x, y))

    for x, y in z:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1

    for b in board:
        answer += b.count(0)

    return answer


solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])
