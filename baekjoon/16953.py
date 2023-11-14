import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split(" "))

min_cnt = sys.maxsize
q = deque([[a, 1]])
while q:
    cur, cnt = q.popleft()

    if cur == b:
        min_cnt = min(min_cnt, cnt)

    # 2 곱하기
    next = cur * 2
    if next <= b:
        q.append([next, cnt + 1])

    # 1 추가하기
    next = int(str(cur) + "1")
    if next <= b:
        q.append([next, cnt + 1])


if min_cnt < sys.maxsize:
    print(min_cnt)
else:
    print(-1)
