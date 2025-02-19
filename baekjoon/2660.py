import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
inf = 100000000

n = int(input())

adj_list: dict[int, list[int]] = defaultdict(list)
while True:
    a, b = map(int, input().split(" "))

    if a == -1 and b == -1:
        break

    adj_list[a - 1].append(b - 1)
    adj_list[b - 1].append(a - 1)

distances: list[list[int]] = []

for i in range(n):
    q: list[tuple[int, int]] = [(0, i)]
    d: list[int] = [inf for _ in range(n)]
    visited: list[bool] = [False for _ in range(n)]

    d[i] = 0
    while q:
        cost, cur_node = heapq.heappop(q)

        if visited[cur_node]:
            continue
        visited[cur_node] = True

        for next_node in adj_list[cur_node]:
            if not visited[next_node] and d[next_node] > d[cur_node] + 1:
                d[next_node] = d[cur_node] + 1
                heapq.heappush(q, (d[next_node], next_node))

    distances.append(d)

scores: list[int] = [max(distance) for distance in distances]
answer_score = min(scores)

print(answer_score, scores.count(answer_score))
print(
    " ".join([str(idx) for idx, score in enumerate(scores, 1) if score == answer_score])
)
