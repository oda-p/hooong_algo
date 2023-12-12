import sys

n, m = map(int, input().split(" "))
lectures = list(map(int, input().split(" ")))
total_time = sum(lectures)
max_lecture = max(lectures)


def find_cnt(target_size):
    if target_size < max_lecture:
        return sys.maxsize

    tmp_sum = 0
    _cnt = 1

    for lecture in lectures:
        tmp_sum += lecture
        if tmp_sum > target_size:
            tmp_sum = lecture
            _cnt += 1

    return _cnt


left = 0
right = total_time

min_size = total_time
while left <= right:
    mid = (left + right) // 2

    cnt = find_cnt(mid)
    if cnt <= m:
        right = mid - 1
        min_size = min(min_size, mid)
    else:
        left = mid + 1

print(min_size)
