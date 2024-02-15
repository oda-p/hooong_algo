import sys

t = int(input())

for _ in range(t):
    n = int(input())

    max_school = {"name": "", "drink": 0}
    for _ in range(n):
        school, drink = sys.stdin.readline().split(" ")
        drink = int(drink)

        if max_school["drink"] < drink:
            max_school["name"] = school
            max_school["drink"] = drink

    print(max_school["name"])
