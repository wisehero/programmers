def solution(bin1, bin2):
    answer = ''
    a, b = int(bin1, 2), int(bin2, 2)
    c = a + b
    answer = bin(c)[2:]
    return answer
