def solution(arr):
    m = max(arr)
    i = 1

    while True:
        flag = True
        n = m * i
        for a in arr:
            if n % a != 0:
                flag = False

        if flag:
            return n
        else:
            i += 1
