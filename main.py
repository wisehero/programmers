from collections import deque

board = list(input())
m = len(board)

for i in range(m - 3):
    if "".join(board[i:i + 4]) == "XXXX":
        board[i] = "A"
        board[i + 1] = "A"
        board[i + 2] = "A"
        board[i + 3] = "A"

for i in range(m - 1):
    if "".join(board[i:i + 2]) == "XX":
        board[i] = "B"
        board[i + 1] = "B"

if "X" in board:
    print(-1)
else:
    print("".join(board))
