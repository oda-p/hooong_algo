t = int(input())
for _ in range(t):
    n = int(input())

    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    for i in range(1, 4):
        for j in range(1, n + 1):
            if j - i >= 0:
                dp[j] = max(dp[j], dp[j - i] + dp[j])

    print(dp[n])
