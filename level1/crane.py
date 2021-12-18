board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1]
]

moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for k in range(len(board)):
            if board[k][i - 1] == 0:
                continue
            else:
                stack.append(board[k][i - 1])
                board[k][i - 1] = 0
                break

        if len(stack) >= 2:
            if stack[-2] == stack[-1]:
                stack.pop()
                stack.pop()
                answer += 2

    return answer


print(solution(board, moves))
