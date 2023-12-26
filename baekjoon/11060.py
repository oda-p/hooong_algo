from collections import deque

n = int(input())
miro = list(map(int, input().split(" ")))

visited = [False for _ in range(n)]
q = deque([[0, 0]])
visited[0] = True
answer = -1
while q:
    cur_idx, cnt = q.popleft()

    if cur_idx == n - 1:
        answer = cnt
        break

    for next_amount in range(1, miro[cur_idx] + 1):
        next_idx = cur_idx + next_amount

        if next_idx < n and not visited[next_idx]:
            q.append([next_idx, cnt + 1])
            visited[next_idx] = True

print(answer)
