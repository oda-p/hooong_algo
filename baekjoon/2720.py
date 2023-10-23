t = int(input())

test_case = []
for _ in range(t):
    test_case.append(int(input()))

answers = []
for total in test_case:
    tmp = []

    tmp.append(total // 25)
    total %= 25

    tmp.append(total // 10)
    total %= 10

    tmp.append(total // 5)
    total %= 5

    tmp.append(total // 1)

    answers.append(tmp)

for answer in answers:
    print(" ".join([str(x) for x in answer]))
