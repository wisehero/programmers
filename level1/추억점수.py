def solution(name, yearning, photo):
    answer = []

    d = {}
    for i in range(len(name)):
        d[name[i]] = yearning[i]

    for p in photo:
        point = 0
        for i in range(len(p)):
            if p[i] in d:
                point += d[p[i]]
        answer.append(point)

    return answer
