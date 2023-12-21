from collections import deque

n, m = map(int, input().split(" "))

incomes = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split(" "))
    incomes[b].append(a)

max_cnt = 0
max_coms = []
for com in range(1, n + 1):
    visited = [False for _ in range(n + 1)]

    q = deque([com])
    visited[com] = True
    cnt = 0
    while q:
        cur_com = q.popleft()
        cnt += 1

        for next_com in incomes[cur_com]:
            if not visited[next_com]:
                visited[next_com] = True
                q.append(next_com)

    if max_cnt == cnt:
        max_coms.append(com)
    elif max_cnt < cnt:
        max_cnt = cnt
        max_coms = [com]

print(" ".join([str(i) for i in max_coms]))
