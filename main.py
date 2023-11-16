import math

n = int(input())

arr = list(map(int, input().split()))
answer = 0
for i in arr:
    f = True
    if i == 1:
        continue
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            f = False

    if f:
        answer += 1

print(answer)
