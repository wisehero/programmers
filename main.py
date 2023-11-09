from collections import Counter

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

c = Counter(arr)
c = list(c.items())
c.sort(key=lambda x: (-x[1], x[0]))
print(c[0][0])
