import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(" "))

start = (0, 0)
is_visit = [[False for _ in range(m)] for _ in range(n)]
board = []
for i in range(n):
    row = list(map(int, input().split(" ")))

    if 2 in row:
        start = (i, row.index(2))

    board.append(row)

answer = [[0 for _ in range(m)] for _ in range(n)]
q = deque([(start[0], start[1], 0)])
is_visit[start[0]][start[1]] = True
while q:
    cur_row, cur_col, distance = q.popleft()

    if not board[cur_row][cur_col] == 0:
        answer[cur_row][cur_col] = distance

    for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        next_row = cur_row + i
        next_col = cur_col + j
        if 0 <= next_row < n and 0 <= next_col < m:
            if not is_visit[next_row][next_col] and board[next_row][next_col] == 1:
                is_visit[next_row][next_col] = True
                q.append((next_row, next_col, distance + 1))

for i in range(n):
    for j in range(m):
        if not is_visit[i][j] and board[i][j] == 1:
            answer[i][j] = -1

for row in answer:
    print(" ".join([str(i) for i in row]))
