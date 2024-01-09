n = int(input())
arr = list(map(int, input().split(" ")))

dp = [0 for _ in range(n)]
dp[n - 1] = arr[n - 1]
for i in range(n - 2, -1, -1):
    dp[i] = max(arr[i], dp[i + 1] + arr[i])

print(max(dp))
