import sys

n = int(sys.stdin.readline())

board = []
for _ in range(n):
    board.append(list(map(str, sys.stdin.readline().strip("\n"))))

max_count = 0
visited = [[False for _ in range(n)] for _ in range(n)]


def all_find():
    global visited

    for y in range(n):
        for x in range(n):
            visited = [[False for _ in range(n)] for _ in range(n)]
            visited[y][x] = True

            d_p = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction in d_p:
                dfs(y, x, 1, direction)


def dfs(y, x, cnt, direction):
    global max_count, visited

    dy, dx = direction
    next_y = y + dy
    next_x = x + dx

    if 0 <= next_y < n and 0 <= next_x < n:
        if not visited[next_y][next_x] and board[y][x] == board[next_y][next_x]:
            visited[next_y][next_x] = True
            cnt += 1
            max_count = max(max_count, cnt)
            dfs(next_y, next_x, cnt, direction)


# 안 바뀐 상태에서 전체 한번 탐색
all_find()

for row in range(n):
    for col in range(n):
        d_pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for d_row, d_col in d_pos:
            next_row = row + d_row
            next_col = col + d_col

            if 0 <= next_row < n and 0 <= next_col < n:
                if board[row][col] == board[next_row][next_col]:
                    continue

                board[row][col], board[next_row][next_col] = (
                    board[next_row][next_col],
                    board[row][col],
                )

                search_target = [[row, col], [next_row, next_col]]

                up_down = [(0, 1), (0, -1)]
                left_right = [(1, 0), (-1, 0)]
                for target_row, target_col in search_target:
                    tmp_cnt = 0
                    for d_y, d_x in up_down:
                        search_row = target_row
                        search_col = target_col

                        while 0 <= search_col < n and 0 <= search_row < n:
                            if (
                                not board[target_row][target_col]
                                == board[search_row][search_col]
                            ):
                                break
                            tmp_cnt += 1
                            search_row += d_y
                            search_col += d_x
                    max_count = max(max_count, tmp_cnt - 1)

                    tmp_cnt = 0
                    for d_y, d_x in left_right:
                        search_row = target_row
                        search_col = target_col

                        while 0 <= search_col < n and 0 <= search_row < n:
                            if (
                                not board[target_row][target_col]
                                == board[search_row][search_col]
                            ):
                                break
                            tmp_cnt += 1
                            search_row += d_y
                            search_col += d_x
                    max_count = max(max_count, tmp_cnt - 1)

                board[row][col], board[next_row][next_col] = (
                    board[next_row][next_col],
                    board[row][col],
                )

print(max_count)
