n = int(input())
arr: list[int] = list(map(int, input().split(" ")))

s, e = 0, n - 1
answer = [abs(arr[s] + arr[e]), [s, e]]
while s < e:
    tmp: int = arr[s] + arr[e]

    if answer == 0:
        answer = [0, [s, e]]
        break

    if answer[0] >= abs(tmp):
        answer = [abs(tmp), [s, e]]

    if abs(arr[s]) < abs(arr[e]):
        e -= 1
    else:
        s += 1

print(arr[answer[1][0]], arr[answer[1][1]])
