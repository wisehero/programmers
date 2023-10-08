def solution(park, routes):
    answer = []
    obs = []

    start = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                start.append(i)
                start.append(j)
            elif park[i][j] == "X":
                obs.append([i, j])

    for r in routes:
        d, m = r.split(" ")
        m = int(m)

        if d == "N" and 0 <= start[0] - m < len(park):
            origin = start[0]
            for i in range(m):
                start[0] -= 1
                if start in obs:
                    start[0] = origin
                    break
        elif d == "S" and 0 <= start[0] + m < len(park):
            origin = start[0]
            for i in range(m):
                start[0] += 1
                if start in obs:
                    start[0] = origin
                    break
        elif d == "E" and 0 <= start[1] + m < len(park[0]):
            origin = start[1]
            for i in range(m):
                start[1] += 1
                if start in obs:
                    start[1] = origin
                    break
        elif d == "W" and 0 <= start[1] - m < len(park[0]):
            origin = start[1]
            for i in range(m):
                start[1] -= 1
                if start in obs:
                    start[1] = origin
                    break

    answer = start

    return answer

solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"])