n, m = map(int, input().split())

a = set()

for _ in range(n):
    a.add(input())

ans = 0
for _ in range(m):
    b = input()
    if b in a:
        ans += 1

print(ans)
