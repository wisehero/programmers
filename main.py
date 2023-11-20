n, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr = arr[::-1]

i = 0
ans = 0
while k != 0:
    ans += k // arr[i]
    k %= arr[i]
    i += 1

print(ans)