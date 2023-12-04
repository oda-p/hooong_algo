import heapq

n = int(input())
buildings = list(map(int, input().split(" ")))
received_table = [0 for _ in range(n + 1)]

q = []
for idx, height in enumerate(buildings, 1):
    while q:
        tmp, tmp_idx = heapq.heappop(q)

        if tmp < height:
            continue
        else:
            received_table[idx] = tmp_idx
            heapq.heappush(q, [tmp, tmp_idx])
            break

    heapq.heappush(q, [height, idx])

print(" ".join([str(i) for i in received_table[1:]]))
