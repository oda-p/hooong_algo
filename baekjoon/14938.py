import heapq
import sys

n, m, r = map(int, sys.stdin.readline().split(" "))
num_of_items = list(map(int, sys.stdin.readline().split(" ")))

adj_list = [[] for _ in range(n + 1)]
for _ in range(r):
    s, e, l = map(int, sys.stdin.readline().split(" "))
    adj_list[s].append((e, l))
    adj_list[e].append((s, l))


def dijkstra(start) -> list[int]:
    dp = [sys.maxsize for _ in range(n + 1)]

    q = [[0, start]]
    dp[start] = 0
    while q:
        cur_cost, cur_node = heapq.heappop(q)

        for next_node, next_cost in adj_list[cur_node]:
            if dp[next_node] > cur_cost + next_cost:
                dp[next_node] = cur_cost + next_cost
                heapq.heappush(q, [dp[next_node], next_node])

    return dp


min_length_tables = []
for i in range(1, n + 1):
    min_length_tables.append(dijkstra(i))

max_num_of_items = 0
for min_length_table in min_length_tables:
    sum_of_items = 0
    for i in range(1, n + 1):
        if min_length_table[i] <= m:
            sum_of_items += num_of_items[i - 1]

    max_num_of_items = max(max_num_of_items, sum_of_items)

print(max_num_of_items)
