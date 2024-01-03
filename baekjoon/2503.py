import itertools

n = int(input())

available_numbers = list(itertools.permutations([str(i) for i in range(1, 10)], 3))

tries = []
for _ in range(n):
    tries.append(list(map(int, input().split(" "))))

for t in tries:
    number, strike, ball = t
    number = list(str(number))

    tmp = []
    for candidate in available_numbers:
        b = len(set(number) & set(candidate))
        s = 0

        for i in range(3):
            if number[i] == candidate[i]:
                b -= 1
                s += 1

        if strike == s and ball == b:
            tmp.append(candidate)
    available_numbers = tmp

print(len(available_numbers))
