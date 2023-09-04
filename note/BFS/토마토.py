from collections import deque

col, row = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(row)]
q = deque()

for i in range(row):
    for j in range(col):
        if box[i][j] == 1:
            q.append([i, j])

direction = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1]
]

while q:
    cur_row, cur_col = q.popleft()
    for i in range(4):
        next_row = cur_row + direction[i][0]
        next_col = cur_col + direction[i][1]

        if 0 <= next_row < row and 0 <= next_col < col:
            if box[next_row][next_col] == 0:
                box[next_row][next_col] = box[cur_row][cur_col] + 1
                q.append([next_row, next_col])

answer = 0
for line in box:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()

    answer = max(answer, max(line))

print(answer - 1)
