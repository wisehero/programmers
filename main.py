from collections import Counter


def solution(array):
    answer = 0

    if len(array) == 1:
        return array[0]

    counter = Counter(array)

    c_list = counter.most_common(2)

    if len(c_list) >= 2 and c_list[0][1] == c_list[1][1]:
        return -1

    return c_list[0][0]



