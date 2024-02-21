n = int(input())

for _ in range(n):
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    a_dict = {i: 0 for i in range(1, 5)}
    for idx in range(1, a[0] + 1):
        a_dict[a[idx]] += 1

    b_dict = {i: 0 for i in range(1, 5)}
    for idx in range(1, b[0] + 1):
        b_dict[b[idx]] += 1

    if a_dict[4] != b_dict[4]:
        print("A" if a_dict[4] > b_dict[4] else "B")
    elif a_dict[3] != b_dict[3]:
        print("A" if a_dict[3] > b_dict[3] else "B")
    elif a_dict[2] != b_dict[2]:
        print("A" if a_dict[2] > b_dict[2] else "B")
    elif a_dict[1] != b_dict[1]:
        print("A" if a_dict[1] > b_dict[1] else "B")
    else:
        print("D")
