s = input()

answer = ""
for ch in s:
    if ch.isalpha():
        base = None
        if ch.isupper():
            base = 65
        else:
            base = 97

        tmp = ord(ch) - base
        tmp = (tmp + 13) % 26
        answer += chr(tmp + base)
    else:
        answer += ch

print(answer)
