n = int(input())
arr = list(map(int, input().split(" ")))

dp = [[0, 0] for _ in range(n)]
dp[n - 1] = [arr[n - 1], arr[n - 1]]
max_sum = min(arr)
for i in range(n - 2, -1, -1):
    dp[i][0] = max(arr[i], dp[i + 1][0] + arr[i])
    dp[i][1] = max(dp[i + 1][0], dp[i + 1][1] + arr[i])
    max_sum = max(max_sum, dp[i][0], dp[i][1])
print(max_sum)
