t = int(input())

for i in range(1, t + 1):
    ans = 0
    n = int(input())
    for k in range(1, n + 1):
        if k % 2 == 0:
            ans -= k
        else:
            ans += k

    print(f"#{i} {ans}")
