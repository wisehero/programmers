from collections import deque

n, k = map(int, input().split())

arr = [x for x in range(1, n + 1)]
ans = []
arr = deque(arr)

i = 1
while arr:
    e = arr.popleft()
    if i % k == 0:
        ans.append(e)
    else:
        arr.append(e)
    i += 1

answer = '<'
for i in range(len(ans)):
    if i == len(ans) - 1:
        answer += str(ans[i]) + ">"
    else:
        answer += str(ans[i]) + ", "

print(answer)
