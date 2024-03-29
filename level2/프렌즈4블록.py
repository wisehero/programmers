import collections


def solution(m, n, board):
    answer = 0
    check_set = set()
    board = [list(i) for i in board]

    # 2x2 블록 조건에 맞으면 집합에 해당 인덱스를 추가하는 함수
    def check(b):
        for i in range(m - 1):
            for j in range(n - 1):
                if b[i][j] == b[i + 1][j] == b[i][j + 1] == b[i + 1][j + 1] != '0':
                    check_set.add((i, j))
                    check_set.add((i + 1, j))
                    check_set.add((i, j + 1))
                    check_set.add((i + 1, j + 1))

    # 격자를 재배열 하는 함수
    def arrange(b):
        for j in range(len(b[0])):
            q = collections.deque([])

            for i in range(len(b) - 1, -1, -1):
                if b[i][j] == '0':
                    q.append((i, j))
                else:
                    if q:
                        qi, qj = q.popleft()
                        b[qi][qj] = b[i][j]
                        b[i][j] = '0'
                        q.append((i, j))

    while True:
        check(board)
        if check_set:
            for i, j in check_set:
                board[i][j] = '0'
            answer += len(check_set)
            arrange(board)
            check_set.clear()
        else:
            break
    return answer


solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
