case_num = 1
while True:
    l, p, v = map(int, input().split(" "))
    if [l, p, v] == [0, 0, 0]:
        break

    answer = (v // p) * l + min((v % p), l)
    print(f"Case {case_num}: {answer}")
    case_num += 1
