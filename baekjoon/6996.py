t = int(input())


def get_cnt(s) -> dict:
    cnt = {}

    for ch in s:
        if ch not in cnt:
            cnt[ch] = 0
        cnt[ch] += 1

    return cnt


for _ in range(t):
    a, b = map(str, input().split(" "))

    a_cnt = get_cnt(a)
    b_cnt = get_cnt(b)

    if a_cnt == b_cnt:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")
