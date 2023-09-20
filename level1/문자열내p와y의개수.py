def solution(s):
    p = 0
    y = 0
    for st in s:
        if st == "p" or st == "P":
            p += 1

        if st == "Y" or st == "y":
            y += 1
    if p == y:
        return True
    else:
        return False
