import heapq

n = int(input())
k = int(input())
sensors = list(map(int, input().split(" ")))
sensors.sort()

distances = []
for i in range(1, len(sensors)):
    heapq.heappush(distances, sensors[i - 1] - sensors[i])

cnt = 1
while cnt != k:
    if not distances:
        break

    cnt += 1
    heapq.heappop(distances)

print(sum(distances) * -1)
