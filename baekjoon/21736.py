import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(" "))

board = []
start = []
for y in range(n):
    row = sys.stdin.readline().replace("\n", "")
    board.append(row)
    for x in range(m):
        if row[x] == "I":
            start = [y, x]

visited = [[False for _ in range(m)] for _ in range(n)]
visited[start[0]][start[1]] = True
q = deque([start])
cnt = 0
while q:
    cur_y, cur_x = q.pop()

    if board[cur_y][cur_x] == "P":
        cnt += 1

    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_y = cur_y + dy
        next_x = cur_x + dx

        if 0 <= next_y < n and 0 <= next_x < m:
            if not visited[next_y][next_x] and not board[next_y][next_x] == "X":
                visited[next_y][next_x] = True
                q.appendleft([next_y, next_x])

print(cnt if cnt else "TT")
