def insert_trie(trie: dict, num: str) -> None:
    cur = trie
    for c in num:
        if c not in cur:
            cur[c] = {}
        cur = cur[c]


def find_leaf(trie: dict, num: str) -> dict:
    cur = trie
    for c in num:
        cur = cur[c]
    return cur


t = int(input())

for _ in range(t):
    n = int(input())

    trie = {}
    nums = []
    for _ in range(n):
        number = input()
        nums.append(number)
        insert_trie(trie, number)

    has_consistency = True
    for num in nums:
        leaf = find_leaf(trie, num)
        if leaf:
            has_consistency = False
            break

    print("YES" if has_consistency else "NO")
