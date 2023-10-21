matrix = [[-1 for _ in range(15)] for _ in range(5)]

for i in range(5):
    input_str = input()
    for j in range(len(input_str)):
        matrix[i][j] = input_str[j]

answer = ""
for j in range(15):
    for i in range(5):
        if matrix[i][j] == -1:
            continue
        answer += matrix[i][j]

print(answer)
