n = int(input())

exist_cards = {}
for num in list(map(int, input().split(" "))):
    exist_cards[num] = True

m = int(input())
for num in list(map(int, input().split(" "))):
    if num in exist_cards:
        print("1", end=" ")
    else:
        print("0", end=" ")
