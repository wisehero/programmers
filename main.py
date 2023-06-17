def solution(n):
    piece = 6
    while True:
        if piece // n >= 1 and piece % n == 0:
            return piece // 6
        else:
            piece += 6


