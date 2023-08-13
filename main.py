import math

n, m = map(int, input().split(" "))

maximum = n * m
result = 0
while True:
    if math.ceil(maximum / n) == m:
        result = maximum
        maximum -= 1
    else:
        break

print(result)
