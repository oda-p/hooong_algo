from collections import defaultdict

n, k = map(int, input().split(" "))

students = defaultdict(int)
for _ in range(n):
    sex, grade = map(int, input().split(" "))
    students[f"{grade}-{sex}"] += 1

cnt = 0
for tmp in students.values():
    cnt += tmp // k
    if tmp % k != 0:
        cnt += 1

print(cnt)
