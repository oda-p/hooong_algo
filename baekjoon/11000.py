import heapq

n = int(input())

classes = []
for _ in range(n):
    classes.append(list(map(int, input().split(" "))))
classes.sort(key=lambda x: [x[0], x[1]])

q = []
for s, e in classes:
    if not q:
        heapq.heappush(q, e)
        continue

    min_e = heapq.heappop(q)
    if min_e > s:
        heapq.heappush(q, min_e)
    heapq.heappush(q, e)

print(len(q))
