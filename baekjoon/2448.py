n = int(input())

base = "  *  \n * * \n*****"
dp = {0: base}

k = 0
tmp = n // 3
while tmp > 1:
    tmp //= 2
    k += 1


def draw(_k):
    if _k in dp:
        return dp[_k]

    before_list = draw(_k - 1).split("\n")
    spaces = " " * (3 * (2 ** (_k - 1)))
    tmp = ""

    for j in range(len(before_list)):
        tmp += spaces + before_list[j] + spaces + "\n"

    for i in range(len(before_list)):
        before = before_list[i]
        tmp += before + " " + before
        if i < len(before_list) - 1:
            tmp += "\n"

    dp[_k] = tmp
    return dp[_k]


draw(k)
print(dp[k])
