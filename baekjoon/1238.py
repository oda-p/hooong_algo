import heapq
import sys

n, m, x = map(int, sys.stdin.readline().split(" "))

adj_list = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, sys.stdin.readline().split(" "))
    adj_list[s].append([e, t])


def dijkstra(start):
    dp = [sys.maxsize for _ in range(n + 1)]
    dp[start] = 0
    hq = []
    heapq.heappush(hq, [0, start])
    while hq:
        cur_cost, cur = heapq.heappop(hq)

        for next, next_cost in adj_list[cur]:
            if dp[next] > cur_cost + next_cost:
                dp[next] = cur_cost + next_cost
                heapq.heappush(hq, [dp[next], next])

    return dp


result_of_dijkstra = [[]]
for i in range(1, n + 1):
    result_of_dijkstra.append(dijkstra(i))

min_distances = []
for i in range(1, n + 1):
    min_distances.append(result_of_dijkstra[i][x] + result_of_dijkstra[x][i])

print(max(min_distances))
