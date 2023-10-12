def solution(sizes):
    answer = 0
    width = []
    height = []
    for size in sizes:
        if size[0] >= size[1]:
            width.append(size[0])
            height.append(size[1])
        else:
            height.append(size[0])
            width.append(size[1])

    return max(width) * max(height)
