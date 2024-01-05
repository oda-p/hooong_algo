import sys

n = int(input())

dp = [[sys.maxsize for _ in range(n + 1)] for _ in range(2)]
dp[0][0] = 0
dp[1][0] = 0

if n >= 2:
    dp[0][2] = 1

if n >= 5:
    dp[1][5] = 1

for i in range(1, n + 1):
    if i - 2 >= 0:
        dp[0][i] = min(dp[0][i - 2] + 1, dp[1][i - 2] + 1)
    if i - 5 >= 0:
        dp[1][i] = min(dp[0][i - 5] + 1, dp[1][i - 5] + 1)

answer = min(dp[0][n], dp[1][n])
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
