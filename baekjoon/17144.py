import sys
from collections import deque

r, c, t = map(int, sys.stdin.readline().split(" "))

board = []
purifier_row = []
for i in range(r):
    tmp_row = list(map(int, sys.stdin.readline().split(" ")))

    if tmp_row[0] == -1:
        purifier_row.append(i)

    board.append(tmp_row)


def do_spread(_board):
    q = deque([])
    for row in range(r):
        for col in range(c):
            dust = _board[row][col]
            if dust not in [-1, 0]:
                q.append((row, col, dust))

    while q:
        cur_row, cur_col, dust = q.popleft()

        spread_dust = dust // 5
        total_spread_dust = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d_row, d_col in directions:
            next_row = cur_row + d_row
            next_col = cur_col + d_col
            if 0 <= next_row < r and 0 <= next_col < c:
                if _board[next_row][next_col] != -1:
                    _board[next_row][next_col] += spread_dust
                    total_spread_dust += spread_dust

        _board[cur_row][cur_col] -= total_spread_dust
    return _board


def do_clean(_board):
    up_purifier_row, down_purifier_row = purifier_row

    before_dust = 0
    for i in range(c):
        if i == 0:
            before_dust = 0
            continue

        swap_tmp = _board[up_purifier_row][i]
        _board[up_purifier_row][i] = before_dust
        before_dust = swap_tmp

    for i in range(up_purifier_row - 1, -1, -1):
        swap_tmp = _board[i][c - 1]
        _board[i][c - 1] = before_dust
        before_dust = swap_tmp

    for i in range(c - 2, -1, -1):
        swap_tmp = _board[0][i]
        _board[0][i] = before_dust
        before_dust = swap_tmp

    for i in range(1, up_purifier_row):
        swap_tmp = _board[i][0]
        _board[i][0] = before_dust
        before_dust = swap_tmp

    for i in range(c):
        if i == 0:
            before_dust = 0
            continue

        swap_tmp = _board[down_purifier_row][i]
        _board[down_purifier_row][i] = before_dust
        before_dust = swap_tmp

    for i in range(down_purifier_row + 1, r):
        swap_tmp = _board[i][c - 1]
        _board[i][c - 1] = before_dust
        before_dust = swap_tmp

    for i in range(c - 2, -1, -1):
        swap_tmp = _board[r - 1][i]
        _board[r - 1][i] = before_dust
        before_dust = swap_tmp

    for i in range(r - 2, down_purifier_row, -1):
        swap_tmp = _board[i][0]
        _board[i][0] = before_dust
        before_dust = swap_tmp

    return _board


def calc_total_dust(board):
    dust = 0
    for row in board:
        dust += sum(row)

    return dust + 2


for _ in range(t):
    board = do_spread(board)
    board = do_clean(board)

print(calc_total_dust(board))
