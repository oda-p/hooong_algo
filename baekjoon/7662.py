import heapq
import sys
from collections import defaultdict

t = int(input())

for _ in range(t):
    small_hq = []
    big_hq = []
    number_map = defaultdict(int)  # 문제의 핵심 포인트! (삭제되는 숫자의 존재 개수 현황을 관리하는 맵)
    k = int(input())

    total_num_cnt = 0  # 큐의 요소가 있는지 확인을 수월하기 위한 변수
    for _ in range(k):
        op, num = sys.stdin.readline().replace("\n", "").split(" ")
        num = int(num)

        if op == "I":
            heapq.heappush(small_hq, num)
            heapq.heappush(big_hq, -num)
            number_map[num] += 1
            total_num_cnt += 1
        elif op == "D":
            if not total_num_cnt:
                continue

            total_num_cnt -= 1
            if num == 1:
                max_num = -heapq.heappop(big_hq)
                while number_map[max_num] == 0:
                    max_num = -heapq.heappop(big_hq)
                number_map[max_num] -= 1

            else:
                min_num = heapq.heappop(small_hq)
                while number_map[min_num] == 0:
                    min_num = heapq.heappop(small_hq)
                number_map[min_num] -= 1

    if not total_num_cnt:
        print("EMPTY")
    else:
        max_num = -heapq.heappop(big_hq)
        while number_map[max_num] == 0:
            max_num = -heapq.heappop(big_hq)

        min_num = heapq.heappop(small_hq)
        while number_map[min_num] == 0:
            min_num = heapq.heappop(small_hq)
        print(max_num, min_num)
