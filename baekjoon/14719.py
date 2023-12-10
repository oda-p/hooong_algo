h, w = map(int, input().split(" "))
blocks = list(map(int, input().split(" ")))

front = [0 for _ in range(w)]
back = [0 for _ in range(w)]

tmp_max = 0
for i in range(w):
    tmp_max = max(tmp_max, blocks[i])
    front[i] = tmp_max

tmp_max = 0
for i in range(w - 1, -1, -1):
    tmp_max = max(tmp_max, blocks[i])
    back[i] = tmp_max

max_list = [0 for _ in range(w)]
for i in range(w):
    max_list[i] = min(front[i], back[i])

answer = 0
for i in range(w):
    answer += max_list[i] - blocks[i]

print(answer)
