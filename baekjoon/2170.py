n = int(input())

dots: list[tuple[int, int]] = []
for _ in range(n):
    x, y = map(int, input().split(" "))
    dots.append((x, y))

dots.sort()

result: list[list[int, int]] = []
for x, y in dots:
    if not result:
        result.append([x, y])
        continue

    last = result[-1]
    if x <= last[1] < y:
        result.pop()
        result.append([last[0], y])
    elif x > last[1]:
        result.append([x, y])

answer: int = 0
for line in result:
    answer += line[1] - line[0]

print(answer)
