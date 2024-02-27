n = int(input())

sticks = []
for _ in range(n):
    sticks.append(int(input()))

min_h = sticks[-1]
cnt = 1
for h in sticks[-2::-1]:
    if h > min_h:
        cnt += 1
        min_h = h

print(cnt)
