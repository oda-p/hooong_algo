n, m = map(int, input().split(" "))
memories = list(map(int, input().split(" ")))
memories.insert(0, 0)
costs = list(map(int, input().split(" ")))
costs.insert(0, 0)

all_costs = sum(costs)
dp = [
    [0 for _ in range(all_costs + 1)] for _ in range(n + 1)
]  # 100(앱의 수) * 100(각 앱의 최대 비용)
for i in range(1, n + 1):
    for j in range(all_costs + 1):
        if j - costs[i] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i]] + memories[i])
        else:
            dp[i][j] = dp[i - 1][j]

answer = 0
for i in range(0, all_costs + 1):
    if dp[n][i] >= m:
        print(i)
        break
