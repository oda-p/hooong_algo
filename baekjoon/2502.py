d, k = map(int, input().split(" "))

dp = [[0, 0] for _ in range(31)]
dp[1] = [1, 0]
dp[2] = [0, 1]
for i in range(3, d + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

for a in range(1, 100001):
    b = (k - (a * dp[d][0])) / dp[d][1]

    if b == int(b):
        print(a)
        print(int(b))
        break
