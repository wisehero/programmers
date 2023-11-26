from collections import Counter
from math import ceil

arr = [0] * 10
n = input()

for i in n:
    arr[int(i)] += 1

k = ceil((arr[6] + arr[9]) / 2)
arr[6] = k
arr[9] = k

print(max(arr))
