import heapq
import sys
from collections import deque

n = int(input())
m = int(input())

adj_list = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split(" "))
    adj_list[s].append(e)
    adj_list[e].append(s)

dis = [sys.maxsize for _ in range(n + 1)]
dis[1] = 0
q = [[0, 1]]
while q:
    cost, cur = heapq.heappop(q)

    for next in adj_list[cur]:
        if dis[next] > cost + 1:
            dis[next] = cost + 1
            heapq.heappush(q, [dis[next], next])

cnt = 0
for d in dis:
    if d <= 2:
        cnt += 1

print(cnt - 1)
