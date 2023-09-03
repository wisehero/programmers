def roundV2(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(input())

if n == 0:
    print(0)
    exit()
else:
    li = []
    for _ in range(n):
        li.append(int(input()))
    li.sort()
    t = roundV2(n * 0.15)
    print(roundV2(sum(li[t:len(li) - t]) / len(li[t:len(li) - t])))
