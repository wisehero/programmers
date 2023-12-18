t = int(input())

for i in range(1, t + 1):
    s = set()
    start = int(input())
    a = start
    while True:
        for e in str(start):
            s.add(e)

        if s == {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            break
        start += a
    print(f"#{i} {start}")
