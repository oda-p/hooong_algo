import heapq

n, k = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

q = []
for i in arr:
    heapq.heappush(q, i)

for _ in range(k - 1):
    heapq.heappop(q)
print(heapq.heappop(q))
