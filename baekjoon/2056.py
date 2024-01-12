from collections import deque

n = int(input())

times = [0 for _ in range(n + 1)]
incomes = [0 for _ in range(n + 1)]
pre_jobs = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    pre_job = list(map(int, input().split(" ")))
    times[i] = pre_job.pop(0)
    pre_job.pop(0)
    pre_jobs[i] = pre_job
    for job in pre_job:
        incomes[job] += 1

q = deque()
for i in range(1, n + 1):
    if incomes[i] == 0:
        q.append(i)

sorted_jobs = []
while q:
    cur = q.popleft()
    sorted_jobs.append(cur)

    for pre_job in pre_jobs[cur]:
        incomes[pre_job] -= 1
        if incomes[pre_job] == 0:
            q.append(pre_job)

dp = [0 for _ in range(n + 1)]
for cur_job in sorted_jobs[::-1]:
    max_pre_time = 0
    for pre_job in pre_jobs[cur_job]:
        max_pre_time = max(max_pre_time, dp[pre_job])

    dp[cur_job] = max_pre_time + times[cur_job]

print(max(dp))
