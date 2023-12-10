n = int(input())

points = []
for _ in range(n):
    points.append(list(map(int, input().split(" "))))


def calc_ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


area = 0
for i in range(1, n - 1):
    point_a = points[0]
    point_b = points[i]
    point_c = points[i + 1]

    ccw = calc_ccw(
        point_a[0],
        point_a[1],
        point_b[0],
        point_b[1],
        point_c[0],
        point_c[1],
    )

    area += ccw / 2

print(round(abs(area), 1))
