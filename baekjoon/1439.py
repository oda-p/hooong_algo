s = input()
split_by_zero = s.split("0")
split_by_one = s.split("1")

while "" in split_by_zero:
    split_by_zero.remove("")

while "" in split_by_one:
    split_by_one.remove("")

print(min(len(split_by_zero), len(split_by_one)))
