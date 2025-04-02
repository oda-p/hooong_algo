n = int(input())
sizes = list(map(int, input().split(" ")))
t, p = map(int, input().split(" "))

shirts_box_count = 0
for size in sizes:
    shirts_box_count += size // t

    if size % t != 0:
        shirts_box_count += 1

print(shirts_box_count)
print(n // p, n % p)
