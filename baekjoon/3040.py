from itertools import combinations

arr = []
for _ in range(9):
    arr.append(int(input()))

all_sum = sum(arr)
target = []
for tmp in combinations(arr, 2):
    if all_sum - sum(tmp) == 100:
        target = tmp

for num in arr:
    if num in target:
        continue
    print(num)
