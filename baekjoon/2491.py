n = int(input())
arr = list(map(int, input().split(" ")))

# 0 : 작아지는 경우
# 1 : 커지는 경우
dp = [[1 for _ in range(n)] for _ in range(2)]
for i in range(1, n):
    if arr[i - 1] == arr[i]:
        dp[0][i] = dp[0][i - 1] + 1
        dp[1][i] = dp[1][i - 1] + 1
    elif arr[i - 1] > arr[i]:
        dp[0][i] = dp[0][i - 1] + 1
    elif arr[i - 1] < arr[i]:
        dp[1][i] = dp[1][i - 1] + 1

print(max(max(dp[0]), max(dp[1])))
