def solution(s):
    a = len(s)
    m = a // 2
    if a % 2 == 0:
        return s[m - 1: m + 1]
    else:
        return s[m]
