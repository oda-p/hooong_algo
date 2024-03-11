arr = list(map(int, input().split(" ")))


def check(arr: list[int]) -> bool:
    for i in range(4):
        if arr[i] > arr[i + 1]:
            return False
    return True


while True:
    for i in range(4):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(" ".join([str(num) for num in arr]))

    if check(arr):
        break
