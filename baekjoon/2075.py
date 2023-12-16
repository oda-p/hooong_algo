import heapq

n = int(input())

q = []
for _ in range(n):
    row = list(map(int, input().split(" ")))

    for num in row:
        heapq.heappush(q, num)

        if len(q) > n:
            heapq.heappop(q)

print(heapq.heappop(q))
