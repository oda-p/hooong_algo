n, m = map(int, input().split(" "))

num_name_map = {}
name_num_map = {}
for i in range(1, n + 1):
    name = input()

    num_name_map[i] = name
    name_num_map[name] = i

for _ in range(m):
    problem = input()

    if problem.isnumeric():
        print(num_name_map[int(problem)])
    else:
        print(name_num_map[problem])
