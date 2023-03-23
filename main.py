number = []
for i in range(1, 46):
    number += [i] * i
a, b = map(int, input().split())
print(sum(number[a - 1:b]))
print(len(number))