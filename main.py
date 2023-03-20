li = []
answer = 0
for i in range(8):
    s = input()
    li.append(list(s))
for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0 and li[i][j] == "F":
                answer += 1
        elif i % 2 != 0:
            if j % 2 != 0 and li[i][j] == "F":
                answer += 1

print(answer)
