n, m = map(int, input().split(" "))
arr1 = list(map(int, input().split(" ")))
arr2 = list(map(int, input().split(" ")))

answer = []
i, j = 0, 0
while True:
    a, b = arr1[i], arr2[j]

    if a < b:
        answer.append(arr1[i])
        i += 1
    elif a > b:
        answer.append(arr2[j])
        j += 1
    else:
        answer.append(arr1[i])
        answer.append(arr2[j])
        i += 1
        j += 1

    if i == n or j == m:
        break

if i < n:
    while i != n:
        answer.append(arr1[i])
        i += 1

if j < m:
    while j != m:
        answer.append(arr2[j])
        j += 1

print(" ".join([str(i) for i in answer]))
