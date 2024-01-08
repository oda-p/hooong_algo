n = int(input())

times = []
prices = []
for _ in range(n):
    time, price = map(int, input().split(" "))
    times.append(time)
    prices.append(price)
times = times[::-1]
prices = prices[::-1]

dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    if i - times[i - 1] >= 0:
        dp[i] = max(dp[i - 1], dp[i - times[i - 1]] + prices[i - 1])

print(dp[n])
