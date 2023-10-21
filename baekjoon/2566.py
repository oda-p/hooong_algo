matrix = [list(map(int, input().split(" "))) for _ in range(9)]

max_value = -1
idx = (0, 0)
for i in range(9):
    for j in range(9):
        tmp = matrix[i][j]
        if tmp > max_value:
            max_value = tmp
            idx = (i + 1, j + 1)

print(max_value)
print(f"{idx[0]} {idx[1]}")
