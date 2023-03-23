n = int(input())
m = list(map(int, input().split()))
i = 0
n = 2
while True:
    for i in range(len(m)):
        if n % 2 != m[i]:
            n += 1
            break

        if i == len(m) - 1:
            print(n)

