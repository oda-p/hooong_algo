import copy
from collections import Counter, deque

n = int(input())
arr = list(map(int, input().split(" ")))

max_count = 1
l, r = 0, 0
tmp = {arr[0]: 1}
while r < len(arr) - 1:
    if len(tmp) <= 2:
        r += 1

        if arr[r] not in tmp:
            tmp[arr[r]] = 0
        tmp[arr[r]] += 1

        if len(tmp) <= 2:
            max_count = max(max_count, r - l + 1)

    else:
        tmp[arr[l]] -= 1
        if tmp[arr[l]] == 0:
            del tmp[arr[l]]

        l += 1

print(max_count)
