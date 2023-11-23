import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(" "))

board: list[list[int]] = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split(" "))))


def is_exist_cheese() -> bool:
    for row in board:
        for col in row:
            if col == 1:
                return True
    return False


def find_air() -> list[list[int]]:
    q = deque([(0, 0)])
    _air = [[False for _ in range(m)] for _ in range(n)]
    _air[0][0] = True

    while q:
        cur_y, cur_x = q.popleft()

        dpos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dy, dx in dpos:
            next_y = cur_y + dy
            next_x = cur_x + dx

            if 0 <= next_x < m and 0 <= next_y < n:
                if not _air[next_y][next_x] and board[next_y][next_x] == 0:
                    _air[next_y][next_x] = True
                    q.append((next_y, next_x))

    return _air


def get_delete_cheese(_air) -> list[list[int]]:
    _delete_cheese = []

    for cur_y in range(n):
        for cur_x in range(m):
            air_cnt = 0

            if board[cur_y][cur_x] == 1:
                dpos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dy, dx in dpos:
                    next_y = cur_y + dy
                    next_x = cur_x + dx

                    if board[next_y][next_x] == 0 and _air[next_y][next_x]:
                        air_cnt += 1

            if air_cnt >= 2:
                _delete_cheese.append([cur_y, cur_x])

    return _delete_cheese


hours = 0
while is_exist_cheese():
    for delete_y, delete_x in get_delete_cheese(find_air()):
        board[delete_y][delete_x] = 0
    hours += 1

print(hours)
