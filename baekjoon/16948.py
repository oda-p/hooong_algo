from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split(" "))

#  (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)
dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

board = [[100000 for _ in range(n)] for _ in range(n)]
board[r1][c1] = 0


q = deque([(r1, c1, 0)])
while q:
    r, c, level = q.popleft()

    if r == r2 and c == c2:
        board[r][c] = min(board[r][c], level + 1)

    for i in range(len(dr)):
        next_r = r + dr[i]
        next_c = c + dc[i]

        if 0 <= next_r < n and 0 <= next_c < n:
            if board[next_r][next_c] > level + 1:
                board[next_r][next_c] = level + 1
                q.append((next_r, next_c, level + 1))

if board[r2][c2] == 100000:
    print(-1)
else:
    print(board[r2][c2])
