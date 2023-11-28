t = int(input())

arr = []
for _ in range(t):
    arr.append(int(input()))

arr.sort(reverse=True)

for a in arr:
    print(a)
