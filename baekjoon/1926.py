import sys

sys.setrecursionlimit(1000000)

n, m = map(int, sys.stdin.readline().split(" "))

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split(" "))))


def dfs(cur_y, cur_x):
    tmp_cnt = 1
    d_pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dy, dx in d_pos:
        next_y = cur_y + dy
        next_x = cur_x + dx

        if 0 <= next_y < n and 0 <= next_x < m:
            if board[next_y][next_x] == 1:
                board[next_y][next_x] = 2
                tmp_cnt += dfs(next_y, next_x)

    return tmp_cnt


max_width = 0
paints_cnt = 0
for row in range(n):
    for col in range(m):
        if board[row][col] in [0, 2]:
            continue

        paints_cnt += 1
        board[row][col] = 2
        max_width = max(max_width, dfs(row, col))

print(paints_cnt)
print(max_width)
