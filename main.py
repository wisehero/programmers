from collections import deque

n, k = map(int, input().split())
arr = list(range(1, n + 1))
arr = deque(arr)
ans = []
i = 1
while arr:
    if i % k == 0:
        ans.append(arr.popleft())
    else:
        arr.append(arr.popleft())
    i += 1

s = '<'

for i, v in enumerate(ans):
    if i != len(ans) - 1:
        s += str(v) + ", "
    else:
        s += str(v) + ">"
print(s)
