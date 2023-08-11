import sys

# 이거 DP임
n = int(sys.stdin.readline())
dp = [0] * 16
dp[0] = 2

for i in range(1, 16):
    dp[i] = dp[i-1] + 2 ** (i-1)

print(dp)

print(pow(dp[n], 2))