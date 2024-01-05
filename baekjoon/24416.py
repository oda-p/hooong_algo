n = int(input())

recursive_cnt = 0
dp_cnt = 0


def recur_fib(num):
    global recursive_cnt

    if num == 1 or num == 2:
        recursive_cnt += 1
        return 1
    return recur_fib(num - 1) + recur_fib(num - 2)


def dp_fib(num):
    global dp_cnt
    dp = [0 for _ in range(n + 1)]

    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp_cnt += 1
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[num]


recur_fib(n)
dp_fib(n)

print(recursive_cnt, dp_cnt)
