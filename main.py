from collections import Counter


def solution(array):
    counter = Counter(array)
    frequent = max(counter.values())
    c = 0
    for i in set(array):
        if counter[i] == frequent:
            c += 1

    if c > 1:
        return -1
    else:
        return counter.most_common()[0][0]
