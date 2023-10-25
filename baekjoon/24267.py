n = int(input())

answer = 0
for x in range(1, n - 1):
    answer += (x**2 + x) // 2

print(answer)
print(3)
