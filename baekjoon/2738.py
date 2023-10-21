def input_matrix():
    return [list(map(int, input().split(" "))) for _ in range(n)]


n, m = map(int, input().split(" "))

matrix_a = input_matrix()
matrix_b = input_matrix()

for i in range(n):
    for j in range(m):
        matrix_a[i][j] += matrix_b[i][j]

for i in range(n):
    print(" ".join([str(x) for x in matrix_a[i]]))
