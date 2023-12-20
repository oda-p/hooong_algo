import sys

n, m, r = map(int, input().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split(" "))))

i = 0
while i < n - (i + 1) and i < m - (i + 1):
    for _ in range(r):
        # 회전 로직
        tmp = board[i][i]
        # 위
        for k in range(i + 1, m - i):
            board[i][k - 1] = board[i][k]

        # 왼
        for k in range(i + 1, n - i):
            board[k][i], tmp = tmp, board[k][i]

        # 아
        for k in range(i + 1, m - i):
            board[n - (i + 1)][k], tmp = tmp, board[n - (i + 1)][k]

        # 오
        for k in range(n - (i + 2), i - 1, -1):
            board[k][m - (i + 1)], tmp = tmp, board[k][m - (i + 1)]

    i += 1

for i in range(n):
    for j in range(m):
        print(board[i][j], end=" ")
    print()
