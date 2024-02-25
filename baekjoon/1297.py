from math import sqrt

d, hr, wr = map(int, input().split(" "))

x = sqrt(d**2 / (hr**2 + wr**2))
print(int(hr * x), int(wr * x))
