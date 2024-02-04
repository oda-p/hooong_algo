import sys

n, m = map(int, input().split(" "))

path_list = []
for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split(" "))
    path_list.append([c, s, e])

path_list.sort(key=lambda x: x[0])

parents = [i for i in range(n + 1)]
rank = [1 for i in range(n + 1)]


def find_root(x):
    global parents

    if x == parents[x]:
        return x
    return find_root(parents[x])


min_cost = 0
max_cost = 0
for c, h1, h2 in path_list:
    h1_root = find_root(h1)
    h2_root = find_root(h2)
    if h1_root == h2_root:
        continue

    if rank[h1_root] < rank[h2_root]:
        parents[h1_root] = h2_root
        rank[h2_root] += rank[h1_root]
    else:
        parents[h2_root] = h1_root
        rank[h1_root] += rank[h2_root]
    min_cost += c
    max_cost = max(max_cost, c)

print(min_cost - max_cost)
