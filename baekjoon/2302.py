n = int(input())
m = int(input())

vips = []
for _ in range(m):
    vip = int(input())
    vips.append(vip)

split_nums = []
tmp = 0
for i in range(1, n + 1):
    if i in vips:
        if tmp:
            split_nums.append(tmp)
        tmp = 0
        continue
    tmp += 1
if tmp:
    split_nums.append(tmp)

dp = [0 for _ in range(41)]
dp[0] = 1
dp[1] = 1
dp[2] = 2


def find_cnt(num):
    if dp[num]:
        return dp[num]
    dp[num] = find_cnt(num - 1) + find_cnt(num - 2)
    return dp[num]


if split_nums:
    find_cnt(max(split_nums))

answer = 1
for split_num in split_nums:
    answer *= dp[split_num]

print(answer)
