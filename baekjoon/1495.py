n, s, m = map(int, input().split(" "))
volumes = list(map(int, input().split(" ")))

dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][s] = True

for i in range(1, n + 1):
    for j in range(m + 1):
        if not dp[i - 1][j]:
            continue

        if j + volumes[i - 1] <= m:
            dp[i][j + volumes[i - 1]] = True

        if j - volumes[i - 1] >= 0:
            dp[i][j - volumes[i - 1]] = True

max_vol = -1
for i in range(m, -1, -1):
    if dp[n][i]:
        max_vol = i
        break
print(max_vol)
