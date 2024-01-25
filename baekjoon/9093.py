t = int(input())
for _ in range(t):
    s = input().split(" ")

    for c in s:
        print(c[::-1], end=" ")
    print()
