n = int(input())

if n < 3:
    if n == 1:
        print("CY")
    elif n == 2:
        print("SK")
    exit()

dp = [-1 for _ in range(n + 1)]
dp[1] = 1
dp[2] = 2
dp[3] = 1

for i in range(3, n + 1):
    if dp[i - 1] == -1 and dp[i - 3] == -1:
        continue
    elif dp[i - 1] == -1:
        dp[i] = dp[i - 3] + 1
    elif dp[i - 3] == -1:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = min(dp[i - 1] + 1, dp[i - 3] + 1)

if dp[n] % 2 == 0:
    print("SK")
else:
    print("CY")

# n = int(input())
#
# cnt = 0
# while n % 3 != 0:
#     cnt += 1
#     n -= 1
#
# cnt += n // 3
#
# if cnt % 2 == 0:
#     print("SK")
# else:
#     print("CY")
