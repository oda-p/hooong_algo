import sys

l = int(sys.stdin.readline())
target_str = sys.stdin.readline()

m = 1234567891
alpha_map = "abcdefghijklmnopqrstuvwxyz"

answer = 0
r_i = 1
for ch in target_str:
    a_i = alpha_map.find(ch) + 1
    answer += (r_i * a_i) % m

    r_i = (r_i * 31) % m

print(answer % m)
