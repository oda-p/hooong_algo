import heapq

n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

hq = []
for num in arr:
    heapq.heappush(hq, num)

for _ in range(m):
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)

    sum_of_nums = a + b
    for _ in range(2):
        heapq.heappush(hq, sum_of_nums)

print(sum(hq))
