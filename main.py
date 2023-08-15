def solution(keyinput, board):
    answer = []
    now = [0, 0]

    for ki in keyinput:
        if ki == "left" and -(board[0] // 2) <= now[0] - 1 <= board[0] // 2:
            now[0] -= 1
        elif ki == "right" and -(board[0] // 2) <= now[0] + 1 <= board[0] // 2:
            now[0] += 1
        elif ki == "up" and -(board[1] // 2) <= now[1] + 1 <= board[1] // 2:
            now[1] += 1
        elif ki == "down" and -(board[1] // 2) <= now[1] - 1 <= board[1] // 2:
            now[1] -= 1

    answer = now
    return answer


solution(["down", "down", "down", "down", "down"], [7, 9])
