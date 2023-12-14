import heapq
import sys

n, m, k, x = map(int, input().split(" "))

adj_list: list[list[int]] = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split(" "))
    adj_list[s].append(e)

d = [sys.maxsize for _ in range(n + 1)]
d[x] = 0
q = [[0, x]]
while q:
    cur_cost, cur_node = heapq.heappop(q)

    for next_node in adj_list[cur_node]:
        if cur_cost + 1 < d[next_node]:
            d[next_node] = cur_cost + 1
            heapq.heappush(q, [d[next_node], next_node])

if d.count(k) == 0:
    print(-1)
else:
    for idx, dis in enumerate(d):
        if dis == k:
            print(idx)
