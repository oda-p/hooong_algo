n = int(input())

friends = {i: [] for i in range(n)}
for i in range(n):
    row = input()

    for j in range(n):
        if row[j] == "Y":
            friends[i].append(j)

two_friend_cnt = [0 for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        a_friends = friends[i]
        b_friends = friends[j]

        if i in b_friends or set(a_friends) & set(b_friends):
            two_friend_cnt[i] += 1
            two_friend_cnt[j] += 1

print(max(two_friend_cnt))
