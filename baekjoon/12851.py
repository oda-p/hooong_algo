import sys
from collections import deque

n, k = map(int, input().split(" "))


def solution():
    if n == k:
        print(0)
        print(1)
        return

    visited = [sys.maxsize for _ in range(100001)]

    min_sec = sys.maxsize
    cnt = []
    q = deque([(n, 0)])
    visited[n] = 0
    while q:
        cur_pos, sec = q.popleft()

        dxs = [1, -1, cur_pos]
        for dx in dxs:
            next_pos = cur_pos + dx

            if 0 <= next_pos <= 100000:
                if next_pos == k:
                    min_sec = min(min_sec, sec + 1)
                    cnt.append(sec + 1)
                    continue
                if visited[next_pos] >= sec + 1:
                    visited[next_pos] = sec + 1
                    q.append((next_pos, sec + 1))

    print(min_sec)
    print(cnt.count(min_sec))


solution()
