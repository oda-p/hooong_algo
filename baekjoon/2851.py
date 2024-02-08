mushrooms = []
for _ in range(10):
    mushrooms.append(int(input()))

score = 0
while mushrooms:
    cur_mushroom = mushrooms.pop(0)

    if abs(100 - score) < abs(100 - (score + cur_mushroom)):
        break

    score += cur_mushroom

print(score)
