n = int(input())

arr = []

for _ in range(n):
    w, h = map(int, input().split())
    arr.append([w, h])

ans = []
for i in range(len(arr)):
    w1, h1 = arr[i][0], arr[i][1]
    rank = 1
    for j in range(len(arr)):
        if i == j:
            continue
        w2, h2 = arr[j][0], arr[j][1]
        if w1 < w2 and h1 < h2:
            rank += 1
    ans.append(rank)

print(*ans)
