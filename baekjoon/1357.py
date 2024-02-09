x, y = map(int, input().split(" "))


def rev(num):
    return int(str(num)[::-1])


print(rev(rev(x) + rev(y)))
