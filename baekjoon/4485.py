import copy
import sys

p_num = 1
while True:
    n = int(input())

    if n == 0:
        break

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split(" "))))

    min_board = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
    min_board[1][1] = board[0][0]
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if r == 1 and c == 1:
                continue

            min_board[r][c] = min(min_board[r - 1][c], min_board[r][c - 1])
            min_board[r][c] += board[r - 1][c - 1]

    def find(tmp_board):
        for r in range(1, n + 1):
            for c in range(1, n + 1):
                if r == 1 and c == 1:
                    continue

                min_cost = sys.maxsize
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + dr
                    nc = c + dc

                    if 0 < nr <= n and 0 < nc <= n:
                        min_cost = min(min_cost, tmp_board[nr][nc])

                tmp_board[r][c] = min_cost + board[r - 1][c - 1]

        return tmp_board

    while True:
        next_board = find(copy.deepcopy(min_board))

        if min_board == next_board:
            break
        min_board = next_board

    print(f"Problem {p_num}: {min_board[n][n]}")
    p_num += 1
