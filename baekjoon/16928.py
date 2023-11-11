import sys
from collections import deque

n, m = map(int, input().split(" "))

board = [sys.maxsize for _ in range(101)]

special_move_map = {}

for _ in range(n):
    start, end = map(int, input().split(" "))
    special_move_map[start] = end

for _ in range(m):
    start, end = map(int, input().split(" "))
    special_move_map[start] = end

q = deque([(1, 0)])
while q:
    cur, cnt = q.popleft()

    if cur in special_move_map:
        next = special_move_map[cur]
        if board[next] > cnt:
            board[next] = cnt
            q.append((next, cnt))
        continue

    for i in range(1, 7):
        next = cur + i
        if next <= 100 and board[next] > cnt + 1:
            board[next] = cnt + 1
            q.append((next, cnt + 1))

print(board[100])
