import copy

n, l = map(int, input().split(" "))

rows = []
cols = [[] for _ in range(n)]
for _ in range(n):
    row = list(map(int, input().split(" ")))
    rows.append(row)

    for idx, num in enumerate(row):
        cols[idx].append(num)


def check(arr) -> bool:
    stack_1 = copy.deepcopy(arr)
    stack_2 = []
    h = stack_1[-1]
    is_possible = True
    while stack_1:
        cur = stack_1.pop()

        if abs(h - cur) > 1:
            is_possible = False
            break

        if h - cur == 1:
            tmp = 1
            while stack_1 and stack_1[-1] == cur and tmp != l:
                stack_1.pop()
                tmp += 1
            if tmp != l:
                is_possible = False
                break
            h = cur
            stack_2 = []
        elif h - cur == -1:
            tmp = 0
            while stack_2 and tmp != l:
                stack_2.pop()
                tmp += 1
            if tmp != l:
                is_possible = False
            h = cur
            stack_2 = [cur]
        else:
            stack_2.append(cur)

    return is_possible


cnt = 0
for row in rows:
    if check(row):
        cnt += 1

for col in cols:
    if check(col):
        cnt += 1

print(cnt)
