def solution(n):
    dp = [0] * 2001
    dp[0], dp[1], dp[2] = 0, 1, 2

    for i in range(3, 2001):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 1234567
