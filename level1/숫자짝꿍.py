from collections import deque, Counter


def solution(X, Y):
    answer = []
    c1 = Counter(X)
    c2 = Counter(Y)

    for key in c1.keys():
        if c1[key] != 0 and c2[key] != 0:
            answer += [key] * min(c1[key], c2[key])
    if len(answer) == 0:
        return "-1"
    if len(answer) == answer.count("0"):
        return "0"
    answer.sort(reverse=True)
    return "".join(answer)


solution("12321", "42531")
