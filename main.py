d_x = {}
d_y = {}
for _ in range(3):
    x, y = map(int, input().split())
    if x in d_x:
        d_x[x] += 1
    else:
        d_x[x] = 1

    if y in d_y:
        d_y[y] += 1
    else:
        d_y[y] = 1

ans = []
for key in d_x.keys():
    if d_x[key] == 1:
        ans.append(key)

for key in d_y.keys():
    if d_y[key] == 1:
        ans.append(key)

print(*ans)