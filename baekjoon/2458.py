from collections import deque

n, m = map(int, input().split(" "))

# 0: 나가는 방향, 1: 들어오는 방향
adj_list = [{"in": [], "out": []} for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split(" "))
    adj_list[a]["out"].append(b)
    adj_list[b]["in"].append(a)

answer = 0
for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    visited[i] = True

    # 나가는 방향 확인
    q = deque([i])
    while q:
        cur = q.popleft()

        for next in adj_list[cur]["out"]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

    # 들어오는 방향 확인
    q = deque([i])
    while q:
        cur = q.popleft()

        for next in adj_list[cur]["in"]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

    if visited.count(False) == 1:
        answer += 1

print(answer)
