from collections import deque

n, m, r = map(int, input().split(" "))

adj_list = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split(" "))
    adj_list[s].append(e)
    adj_list[e].append(s)

for adj in adj_list:
    adj.sort()

visited = [0 for _ in range(n + 1)]
q = deque([r])
visit_cnt = 1
visited[r] = visit_cnt
while q:
    cur_node = q.popleft()

    for next_node in adj_list[cur_node]:
        if not visited[next_node]:
            visit_cnt += 1
            visited[next_node] = visit_cnt
            q.append(next_node)

for i in range(1, n + 1):
    print(visited[i])
