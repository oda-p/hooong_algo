n = int(input())
hearts = list(map(int, input().split(" ")))
pleasures = list(map(int, input().split(" ")))

dp = [[0 for _ in range(100)] for _ in range(n + 1)]

max_pleasure = 0
for i in range(1, n + 1):
    for j in range(100):
        if j - hearts[i - 1] < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(
                dp[i - 1][j - hearts[i - 1]] + pleasures[i - 1], dp[i - 1][j]
            )
        max_pleasure = max(max_pleasure, dp[i][j])

print(max_pleasure)
