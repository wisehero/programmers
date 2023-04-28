def solution(park, routes):
    answer = []
    park = list(map(list, park))
    print(park[0])
    start = []
    for row in range(len(park)):
        for col in range(len(park[row])):
            if park[row][col] == "S":
                start.append(row)
                start.append(col)
        if len(start) == 2:
            break

    print(start)

    for route in routes:
        direction, move = route.split(" ")
        move = int(move)
        possible = True
        if direction == "N" and start[0] - move >= 0:
            for i in range(start[0], start[0] - move - 1, -1):
                if park[i][start[1]] == "X":
                    possible = False
                    break

            if possible:
                park[start[0]][start[1]], park[i][start[1]] = park[i][start[1]], park[start[0]][start[1]]
                start[0] = i

        elif direction == "S" and start[0] + move <= len(park) - 1:
            for i in range(start[0] + 1, start[0] + move + 1):
                if park[i][start[1]] == "X":
                    possible = False
                    break
            if possible:
                park[start[0]][start[1]], park[i][start[1]] = park[i][start[1]], park[start[0]][start[1]]
                start[0] = i
        elif direction == "W" and start[1] - move >= 0:
            for i in range(start[1] - 1, start[1] - move - 1, -1):
                if park[start[0]][i] == "X":
                    possible = False
                    break
            if possible:
                park[start[0]][start[1]], park[start[0]][i] = park[start[0]][i], park[start[0]][start[1]]
                start[1] = i
        elif direction == "E" and start[1] + move <= len(park[0]) - 1:
            for i in range(start[1] + 1, start[1] + move + 1):
                if park[start[0]][i] == "X":
                    possible = False
                    break
            if possible:
                park[start[0]][start[1]], park[start[0]][i] = park[start[0]][i], park[start[0]][start[1]]
                start[1] = i

    return start


print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))
