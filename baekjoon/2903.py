# 한 변의 점의 개수
# 2, 3, 5, 9, 17... -> before * 2 - 1

n = int(input())
side_dots = 2

for _ in range(n):
    side_dots = side_dots * 2 - 1

print(side_dots**2)
