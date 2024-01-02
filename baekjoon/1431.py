from functools import cmp_to_key

n = int(input())

serial_numbers = []
for _ in range(n):
    serial_numbers.append(input())


def get_sum_of_number(s):
    sum_of_number = 0
    for ch in s:
        if ch.isdigit():
            sum_of_number += int(ch)
    return sum_of_number


def sort_key(a, b):
    if not len(a) == len(b):
        if len(a) > len(b):
            return 1
        else:
            return -1

    sum_of_a = get_sum_of_number(a)
    sum_of_b = get_sum_of_number(b)
    if not sum_of_a == sum_of_b:
        if sum_of_a > sum_of_b:
            return 1
        else:
            return -1

    if a > b:
        return 1
    else:
        return -1


serial_numbers.sort(key=cmp_to_key(sort_key))
for serial in serial_numbers:
    print(serial)
