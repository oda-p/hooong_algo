import sys


class Node:
    pre_node = None
    next_node = None
    ch = None

    def __init__(self, ch, pre_node, next_node):
        self.ch = ch
        self.pre_node = pre_node
        self.next_node = next_node


t = int(input())
for _ in range(t):
    inputs = sys.stdin.readline().replace("\n", "")
    head = Node(None, None, None)
    before = head
    cursor = before

    for ch in inputs:
        if ch == "<":
            if not cursor.ch:
                continue

            cursor = cursor.pre_node
        elif ch == ">":
            if not cursor.next_node:
                continue

            cursor = cursor.next_node
        elif ch == "-":
            if not cursor.ch:
                continue

            if cursor.next_node:
                cursor.next_node.pre_node = cursor.pre_node
            cursor.pre_node.next_node = cursor.next_node
            cursor = cursor.pre_node
        else:
            new_node = Node(ch, cursor, cursor.next_node)
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
    print()
