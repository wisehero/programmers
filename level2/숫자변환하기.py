# 어떻게 풀어야하는지 생각이 안났다.
# dp를 이용해야한다.
def solution(x, y, n):
    if x == y:
        return 0

    dp = [float('inf')] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] == float('inf'):
            continue
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    if dp[y] == float('inf'):
        return -1
    else:
        return dp[y]


solution(10, 40, 5)
