k = int(input())
pre_order = list(map(int, input().split(" ")))

tree = [[] for _ in range(k)]


def make_tree(level, pre_order):
    global tree

    if level == k - 1:
        tree[level].append(pre_order[0])
        return

    root = len(pre_order) // 2

    tree[level].append(pre_order[root])
    make_tree(level + 1, pre_order[:root])
    make_tree(level + 1, pre_order[root + 1 :])


make_tree(0, pre_order)

for level in tree:
    print(" ".join([str(i) for i in level]))
