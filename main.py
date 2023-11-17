n = int(input())

room = 1
ans = 1
while room < n:
    room += 6 * ans
    ans += 1

print(ans)
