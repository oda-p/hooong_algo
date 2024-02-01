from sys import setrecursionlimit

setrecursionlimit(10**5)

n, m, r = map(int, input().split(" "))

adj_list = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split(" "))
    adj_list[s].append(e)
    adj_list[e].append(s)

for adj in adj_list:
    adj.sort(reverse=True)

visited = [0 for _ in range(n + 1)]
cnt = 1
visited[r] = 1


def dfs(cur):
    global visited, cnt

    if cnt == n + 1:
        return

    for next_node in adj_list[cur]:
        if not visited[next_node]:
            cnt += 1
            visited[next_node] = cnt
            dfs(next_node)


dfs(r)
for i in range(1, n + 1):
    print(visited[i])
