import sys

n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    scores = []
    for _ in range(n):
        scores.append(int(sys.stdin.readline()))

    cut_count = int(n * (15 / 100) + 0.5)

    scores.sort()
    target_scores = scores[cut_count : n - cut_count]
    print(int(sum(target_scores) / len(target_scores) + 0.5))
