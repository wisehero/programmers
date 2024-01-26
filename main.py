# A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
# 길이가 서로 같다면 A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저 온다.
# 사전 순으로 한다.
n = int(input())
arr = []

for _ in range(n):
    arr.append([input(), 0])

for i in range(len(arr)):
    s = 0
    for j in arr[i][0]:
        if j.isdigit():
            s += int(j)
    arr[i][1] = s
arr.sort(key=lambda x: (len(x[0]), x[1], x[0]))
for a in arr:
    print(a[0])
