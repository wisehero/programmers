def solution(n, t, m, p):
    answer = ''
    numbers = ''
    for number in range(t * m):
        if n == 16:
            numbers += hex(number)[2:]
        else:
            numbers += decimalToN(number, n)
    answer += numbers[p - 1::m]
    return answer


def decimalToN(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]


print(solution(2, 4, 2, 1))
