a, b, c = map(int, input().split())
e, s, m = 1, 1, 1
year = 1

while True:
    if a == e and b == s and c == m:
        print(year)
        break

    e += 1
    s += 1
    m += 1

    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1

    year += 1
