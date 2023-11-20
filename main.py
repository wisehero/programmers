n = int(input())
numbers = list(map(int, input().split()))
d = {}
for num in numbers:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
ans = []
m = int(input())
m_arr = list(map(int, input().split()))
for a in m_arr:
    if a in d:
        ans.append(d[a])
    else:
        ans.append(0)

print(*ans)