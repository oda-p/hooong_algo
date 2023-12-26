board = []
for _ in range(5):
    board.append(list(map(str, input().split(" "))))

possible = set()


def dfs(x, y, cur):
    cur += board[y][x]

    if len(cur) == 6:
        possible.add(cur)
        return

    d_pos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in d_pos:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, cur)


for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(possible))
