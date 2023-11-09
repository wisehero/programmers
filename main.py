n = int(input())
m = [list(input()) for _ in range(n)]

w = 0
h = 0

for line in m:
    cnt = 0
    for i in range(len(line)):
        if line[i] == ".":
            cnt += 1
        else:
            if cnt >= 2:
                w += 1
            cnt = 0

    if cnt >= 2:
        w += 1

for i in range(len(m)):
    cnt = 0
    for j in range(len(m)):
        if m[j][i] == ".":
            cnt += 1
        else:
            if cnt >= 2:
                h += 1
            cnt = 0

    if cnt >= 2:
        h += 1




print(w, h)
