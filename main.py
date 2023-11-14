def solution(wallpaper):
    answer = []
    a, b, c, d = 51, 51, 0, 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                a = min(i, a)
                b = min(j, b)
                c = max(i + 1, c)
                d = max(j + 1, d)

    answer = [a, b, c, d]
    return answer
