n = int(input())

fact = 1
for i in range(1, n + 1):
    fact *= i

    while fact % 10 == 0:
        fact //= 10

    fact = int(str(fact)[-100:])

print(str(fact)[-5:].zfill(5))
