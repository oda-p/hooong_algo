s = input()

stack = []
answer = 0
before = "("
for ch in s:
    if ch == "(":
        stack.append(ch)
    else:
        stack.pop()

        if before == "(":
            answer += len(stack)
        else:
            answer += 1
    before = ch

print(answer)
