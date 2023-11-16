n = int(input())

for i in range(1, n + 1):
    s = str(i)
    a = i

    for j in range(len(s)):
        a += int(s[j])

    if a == n:
        print(i)
        break

print(0)
