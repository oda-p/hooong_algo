import sys


def recursion(s, l, r):
    if l >= r:
        return 1, 1
    elif s[l] != s[r]:
        return 0, 1
    else:
        result, cnt = recursion(s, l + 1, r - 1)
        return result, cnt + 1


def is_palindrome(s):
    return recursion(s, 0, len(s) - 1)


t = int(input())
for _ in range(t):
    result, cnt = is_palindrome(input())
    print(result, cnt)
