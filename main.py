li = []
for i in range(8):
    score = int(input())
    li.append([i + 1, score])

li.sort(key=lambda x: (x[1], x[0]))

result = []
s = 0
for i, score in li[-5:]:
    s += score
    result.append(i)

result.sort()
print(s)
for r in result:
    print(r, end=' ')
