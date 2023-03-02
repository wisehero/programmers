def solution(wallpaper):
    answer = []
    top, bottom, left, right = 0, 0, 0, 0
    for i in range(len(wallpaper)):
        if wallpaper[i] == -1:
            continue
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                if top == 0 and left == 0 and right == 0 and bottom == 0:
                    top = i
                    bottom = i + 1
                    right = j + 1
                    left = j
                else:
                    bottom = max(bottom, i + 1)
                    left = min(left, j)
                    right = max(right, j + 1)
    answer.append(top)
    answer.append(left)
    answer.append(bottom)
    answer.append(right)

    return answer
