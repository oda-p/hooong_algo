import sys

sys.setrecursionlimit(10000)

nums = []
while True:
    try:
        num = int(input())
        nums.append(num)
    except:
        break


def post_travel(arr):
    root = arr[0]

    left_start = 1
    right_start = len(arr)
    for i in range(1, len(arr)):
        if root < arr[i]:
            right_start = i
            break

    left_arr = arr[left_start:right_start]
    if left_arr:
        post_travel(left_arr)

    right_arr = arr[right_start:]
    if right_arr:
        post_travel(right_arr)
    print(root)


post_travel(nums)
