import sys

n, s = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

min_cnt = sys.maxsize
start, end = 0, 0
tmp_sum = arr[0]
while True:
    if tmp_sum >= s:
        min_cnt = min(min_cnt, end - start + 1)
        tmp_sum -= arr[start]
        start += 1
    else:
        end += 1
        if end == n:
            break
        tmp_sum += arr[end]

if min_cnt < sys.maxsize:
    print(min_cnt)
else:
    print(0)
