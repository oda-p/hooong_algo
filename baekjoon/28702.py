a = input()
b = input()
c = input()

if a.isdigit():
    x = int(a) + 3
elif b.isdigit():
    x = int(b) + 2
else:
    x = int(c) + 1

if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print(x)
