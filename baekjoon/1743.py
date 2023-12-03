import sys

sys.setrecursionlimit(1000000)

n, m, k = map(int, input().split(" "))
board = [[False for _ in range(m)] for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split(" "))
    board[r - 1][c - 1] = True

visited = [[False for _ in range(m)] for _ in range(n)]


def dfs(cur_y, cur_x) -> int:
    cnt = 1

    d_pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dy, dx in d_pos:
        next_y = cur_y + dy
        next_x = cur_x + dx

        if 0 <= next_y < n and 0 <= next_x < m:
            if not visited[next_y][next_x] and board[next_y][next_x]:
                visited[next_y][next_x] = True
                cnt += dfs(next_y, next_x)

    return cnt


max_size = 0
for row in range(n):
    for col in range(m):
        if not board[row][col]:
            continue

        if visited[row][col]:
            continue

        visited[row][col] = True
        max_size = max(max_size, dfs(row, col))

print(max_size)
