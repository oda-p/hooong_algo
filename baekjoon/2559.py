import sys

n, k = map(int, input().split(" "))
temps = list(map(int, input().split(" ")))

window_size = k
front, back = 0, k - 1

tmp_sum = sum(temps[front : back + 1])
max_sum = tmp_sum
while back <= n - 2:
    back += 1
    tmp_sum += temps[back]
    tmp_sum -= temps[front]
    front += 1

    max_sum = max(max_sum, tmp_sum)

print(max_sum)
