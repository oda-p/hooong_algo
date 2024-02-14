n = int(input())
h_list = list(map(int, input().split(" ")))

answer = 0
min_h = h_list[0]
for i in range(1, n):
    cur = h_list[i]

    if cur > h_list[i - 1]:
        answer = max(cur - min_h, answer)
    else:
        min_h = cur

print(answer)
