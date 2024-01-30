n, d, k, c = map(int, input().split(" "))

sushi = []
for i in range(n):
    sushi.append(int(input()))

max_cnt = 0
max_target = []
for i in range(n):
    tmp = set()
    cur = i
    for _ in range(k):
        tmp.add(sushi[cur])
        cur = (cur + 1) % n

    if len(tmp) > max_cnt:
        max_cnt = len(tmp)
        max_target = [tmp]
    elif len(tmp) == max_cnt:
        max_target.append(tmp)

for target in max_target:
    if c not in target:
        max_cnt += 1
        break

print(max_cnt)
