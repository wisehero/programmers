n = int(input())
m = int(input())
s = input()

dp = [0]
for i in range(1, n + 1):
    if i == 1:
        dp.append("IOI")
    else:
        dp.append(dp[i-1] + "OI")

pn = dp[n]
len_pn = len(pn)
result = 0
for i in range(len(s)):
    if s[i:i + len_pn] == pn:
        result += 1

print(result)
