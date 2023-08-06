import sys

n, m = map(int, sys.stdin.readline().split(" "))
matrixA = []
matrixB = []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    matrixA.append(tmp)

m, k = map(int, sys.stdin.readline().split())
for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    matrixB.append(tmp)

matrixC = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for z in range(m):
            matrixC[i][j] += matrixA[i][z] * matrixB[z][j]

for i in matrixC:
    for j in i:
        print(j, end=' ')
    print()
