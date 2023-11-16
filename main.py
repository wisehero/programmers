t = int(input())

for _ in range(t):
    s = input()
    score = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == "O":
            score += 1
            ans += score
        else:
            score = 0
    print(ans)
