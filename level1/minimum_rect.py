def solution(sizes):
    answer = 0
    width = []
    height = []
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
    for i in sizes:
        width.append(i[0])
        height.append(i[1])
    answer = max(width) * max(height)
    return answer


sizes = [
    [60, 50],
    [30, 70],
    [60, 30],
    [80, 40]
]

solution(sizes)
