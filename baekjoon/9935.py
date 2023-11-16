s = input()
target = input()

stack = []
for ch in s:
    stack.append(ch)

    if len(stack) >= len(target):
        if not stack[-1] == target[-1]:
            continue

        if target == "".join(stack[len(stack) - len(target) :]):
            for _ in range(len(target)):
                stack.pop()

print("".join(stack) if stack else "FRULA")
