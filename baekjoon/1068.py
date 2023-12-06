n = int(input())
arr = list(map(int, input().split(" ")))
del_target_node = int(input())

tree = {i: [] for i in range(n)}
for node, p_node in enumerate(arr):
    if p_node == -1:
        continue

    tree[p_node].append(node)


def delete_node(del_node):
    del_child_list = tree.pop(del_node)

    for del_child in del_child_list:
        delete_node(del_child)


delete_node(del_target_node)

leaf_cnt = 0
for child_list in tree.values():
    if del_target_node in child_list:
        child_list.remove(del_target_node)

    if not child_list:
        leaf_cnt += 1

print(leaf_cnt)
