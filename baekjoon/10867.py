n = int(input())
arr = list(map(int, input().split(" ")))

arr = list(set(arr))
arr.sort()

print(" ".join([str(i) for i in arr]))
