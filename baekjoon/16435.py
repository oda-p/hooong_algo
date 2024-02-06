n, l = map(int, input().split(" "))
fruits = list(map(int, input().split(" ")))

fruits.sort()

while fruits:
    cur_fruit = fruits.pop(0)

    if l >= cur_fruit:
        l += 1
    else:
        break

print(l)
