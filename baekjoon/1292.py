a, b = map(int, input().split(" "))

a_sum = 0
b_sum = 0


def get_sum(num) -> int:
    tmp_sum = 0
    i = 1
    cnt = 0
    while cnt < num:
        if cnt + i <= num:
            tmp_sum += i * i
            cnt += i
        else:
            tmp_sum += i * (num - cnt)
            cnt = num

        i += 1
    return tmp_sum


print(get_sum(b) - get_sum(a - 1))
