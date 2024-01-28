n = int(input())
m = int(input())

links = []
for _ in range(m):
    links.append(list(map(int, input().split(" "))))
links.sort(key=lambda x: x[2])

parents = [i for i in range(n + 1)]


def find(x):
    global parents

    if parents[x] == x:
        return x
    return find(parents[x])


def union(x, y):
    global parents
    y = find(y)
    parents[y] = find(x)


def is_linked(x, y):
    if find(x) == find(y):
        return True
    return False


min_cost = 0
for a, b, c in links:
    if is_linked(a, b):
        continue

    union(a, b)

    min_cost += c

print(min_cost)
