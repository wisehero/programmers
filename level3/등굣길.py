def solution(m, n, puddles):
    puddles = [[q, p] for [p, q] in puddles]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if row == 1 and col == 1:
                continue

            if [row, col] in puddles:
                dp[row][col] = 0
            else:
                dp[row][col] = (dp[row - 1][col] + dp[row][col - 1]) % 1000000007

    return dp[n][m]