import sys


def get_distance(mbti_1, mbti_2):
    distance = 0
    for i in range(4):
        if mbti_1[i] != mbti_2[i]:
            distance += 1
    return distance


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    mbti_list = list(map(str, sys.stdin.readline().replace("\n", "").split(" ")))

    # 비둘기집 원리
    # mbti의 개수는 총 16개로 서로 다른 mbti 2개씩 총 32개가 있는 상황에서 1개가 추가되는 경우에는 무조건 3개가 똑같다고 볼 수 있다.
    if len(mbti_list) > 32:
        print(0)
        continue

    min_distance = sys.maxsize
    for i in range(len(mbti_list) - 2):
        for j in range(i + 1, len(mbti_list) - 1):
            for k in range(j + 1, len(mbti_list)):
                a, b, c = mbti_list[i], mbti_list[j], mbti_list[k]
                cur_distance = (
                    get_distance(a, b) + get_distance(b, c) + get_distance(a, c)
                )
                min_distance = min(min_distance, cur_distance)

    print(min_distance)
