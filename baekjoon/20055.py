from collections import deque

n, k = map(int, input().split(" "))
belt_hp = list(map(int, input().split(" ")))
robot_tracking = deque([False for _ in range(n)])

belt_hp = deque(belt_hp)
dead_cnt = 0
step = 0
while True:
    step += 1

    # 벨트 회전
    belt_hp.appendleft(belt_hp.pop())
    robot_tracking.appendleft(robot_tracking.pop())
    robot_tracking[0] = False
    robot_tracking[-1] = False

    # 로봇 이동
    for i in range(n - 2, -1, -1):
        if not robot_tracking[i] or robot_tracking[i + 1]:
            continue

        if belt_hp[i + 1] > 0:
            robot_tracking[i] = False
            robot_tracking[i + 1] = True
            belt_hp[i + 1] -= 1

            if belt_hp[i + 1] == 0:
                dead_cnt += 1

    # 0번 인덱스(올리는 칸)에 올릴 수 있으면
    if belt_hp[0] > 0:
        robot_tracking[0] = True
        belt_hp[0] -= 1
        if belt_hp[0] == 0:
            dead_cnt += 1

    # 4 0인게 k개 이상이면 종료
    if dead_cnt >= k:
        print(step)
        break
