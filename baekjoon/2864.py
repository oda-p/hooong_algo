a, b = map(int, input().split(" "))

min_a = ""
max_a = ""
for num in str(a):
    if num in ["5", "6"]:
        min_a += "5"
        max_a += "6"
    else:
        min_a += num
        max_a += num

min_b = ""
max_b = ""
for num in str(b):
    if num in ["5", "6"]:
        min_b += "5"
        max_b += "6"
    else:
        min_b += num
        max_b += num

print(int(min_a) + int(min_b), int(max_a) + int(max_b))
