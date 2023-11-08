def solution(n):
    dp = [0] * 60_002
    dp[1] = 1
    dp[2] = 2

    if n == 1 or n == 2:
        return dp[n]

    for i in range(3, 60002):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000007
        if i == n:
            return dp[i]
