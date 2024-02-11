len_s, len_p = map(int, input().split(" "))
dna = input()
min_cnt = list(map(int, input().split(" ")))

s, e = 0, len_p - 1
tmp = {"A": 0, "C": 0, "G": 0, "T": 0}
for ch in dna[s : e + 1]:
    tmp[ch] += 1

answer = 0
while True:
    if (
        tmp["A"] >= min_cnt[0]
        and tmp["C"] >= min_cnt[1]
        and tmp["G"] >= min_cnt[2]
        and tmp["T"] >= min_cnt[3]
    ):
        answer += 1

    tmp[dna[s]] -= 1
    s += 1

    e += 1
    if e == len_s:
        break
    tmp[dna[e]] += 1

print(answer)
