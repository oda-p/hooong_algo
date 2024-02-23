n = int(input())

first_counter = {}
for _ in range(n):
    s = input()

    if s[0] not in first_counter:
        first_counter[s[0]] = 0
    first_counter[s[0]] += 1

answer = ""
keys = sorted(list(first_counter.keys()))
for key in keys:
    if first_counter[key] >= 5:
        answer += key

print(answer if answer else "PREDAJA")
