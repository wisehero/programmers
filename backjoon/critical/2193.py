n = int(input())
dp = [0] * 91
dp[1] = 1
dp[2] = 1

if n == 1 or n == 2:
    print(1)
for i in range(3, 91):
    dp[i] = dp[i - 1] + dp[i - 2]
    if i == n:
        print(dp[i])
        break
