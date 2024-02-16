n = int(input())
seats = input()

stack = ["*"]
l_cnt = 0
for seat in seats:
    stack.append(seat)
    if seat == "L":
        l_cnt += 1
        if l_cnt < 2:
            continue
        l_cnt = 0
    stack.append("*")

impossible_cnt = 0
while stack:
    cur = stack.pop()

    if cur == "*":
        if stack:
            stack.pop()
    else:
        if stack[-1] == "*":
            stack.pop()
        else:
            impossible_cnt += 1

print(n - impossible_cnt)
