import heapq

t = int(input())

for _ in range(t):
    n = int(input())

    pq = []
    for _ in range(n):
        scores = list(map(int, input().split(" ")))
        heapq.heappush(pq, scores)

    success_cnt = 0
    min_score = n + 1
    while pq:
        _, score = heapq.heappop(pq)

        if score < min_score:
            success_cnt += 1
            min_score = score

    print(success_cnt)
