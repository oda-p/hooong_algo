n, d = map(int, input().split(" "))

fast_paths = {}  # 도착점: [시작점, 거리]
for _ in range(n):
    s, e, c = map(int, input().split(" "))

    if e in fast_paths:
        fast_paths[e].append([s, c])
    else:
        fast_paths[e] = [[s, c]]

dp = [0 for i in range(d + 1)]
for i in range(1, d + 1):
    dp[i] = dp[i - 1] + 1
    if i in fast_paths:
        for start, cost in fast_paths[i]:
            dp[i] = min(dp[i], dp[start] + cost)

print(dp[d])
