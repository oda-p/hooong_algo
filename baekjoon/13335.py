n, w, l = map(int, input().split(" "))
trucks = list(map(int, input().split(" ")))
times = [0 for _ in range(n)]

time = 0
s, e = 0, 0
cur_w = 0
while s < n - 1 and e < n:
    if cur_w + trucks[e] <= l:
        cur_w += trucks[e]
        e += 1

    for i in range(s, e):
        times[i] += 1
        if times[i] == w:
            s += 1
            cur_w -= trucks[i]

    time += 1
time += w - times[-1] + 1

print(time)
