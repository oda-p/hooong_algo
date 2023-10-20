score_mapping = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

sum_of_score = 0
sum_of_point = 0
for _ in range(20):
    _, point, score_key = input().split(" ")

    if score_key == "P":
        continue

    point = float(point)
    score = score_mapping[score_key]

    sum_of_point += point
    sum_of_score += point * score
print(sum_of_score / sum_of_point)
