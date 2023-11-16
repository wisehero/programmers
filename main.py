from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for case in list(combinations(arr, 3)):
    amount = sum(case)
    if amount <= m:
        ans = max(ans, amount)

print(ans)
