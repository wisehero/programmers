def solution(x):
    answer = True
    str_x = str(x)
    n = 0

    for s in str_x:
        n += int(s)

    if x % n != 0:
        answer = False
    return answer