def solution(k, d):
    count = 0
    a = 0
    while a * k <= d:
        b_squared = d ** 2 - (a * k) ** 2
        if b_squared >= 0:
            b = int(b_squared ** 0.5 // k)
            count += b + 1
        a += 1
    return count
