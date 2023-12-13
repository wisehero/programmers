def solution(board, h, w):
    answer = 0
    n = len(board)

    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    color = board[h][w]

    for i in range(4):
        next_h = h + direction[i][0]
        next_w = w + direction[i][1]

        if 0 <= next_h < n and 0 <= next_w < n:
            if board[next_h][next_w] == color:
                answer += 1
    return answer
