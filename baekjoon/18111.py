import sys

n, m, b = map(int, sys.stdin.readline().split(" "))

min_time = sys.maxsize
max_target_height = 0

board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split(" "))))

for target_height in range(257):
    add_blocks = 0
    remove_blocks = 0

    for row in board:
        for cur_height in row:
            diff = target_height - cur_height

            if diff < 0:
                remove_blocks += -diff
            elif diff > 0:
                add_blocks += diff

    if remove_blocks + b >= add_blocks:
        time = remove_blocks * 2 + add_blocks
        if time <= min_time:
            min_time = time
            max_target_height = target_height

print(min_time, max_target_height)
