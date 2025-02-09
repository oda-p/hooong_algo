import sys
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split(" ")))

    nums.sort(reverse=True)

    q = deque([])

    is_left: bool = False
    for num in nums:
        if is_left:
            deque.appendleft(q, num)
        else:
            deque.append(q, num)

        is_left = not is_left

    level: int = 0
    for i in range(n):
        next_i: int = (i + 1) % n

        level = max(level, abs(q[i] - q[next_i]))

    print(level)
