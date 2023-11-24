num = [0] * 10001

for i in range(1, 10000):
    n = i

    for j in str(i):
        n += int(j)

    if n < len(num):
        num[n] += 1

for i in range(1, 10001):
    if num[i] == 0:
        print(i)
