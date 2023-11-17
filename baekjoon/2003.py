n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
i, j = 0, 0

answer = 0
tmp_sum = arr[0]
while True:
    if tmp_sum == m:
        answer += 1

    if tmp_sum <= m:
        if i == n - 1:
            break

        i += 1
        tmp_sum += arr[i]

    elif tmp_sum > m:
        if j < i:
            tmp_sum -= arr[j]
            j += 1
        else:
            if i == n - 1:
                break
            i += 1
            tmp_sum += arr[i]

if tmp_sum >= m and j <= i:
    tmp_sum -= arr[j]
    j += 1

    if tmp_sum == m:
        answer += 1

print(answer)
