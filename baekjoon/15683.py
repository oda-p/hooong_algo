import copy

n, m = map(int, input().split(" "))

office = []
for _ in range(n):
    office.append(list(map(int, input().split(" "))))

cctv_list = []
for r in range(n):
    for c in range(m):
        tmp = office[r][c]

        if 0 < tmp < 6:
            cctv_list.append([tmp, r, c])

answer = n * m


def count_zero(cur_office) -> int:
    tmp_cnt = 0
    for r in range(n):
        for c in range(m):
            if cur_office[r][c] == 0:
                tmp_cnt += 1
    return tmp_cnt


def dfs(level, cur_office):
    global answer

    if level == len(cctv_list):
        answer = min(answer, count_zero(cur_office))
        return

    cctv, cur_r, cur_c = cctv_list[level]
    if cctv == 5:
        next_office = copy.deepcopy(cur_office)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_r = cur_r + dr
            next_c = cur_c + dc

            while 0 <= next_r < n and 0 <= next_c < m and office[next_r][next_c] != 6:
                next_office[next_r][next_c] = "#"
                next_r += dr
                next_c += dc
        dfs(level + 1, next_office)
    elif cctv == 4:
        for next_d in [
            [(1, 0), (-1, 0), (0, 1)],
            [(1, 0), (-1, 0), (0, -1)],
            [(1, 0), (0, 1), (0, -1)],
            [(-1, 0), (0, 1), (0, -1)],
        ]:
            next_office = copy.deepcopy(cur_office)
            for dr, dc in next_d:
                next_r = cur_r + dr
                next_c = cur_c + dc

                while (
                    0 <= next_r < n and 0 <= next_c < m and office[next_r][next_c] != 6
                ):
                    next_office[next_r][next_c] = "#"
                    next_r += dr
                    next_c += dc
            dfs(level + 1, next_office)
    elif cctv == 3:
        for next_d in [
            [(-1, 0), (0, 1)],
            [(0, 1), (1, 0)],
            [(1, 0), (0, -1)],
            [(-1, 0), (0, -1)],
        ]:
            next_office = copy.deepcopy(cur_office)
            for dr, dc in next_d:
                next_r = cur_r + dr
                next_c = cur_c + dc

                while (
                    0 <= next_r < n and 0 <= next_c < m and office[next_r][next_c] != 6
                ):
                    next_office[next_r][next_c] = "#"
                    next_r += dr
                    next_c += dc
            dfs(level + 1, next_office)
    elif cctv == 2:
        for next_d in [
            [(-1, 0), (1, 0)],
            [(0, 1), (0, -1)],
        ]:
            next_office = copy.deepcopy(cur_office)
            for dr, dc in next_d:
                next_r = cur_r + dr
                next_c = cur_c + dc

                while (
                    0 <= next_r < n and 0 <= next_c < m and office[next_r][next_c] != 6
                ):
                    next_office[next_r][next_c] = "#"
                    next_r += dr
                    next_c += dc
            dfs(level + 1, next_office)
    elif cctv == 1:
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_office = copy.deepcopy(cur_office)
            next_r = cur_r + dr
            next_c = cur_c + dc

            while 0 <= next_r < n and 0 <= next_c < m and office[next_r][next_c] != 6:
                next_office[next_r][next_c] = "#"
                next_r += dr
                next_c += dc
            dfs(level + 1, next_office)


dfs(0, office)
print(answer)
