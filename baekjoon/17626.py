import math
import sys

n = int(input())
dp = {1: 1}


def dfs(x):
    if x in dp:
        return dp[x]

    min_sqrt_num = int(math.sqrt(x))
    if x == min_sqrt_num**2:
        dp[x] = 1
    else:
        dp[x] = sys.maxsize
        for i in range(min_sqrt_num, min_sqrt_num // 2, -1):
            dp[x] = min(dp[x], dfs(i**2) + dfs(x - i**2))
    return dp[x]


print(dfs(n))
