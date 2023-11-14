import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m, w = map(int, sys.stdin.readline().split(" "))

    adj_list = []
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split(" "))
        adj_list.append([s, e, t])
        adj_list.append([e, s, t])

    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split(" "))
        adj_list.append([s, e, -t])

    def bellman_ford():
        distance = [sys.maxsize for _ in range(n + 1)]
        for i in range(n):
            for cur_node, next_node, cost in adj_list:
                if distance[next_node] > distance[cur_node] + cost:
                    distance[next_node] = distance[cur_node] + cost
                    if i == n - 1:
                        return True
        return False

    has_negative_cycle = bellman_ford()
    print("YES" if has_negative_cycle else "NO")
