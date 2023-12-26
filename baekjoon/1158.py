from collections import deque

n, k = map(int, input().split(" "))

q = deque([i for i in range(1, n + 1)])
answer = []

cnt = 0
while q:
    cur = q.popleft()
    cnt += 1

    if cnt == k:
        answer.append(cur)
        cnt = 0
        continue
    q.append(cur)

print("<" + ", ".join([str(i) for i in answer]) + ">")
