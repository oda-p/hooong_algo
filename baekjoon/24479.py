import sys

sys.setrecursionlimit(10**5)

n, m, r = map(int, input().split(" "))

adj_list = [[] for _ in range(n + 1)]
for _ in range(m):
    node_1, node_2 = map(int, input().split(" "))
    adj_list[node_1].append(node_2)
    adj_list[node_2].append(node_1)


for adj in adj_list:
    adj.sort()

visited = [0 for _ in range(n + 1)]
visit_cnt = 1


def dfs(cur_node):
    global visit_cnt

    visited[cur_node] = visit_cnt
    visit_cnt += 1

    for next_node in adj_list[cur_node]:
        if visited[next_node]:
            continue

        dfs(next_node)


dfs(r)

for i in range(1, n + 1):
    print(visited[i])
