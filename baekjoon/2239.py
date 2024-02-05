row_board = [[0 for _ in range(9)] for _ in range(9)]  # 가로 기준으로
col_board = [[0 for _ in range(9)] for _ in range(9)]  # 세로 기준으로

# 문제 입력
target_list = []
for i in range(9):
    s = input()
    for j in range(9):
        num = int(s[j])
        row_board[i][j] = num
        col_board[j][i] = num

        if num == 0:
            target_list.append([i, j])


def check_square(r, c, num) -> bool:
    global row_board

    tmp_r = (r // 3) * 3
    tmp_c = (c // 3) * 3
    for square_r in range(tmp_r, tmp_r + 3):
        for square_c in range(tmp_c, tmp_c + 3):
            if num == row_board[square_r][square_c]:
                return False
    return True


def dfs(level) -> bool:
    if level == len(target_list):
        return True

    cur_r, cur_c = target_list[level]

    for num in range(1, 10):
        if (
            num not in row_board[cur_r]
            and num not in col_board[cur_c]
            and check_square(cur_r, cur_c, num)
        ):
            row_board[cur_r][cur_c] = num
            col_board[cur_c][cur_r] = num

            if dfs(level + 1):
                return True

            row_board[cur_r][cur_c] = 0
            col_board[cur_c][cur_r] = 0
    return False


dfs(0)
for row in row_board:
    print("".join([str(i) for i in row]))
