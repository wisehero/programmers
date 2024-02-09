def solution(s):
    s = list(s)
    n = 0
    for i in s:
        if i == "(":
            n += 1
        else:
            n -= 1
            if n < 0:
                return False

    if n > 0:
        return False

    return True
