t = int(input())

for _ in range(t):
    n = int(input())
    clothes = []
    for _ in range(n):
        a, b = input().split()
        clothes.append([a, b])
    d = {}

    for name, kind in clothes:
        if kind in d:
            d[kind] += 1
        else:
            d[kind] = 1

    ans = 1

    for key, value in d.items():
        ans *= (value + 1)

    print(ans - 1)
