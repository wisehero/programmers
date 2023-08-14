n, m = map(int, input().split(" "))
mA = []
mB = []

row = max(n, m)

for _ in range(row):
    mA.append(list(map(int, input().split(" "))))
for _ in range(row):
    mB.append(list(map(int, input().split(" "))))

for i in range(n):
    for j in range(m):
        mA[i][j] += mB[i][j]
        print(mA[i][j], end=' ')
    print()
