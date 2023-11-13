target = input()

answer = ""

op_stack = []
for ch in target:
    if ch == "(":
        op_stack.append(ch)
    elif ch == ")":
        while op_stack[-1] != "(":
            answer += op_stack.pop()
        op_stack.pop()
    elif ch in ["*", "/"]:
        while op_stack and op_stack[-1] in ["*", "/"]:
            answer += op_stack.pop()
        op_stack.append(ch)
    elif ch in ["+", "-"]:
        while op_stack and op_stack[-1] != "(":
            answer += op_stack.pop()
        op_stack.append(ch)
    else:
        answer += ch

while op_stack:
    answer += op_stack.pop()

print(answer)
