n = list(map(int, input().split(" ")))

maxnum = max(n)
minnum = min(n)
asc = 0
desc = 0

for i in range(len(n) - 1):
    if n[i] < n[i + 1]:
        asc += 1
    elif n[i] > n[i + 1]:
        desc += 1

if asc > 0 and desc == 0:
    print("ascending")
elif desc > 0 and asc == 0:
    print("descending")
else:
    print("mixed")







