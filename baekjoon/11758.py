p1_x, p1_y = map(int, input().split(" "))
p2_x, p2_y = map(int, input().split(" "))
p3_x, p3_y = map(int, input().split(" "))

v_1_2 = [(p2_x - p1_x), (p2_y - p1_y)]
v_1_3 = [(p3_x - p1_x), (p3_y - p1_y)]

ccw = (v_1_2[0] * v_1_3[1]) - (v_1_2[1] * v_1_3[0])
if ccw == 0:
    print(0)
elif ccw > 0:
    print(1)
else:
    print(-1)
