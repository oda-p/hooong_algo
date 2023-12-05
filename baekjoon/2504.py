import sys


def is_correct() -> bool:
    correct_stack = []
    for ch in input_str:
        if ch in ["(", "["]:
            correct_stack.append(ch)
        elif ch == ")":
            if not correct_stack or not correct_stack[-1] == "(":
                return False
            correct_stack.pop()
        elif ch == "]":
            if not correct_stack or not correct_stack[-1] == "[":
                return False
            correct_stack.pop()
    if correct_stack:
        return False
    return True


def dfs(tmp_str) -> int:
    if not tmp_str:
        return 1

    answer = 0
    tmp = ""
    stack = []
    for ch in tmp_str:
        if ch in ["(", "["]:
            stack.append(ch)
        elif ch in [")", "]"]:
            stack.pop()

        tmp += ch

        if not stack:
            multiple_num = 2 if ch == ")" else 3
            answer += multiple_num * dfs(tmp[1:-1])
            tmp = ""

    return answer


if __name__ == "__main__":
    input_str = input()

    if not is_correct():
        print(0)
        sys.exit()

    print(dfs(input_str))
