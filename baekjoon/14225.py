n = int(input())
arr = list(map(int, input().split(" ")))
visited = [False for _ in range(2000001)]


def dfs(i, cur_sum):
    visited[cur_sum] = True

    if i == n:
        return 0

    cur_num = arr[i]

    dfs(i + 1, cur_sum)
    dfs(i + 1, cur_sum + cur_num)


dfs(0, 0)

for i in range(1, 2000001):
    if not visited[i]:
        print(i)
        break
