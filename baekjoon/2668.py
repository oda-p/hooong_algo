n = int(input())

arr = [0 for _ in range(101)]
for i in range(1, n + 1):
    arr[i] = int(input())

visited = [False for _ in range(101)]
answer = []
for i in range(1, n + 1):
    if visited[i]:
        continue

    def find_circle(num) -> (bool, list):
        tmp_visit = [False for _ in range(101)]

        tmp_visit[num] = True
        tmp_a = {num}
        tmp_b = {arr[num]}
        while True:
            num = arr[num]

            if tmp_visit[num]:
                if arr[num] in tmp_a:
                    return True, list(tmp_a)
                else:
                    return False, []

            tmp_visit[num] = True
            tmp_a.add(num)
            tmp_b.add(arr[num])

            if len(tmp_a) != len(tmp_b):
                return False, []

    has_circle, nums = find_circle(i)
    if has_circle:
        answer.extend(nums)
        for num in nums:
            visited[num] = True

answer.sort()
print(len(answer))
for num in answer:
    print(num)
