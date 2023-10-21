paper = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split(" "))

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

answer = 0
for row in paper:
    answer += sum(row)

print(answer)
