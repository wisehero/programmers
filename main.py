n = int(input())

if n < 100:
    print(n)
    exit()

answer = 99

for i in range(100, n + 1):
    k = str(i)
    m = int(k[len(k) // 2])
    a, b = int(k[0]), int(k[-1])

    if (a + b) / 2 == m:
        answer += 1

print(answer)
