n = input()
li = []
answer = 1
zero, one = [], []
tmp = ""
for i, v in enumerate(list(n)):
    if tmp != "" and tmp[-1] != v:
        if tmp[-1] == "1":
            one.append(tmp)
            tmp = ""
        else:
            zero.append(tmp)
            tmp = ""
    tmp += v
    if i == len(list(n)) - 1:
        if tmp[-1] == "1":
            one.append(tmp)
        else:
            zero.append(tmp)


answer = min(len(zero), len(one))
print(answer)
