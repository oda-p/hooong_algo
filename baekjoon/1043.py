from itertools import combinations

n, m = map(int, input().split(" "))
people = [i for i in range(n + 1)]


def find(x):
    if x == people[x]:
        return x
    people[x] = find(people[x])
    return people[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        people[y] = x


def solution():
    true_list: list = list(map(int, input().split(" ")))
    if true_list.pop(0) == 0:
        print(m)
        return

    if len(true_list) > 1:
        for x, y in combinations(true_list, 2):
            union(x, y)

    parties = []
    for _ in range(m):
        party = list(map(int, input().split(" ")))
        party.pop(0)
        parties.append(party)

        if len(party) > 1:
            for x, y in combinations(party, 2):
                union(x, y)

    cnt = 0
    for party in parties:
        roots = set()
        for person in party:
            roots.add(find(person))
        if roots != {find(true_list[0])}:
            cnt += 1

    print(cnt)


solution()
