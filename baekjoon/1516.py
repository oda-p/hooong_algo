import sys
from collections import deque

n = int(input())

times = [[]]
dependencies = [[]]
for _ in range(n):
    inputs = list(map(int, input().split(" ")))
    times.append(inputs.pop(0))

    inputs.pop()  # -1 제거
    dependencies.append(inputs)

in_degree = [0 for _ in range(n + 1)]
for dependency in dependencies:
    for i in dependency:
        in_degree[i] += 1

q = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)

stack = []
while q:
    cur = q.popleft()

    stack.append(cur)

    for i in dependencies[cur]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)

dp = [0 for _ in range(n + 1)]
while stack:
    cur = stack.pop()

    max_time = 0
    for i in dependencies[cur]:
        max_time = max(max_time, dp[i])

    dp[cur] = times[cur] + max_time

for i in range(1, n + 1):
    print(dp[i])
