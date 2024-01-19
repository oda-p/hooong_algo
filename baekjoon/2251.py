from collections import deque


def pour(from_l, to_l, target):
    nl2 = from_l + to_l
    nl1 = 0
    if nl2 > target:
        nl1 = nl2 - target
        nl2 = target
    return nl1, nl2


a, b, c = map(int, input().split(" "))

answer = set()
visit = [[[False for _ in range(c + 1)] for _ in range(b + 1)] for _ in range(a + 1)]
q = deque([[0, 0, c]])
visit[0][0][c] = True
while q:
    ca, cb, cc = q.popleft()

    if ca == 0:
        answer.add(cc)

    if ca:
        # cb로 붓기
        na, nb = pour(ca, cb, b)
        if not visit[na][nb][cc]:
            visit[na][nb][cc] = True
            q.append([na, nb, cc])

        # cc로 붓기
        na, nc = pour(ca, cc, c)
        if not visit[na][cb][nc]:
            visit[na][cb][nc] = True
            q.append([na, cb, nc])

    if cb:
        # ca로 붓기
        nb, na = pour(cb, ca, a)
        if not visit[na][nb][cc]:
            visit[na][nb][cc] = True
            q.append([na, nb, cc])

        # cc로 붓기
        nb, nc = pour(cb, cc, c)
        if not visit[ca][nb][nc]:
            visit[ca][nb][nc] = True
            q.append([ca, nb, nc])

    if cc:
        # ca로 붓기
        nc, na = pour(cc, ca, a)
        if not visit[na][cb][nc]:
            visit[na][cb][nc] = True
            q.append([na, cb, nc])

        # cb로 붓기
        nc, nb = pour(cc, cb, b)
        if not visit[ca][nb][nc]:
            visit[ca][nb][nc] = True
            q.append([ca, nb, nc])

print(" ".join([str(i) for i in sorted(list(answer))]))
