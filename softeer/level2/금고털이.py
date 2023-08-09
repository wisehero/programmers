import sys

result = 0
w, n = map(int, sys.stdin.readline().split(" "))

item = []
for _ in range(n):
    gram, price = map(int, sys.stdin.readline().split(" "))
    item.append([gram, price])


item.sort(key=lambda x:-x[1])

## w = 100
## gram = 140
for gram, price in item:
    if gram > w:
        result += w * price
        w -= w
    else:
        w -= gram
        result += gram * price

print(result)