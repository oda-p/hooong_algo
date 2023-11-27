import sys


class Node:
    pre_node = None
    next_node = None
    ch = None

    def __init__(self, ch, pre_node, next_node):
        self.ch = ch
        self.pre_node = pre_node
        self.next_node = next_node


init_str = sys.stdin.readline().replace("\n", "")
head = Node(None, None, None)
before = head
for ch in init_str:
    cur_node = Node(ch, before, None)

    if before:
        before.next_node = cur_node
    before = cur_node
cursor = before


m = int(input())
for _ in range(m):
    op_str = list(map(str, sys.stdin.readline().replace("\n", "").split(" ")))
    op = op_str[0]

    if op == "L":
        if not cursor.ch:
            continue

        cursor = cursor.pre_node
    elif op == "D":
        if not cursor.next_node:
            continue

        cursor = cursor.next_node
    elif op == "B":
        if not cursor.ch:
            continue

        if cursor.next_node:
            cursor.next_node.pre_node = cursor.pre_node
        cursor.pre_node.next_node = cursor.next_node
        cursor = cursor.pre_node
    else:
        add_ch = op_str[1]
        new_node = Node(add_ch, cursor, cursor.next_node)
        if cursor.next_node:
            cursor.next_node.pre_node = new_node
        cursor.next_node = new_node
        cursor = new_node

cur = head
while True:
    if cur.ch:
        print(cur.ch, end="")

    if not cur.next_node:
        break
    cur = cur.next_node
