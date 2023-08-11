n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, 1002):
    dp[i] = dp[i - 2] * 2 + d[i - 1]

print(dp[n] % 10007)
