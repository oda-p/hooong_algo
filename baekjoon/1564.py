import sys

n = int(sys.stdin.readline())

fact = 1
for i in range(1, n + 1):
    fact *= i

    while fact % 10 == 0:
        fact //= 10

    # rstrip을 사용할 수 있구나!!
    # -12를 알아내는 것은 노가다인가?
    # fact = int(str(fact).rstrip("0")[-12:])

    fact = int(str(fact)[-100:])

print(str(fact)[-5:].zfill(5))
