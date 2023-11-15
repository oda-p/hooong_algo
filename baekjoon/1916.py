import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

adj_list = [[] for i in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, sys.stdin.readline().split(" "))
    adj_list[s].append([e, t])

target_s, target_e = map(int, sys.stdin.readline().split(" "))

distance = [sys.maxsize for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
distance[target_s] = 0
q = [[0, target_s]]
while q:
    cur_cost, cur_node = heapq.heappop(q)
    if visited[cur_node]:
        # 방문여부를 확인함으로써 시간 단축!
        continue
    visited[cur_node] = True

    for next_node, next_cost in adj_list[cur_node]:
        if distance[next_node] > cur_cost + next_cost:
            distance[next_node] = cur_cost + next_cost
            heapq.heappush(q, [distance[next_node], next_node])

print(distance[target_e])
