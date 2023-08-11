n = int(input())

blue = 0
white = 0

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split(" "))))


def solution(x, y, n):
    global blue, white
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                solution(x, y + n // 2, n // 2)
                solution(x + n // 2, y, n // 2)
                solution(x, y, n // 2)
                solution(x + n // 2, y + n // 2, n // 2)
                return # 위 처럼 다 나눠서 solution 함수 호출 후 함수를 종료해야함

    if color == 0:
        white += 1
    else:
        blue += 1


solution(0, 0, n)
print(white)
print(blue)
