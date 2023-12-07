import sys
from collections import deque

t = int(sys.stdin.readline())

for t in range(t):
    n = int(sys.stdin.readline())

    # 노드 입력
    nodes = dict()
    nodes["s"] = list(map(int, input().split(" ")))
    for i in range(n):
        nodes[str(i)] = list(map(int, input().split(" ")))
    nodes["e"] = list(map(int, input().split(" ")))

    # 방문 노드 확인을 위한 정보
    visited = {str(i): False for i in range(n)}
    visited["s"] = False
    visited["e"] = False

    # 각 노드에서 접근 가능한 노드 구하기
    adj_info = dict()
    for node, point in nodes.items():
        adj_info[node] = []
        for to_node, to_point in nodes.items():
            if node == to_node:
                continue

            x, y = point
            to_x, to_y = to_point

            distance = abs(x - to_x) + abs(y - to_y)
            if distance <= 1000:
                adj_info[node].append(to_node)

    # bfs
    q = deque(["s"])
    while q:
        cur_node = q.popleft()

        if cur_node == "e":
            break

        next_nodes = adj_info[cur_node]
        for next_node in next_nodes:
            if visited[next_node]:
                continue

            visited[next_node] = True
            q.append(next_node)

    if visited["e"]:
        print("happy")
    else:
        print("sad")
