import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()

cnt = 0
tmp_cnt = 0
cur = 0
while cur < m - 1:
    if s[cur : cur + 3] == "IOI":
        tmp_cnt += 1
        if tmp_cnt >= n:
            cnt += 1
        cur += 2
    else:
        tmp_cnt = 0
        cur += 1

print(cnt)
