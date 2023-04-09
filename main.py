from collections import Counter


def solution(array):
    answer = 0
    counter = Counter(array)
    if list(counter.values()).count(counter.most_common()[0][1]) > 1:
        return -1
    else:
        return counter.most_common()[0][0]
