def solution(n):
    cnt_one = bin(n)[2:].count('1')
    for m in range(n+1, 1000001):
        if cnt_one == bin(m)[2:].count('1'):
            return m