from collections import deque

k = int(input())

direction_counter = {1: 0, 2: 0, 3: 0, 4: 0}
double_corner = set()
q = deque([])
for _ in range(6):
    direction, length = map(int, input().split(" "))
    q.append([direction, length])

    direction_counter[direction] += 1
    if direction_counter[direction] == 2:
        double_corner.add(direction)

if double_corner == {1, 3}:
    while q[0][0] != 4:
        q.append(q.popleft())
elif double_corner == {2, 4}:
    while q[0][0] != 3:
        q.append(q.popleft())
elif double_corner == {1, 4}:
    while q[0][0] != 2:
        q.append(q.popleft())
else:
    while q[0][0] != 1:
        q.append(q.popleft())

sq_area = (q[0][1] * q[1][1]) - (q[3][1] * q[4][1])
print(sq_area * k)
