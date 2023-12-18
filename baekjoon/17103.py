t = int(input())

eratos = [False for _ in range(1000001)]
for i in range(2, 1000001):
    if eratos[i]:
        continue

    tmp = i * i
    while tmp <= 1000000:
        eratos[tmp] = True
        tmp += i

for _ in range(t):
    n = int(input())

    cnt = 0
    prime_nums = []
    for i in range(2, n + 1):
        if eratos[i]:
            continue
        prime_nums.append(i)

    start, end = 0, len(prime_nums) - 1
    while start <= end:
        sum_of_two_nums = prime_nums[start] + prime_nums[end]
        if sum_of_two_nums == n:
            cnt += 1

        if sum_of_two_nums <= n:
            start += 1
        else:
            end -= 1

    print(cnt)
