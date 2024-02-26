n = int(input())
nums = list(map(int, input().split(" ")))
answer = [0 for _ in range(n)]
for idx, num in enumerate(nums):
    for i in range(idx, idx - num, -1):
        answer[i] = answer[i - 1]
    answer[idx - num] = idx + 1
print(" ".join([str(num) for num in answer]))
