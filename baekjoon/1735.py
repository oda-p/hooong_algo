a_1, b_1 = map(int, input().split(" "))
a_2, b_2 = map(int, input().split(" "))


def get_gcd(a, b):
    tmp = a % b
    if tmp == 0:
        return b
    return get_gcd(b, tmp)


gcd = get_gcd(max(b_1, b_2), min(b_1, b_2))
lcm = b_1 * b_2 // gcd

b_3 = lcm
a_3 = a_1 * (lcm // b_1) + a_2 * (lcm // b_2)

gcd = get_gcd(max(a_3, b_3), min(a_3, b_3))
b_3 = b_3 // gcd
a_3 = a_3 // gcd
print(a_3, b_3)
