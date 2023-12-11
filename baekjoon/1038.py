from itertools import combinations

n = int(input())

if n < 10:
    print(n)
    exit()

dp = [[0 for _ in range(10)], [1 for _ in range(10)]]

cnt = 9
i = 2
j = 1
while i < 11:
    dp.append([0 for _ in range(10)])
    is_end = False

    j = 1
    while j < 10:
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

        if cnt + dp[i][j] >= n:
            is_end = True
            break

        cnt += dp[i][j]
        j += 1

    if is_end:
        break

    i += 1

if i == 11:
    print(-1)
    exit()

num_len = i
first_num = j

tmp_list = []
for arr in combinations(range(first_num), i - 1):
    arr = list(arr)
    tmp_list.append(int("".join([str(num) for num in sorted(arr, reverse=True)])))

tmp_list.sort()

print(str(first_num) + str(tmp_list[n - cnt - 1]))
