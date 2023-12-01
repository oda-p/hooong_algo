import sys
from collections import deque

f, s, g, u, d = map(int, input().split(" "))

dp = [sys.maxsize for _ in range(f + 1)]
dp[s] = 0
q = deque([[s, 0]])
while q:
    cur_x, cnt = q.popleft()

    for dx in [u, -d]:
        next_x = cur_x + dx

        if 0 < next_x <= f:
            if cnt + 1 < dp[next_x]:
                dp[next_x] = cnt + 1
                q.append([next_x, cnt + 1])

print(dp[g] if dp[g] != sys.maxsize else "use the stairs")
