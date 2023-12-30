n = int(input())
arr_a = list(map(int, input().split(" ")))
arr_b = list(map(int, input().split(" ")))

arr_a.sort()
arr_b.sort(reverse=True)
tmp_1 = 0
for i in range(n):
    tmp_1 += arr_a[i] * arr_b[i]

arr_a.sort(reverse=True)
arr_b.sort()
tmp_2 = 0
for i in range(n):
    tmp_2 += arr_a[i] * arr_b[i]

print(min(tmp_1, tmp_2))
