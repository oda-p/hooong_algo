import sys

X = 1000000007
m = int(sys.stdin.readline())


def get_power(_b, num_of_power):
    if num_of_power == 1:
        return _b % X

    tmp = get_power(_b, num_of_power // 2) % X
    if num_of_power % 2 == 0:
        return tmp * tmp % X
    else:
        return (tmp * tmp % X) * (_b % X)


answer = 0
for _ in range(m):
    b, a = map(int, sys.stdin.readline().split(" "))
    answer += (a % X) * (get_power(b, X - 2) % X)

print(answer % X)
