n = int(input())
test_rooms = list(map(int, input().split(" ")))
b, c = map(int, input().split(" "))

answer = n
for test_room in test_rooms:
    test_room -= b

    if test_room > 0:
        answer += test_room // c
        if test_room % c > 0:
            answer += 1

print(answer)
