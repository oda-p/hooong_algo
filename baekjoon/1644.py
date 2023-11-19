def solution(n):
    if n == 1:
        return 0

    # 에라토스테네스의 체 이용 (소수 구하기)
    prime_nums = []
    numbers = [False for _ in range(n + 1)]
    for i in range(2, n + 1):
        if numbers[i]:
            continue

        prime_nums.append(i)
        tmp = i
        while tmp <= n:
            numbers[tmp] = True
            tmp += i

    # 투포인터로 연속된 합 구하기
    i, j = 0, 0
    sum_num = prime_nums[0]
    cnt = 0
    while j < len(prime_nums):
        if sum_num <= n:
            if sum_num == n:
                cnt += 1

            j += 1
            if j == len(prime_nums):
                break
            sum_num += prime_nums[j]
        else:
            if i < j:
                sum_num -= prime_nums[i]
                i += 1
            else:
                j += 1
                if j == len(prime_nums):
                    break
                sum_num += prime_nums[j]

    while i < j:
        sum_num -= prime_nums[i]

        if sum_num == n:
            cnt += 1

        i += 1
        if i == j:
            break

    return cnt


n = int(input())
print(solution(n))
