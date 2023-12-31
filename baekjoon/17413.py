s = input()

split_s = []
tmp = ""
i = 0
for ch in s:
    if ch == "<":
        if tmp:
            split_s.append(tmp)
            tmp = ""
        tmp += ch
    elif ch == ">":
        tmp += ch
        split_s.append(tmp)
        tmp = ""
    else:
        tmp += ch

if tmp:
    split_s.append(tmp)

answer = ""
for part in split_s:
    if part[0] == "<":
        answer += part
    else:
        answer += " ".join([split_part[::-1] for split_part in part.split(" ")])

print(answer)
