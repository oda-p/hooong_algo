number, base = map(int, input().split(" "))

answer = ""
while number >= base:
    num = number % base

    if num >= 10:
        num = chr(num + 55)
    answer += str(num)

    number = number // base

if number >= 10:
    number = chr(number + 55)
answer += str(number)

print(answer[::-1])
