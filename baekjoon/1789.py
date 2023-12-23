s = int(input())

sum_of_nums = 0
cnt = 0
i = 1
while sum_of_nums < s:
    sum_of_nums += i
    i += 1
    cnt += 1

if sum_of_nums == s:
    print(cnt)
else:
    print(cnt - 1)
