from collections import deque

r, c = map(int, input().split(" "))
meadow = []
for _ in range(r):
    meadow.append(input())

visited = [[False for _ in range(c)] for _ in range(r)]

sheep_and_cows = []
for i in range(r):
    for j in range(c):
        if visited[i][j] or meadow[i][j] == "#":
            continue

        group = [0, 0]  # sheep, cow
        q = deque([[i, j]])
        visited[i][j] = True
        while q:
            cur_r, cur_c = q.popleft()

            if meadow[cur_r][cur_c] == "o":
                group[0] += 1
            elif meadow[cur_r][cur_c] == "v":
                group[1] += 1

            d_pos = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for d_r, d_c in d_pos:
                next_r = cur_r + d_r
                next_c = cur_c + d_c

                if 0 <= next_r < r and 0 <= next_c < c:
                    if (
                        not visited[next_r][next_c]
                        and not meadow[next_r][next_c] == "#"
                    ):
                        visited[next_r][next_c] = True
                        q.append([next_r, next_c])
        sheep_and_cows.append(group)

sheep = 0
cow = 0
for p_sheep, p_cow in sheep_and_cows:
    if p_sheep > p_cow:
        sheep += p_sheep
    else:
        cow += p_cow

print(sheep, cow)
