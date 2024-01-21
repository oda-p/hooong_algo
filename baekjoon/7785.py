n = int(input())

now = {}
for _ in range(n):
    name, op = map(str, input().split(" "))

    if op == "enter":
        now[name] = 1
    elif op == "leave":
        if name in now:
            now.pop(name)

answer = list(now.keys())
answer.sort(reverse=True)
for people in answer:
    print(people)
