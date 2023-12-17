n = int(input())
info = list(map(int, input().split(" ")))


def check(arr):
    if not arr:
        return True

    target = arr[-1]
    bigger_cnt = 0
    for num in arr[:-1]:
        if num > target:
            bigger_cnt += 1

    return info[target - 1] == bigger_cnt


answer = []


def dfs(tmp):
    global answer

    if not check(tmp):
        return False

    if len(tmp) == n:
        print(" ".join([str(num) for num in tmp]))
        return

    for i in range(1, n + 1):
        if i in tmp:
            continue

        tmp.append(i)
        dfs(tmp)
        tmp.pop()


dfs([])
