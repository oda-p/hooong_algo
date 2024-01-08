import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

adj_list = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split(" "))
    adj_list[a].append(b)
    adj_list[b].append(a)

dp = [[0 for _ in range(2)] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]


def dfs(parent):
    global dp, visited

    # 0 : 얼리어답터, 1 : 일반
    visited[parent] = True
    dp[parent][0] = 1
    dp[parent][1] = 0
    for child in adj_list[parent]:
        if visited[child]:
            continue

        dfs(child)
        dp[parent][1] += dp[child][0]
        dp[parent][0] += min(dp[child][0], dp[child][1])


dfs(1)
print(min(dp[1]))
