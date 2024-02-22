from collections import deque

primes = [True for _ in range(100000)]
for i in range(2, 100000):
    tmp = i * 2
    while tmp < 100000:
        primes[tmp] = False
        tmp += i

t = int(input())
for _ in range(t):
    a, b = map(int, input().split(" "))

    visited = [False for _ in range(100000)]

    q = deque([(a, 0)])  # (num, cnt)
    visited[a] = True
    is_possible = False
    while q:
        cur, cnt = q.popleft()
        cur_s = str(cur)

        if cur == b:
            is_possible = True
            print(cnt)
            break

        for i in range(4):
            for j in range(10):
                if (i == 0 and j == 0) or (int(cur_s[i]) == j):
                    continue

                tmp = list(cur_s)
                tmp[i] = str(j)
                tmp = int("".join(tmp))

                if not visited[tmp] and primes[tmp]:
                    visited[tmp] = True
                    q.append((tmp, cnt + 1))
    if not is_possible:
        print("Impossible")
