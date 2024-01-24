from collections import deque

n = int(input())

cards = deque([i for i in range(1, n + 1)])
del_cards = []
while len(cards) > 1:
    del_cards.append(cards.popleft())
    cards.append(cards.popleft())

del_cards.append(cards[0])
for card in del_cards:
    print(card, end=" ")
print()
