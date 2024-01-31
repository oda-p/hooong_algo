from collections import deque

n, m, r = map(int, input().split(" "))

adj_list: list[list[int]] = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split(" "))
    adj_list[s].append(e)
    adj_list[e].append(s)

for adj in adj_list:
    adj.sort(reverse=True)

visited = [0 for _ in range(n + 1)]
q = deque([r])
visited[r] = 1
cnt = 1
while q:
    cur_node = q.popleft()

    for next_node in adj_list[cur_node]:
        if not visited[next_node]:
            cnt += 1
            visited[next_node] = cnt
            q.append(next_node)

for i in range(1, len(visited)):
    print(visited[i])
