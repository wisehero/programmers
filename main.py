n = int(input())

target_arr = []
arr = []
for _ in range(n):
    target_arr.append(int(input()))
target_arr = target_arr[::-1]
i = 0
ans = []

for i in range(1, n + 1):
    arr.append(i)
    ans.append("+")
    while arr and arr[-1] == target_arr[-1]:
        arr.pop()
        target_arr.pop()
        ans.append("-")

if len(arr) != 0:
    print("NO")
else:
    for a in ans:
        print(a)
