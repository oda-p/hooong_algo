import sys
from itertools import combinations

n = int(input())
ingredients = []
for _ in range(n):
    ingredients.append(list(map(int, input().split(" "))))

answer = sys.maxsize
for i in range(1, n + 1):
    for cook in combinations(ingredients, i):
        sour = 1
        bitter = 0
        for ingredient in cook:
            sour *= ingredient[0]
            bitter += ingredient[1]

        answer = min(answer, abs(sour - bitter))

print(answer)
