import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()

target = "I"
for _ in range(n):
    target += "OI"

count = 0
for i in range(m - len(target) + 1):
    if not s[i] == "I":
        continue

    if s[i : i + len(target)] == target:
        count += 1

print(count)
