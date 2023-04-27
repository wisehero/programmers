from collections import Counter


def solution(a, b, c, d):
    answer = 1
    li = [a, b, c, d]
    counter = Counter(li)

    keys = list(counter.keys())
    if len(keys) == 4:
        return min(keys)
    elif len(keys) == 3:
        for key in keys:
            if counter[key] == 1:
                answer *= key

    elif len(keys) == 2:
        if counter.most_common()[0][1] == 3:
            return (10 * counter.most_common()[0][0] + counter.most_common()[1][0]) ** 2
        else:
            return (keys[0] + keys[1]) * abs(keys[0] - keys[1])
    else:
        return 1111 * keys[0]

    return answer