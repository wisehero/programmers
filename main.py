def solution(n):
    answer = 0

    dp = [0] * 101
    dp[1] = 1
    dp[2] = 2

    for i in range(3, 101):
        dp[i] = dp[i - 1] + 1

        while dp[i] % 3 == 0 or str(dp[i]).count("3"):
            dp[i] += 1

    answer = dp[n]

    return answer


solution(15)
