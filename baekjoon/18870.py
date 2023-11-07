import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))

sorted_map = {}
for i, num in enumerate(sorted(list(set(arr)))):
    sorted_map[num] = i

answer = []
for num in arr:
    answer.append(sorted_map[num])

print(" ".join([str(i) for i in answer]))
