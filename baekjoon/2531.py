n, d, k, c = map(int, input().split(" "))

sushi = []
for i in range(n):
    sushi.append(int(input()))

s = 0
e = k - 1
tmp = sushi[s : e + 1]

max_cnt = 0
max_target = []
while s < n:
    sushi_cnt = len(set(tmp))

    if sushi_cnt > max_cnt:
        max_cnt = sushi_cnt
        max_target = [set(tmp)]
    elif sushi_cnt == max_cnt:
        max_target.append(set(tmp))

    s += 1
    tmp.pop(0)

    e = (e + 1) % n
    tmp.append(sushi[e])

for target in max_target:
    if c not in target:
        max_cnt += 1
        break

print(max_cnt)
