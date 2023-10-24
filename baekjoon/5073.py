def is_triangle(a, b, c):
    max_len = max(a, max(b, c))

    return max_len < (a + b + c) - max_len


while True:
    a, b, c = map(int, input().split(" "))

    if a == b == c == 0:
        break

    if not is_triangle(a, b, c):
        print("Invalid")
        continue

    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
