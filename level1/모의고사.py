def solution(answers):
    points = [0, 0, 0]

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            points[0] += 1

        if answers[i] == two[i % len(two)]:
            points[1] += 1

        if answers[i] == three[i % len(three)]:
            points[2] += 1

    d = {}

    for i in range(len(points)):
        d[i + 1] = points[i]

    m = max(points)
    rank = []
    for k, v in d.items():
        if v == m:
            rank.append(k)

    return rank
