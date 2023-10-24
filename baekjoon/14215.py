a, b, c = map(int, input().split(" "))
max_len = max(a, max(b, c))

sum_of_other_len = a + b + c - max_len

if max_len < sum_of_other_len:
    print(a + b + c)
else:
    print(2 * sum_of_other_len - 1)
