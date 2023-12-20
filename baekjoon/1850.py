a, b = map(int, input().split(" "))


def find(big, small) -> int:
    tmp = big % small
    if tmp == 0:
        return small
    return find(small, tmp)


cnt = find(a, b)

print("1" * cnt)
