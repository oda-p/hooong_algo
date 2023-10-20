cur_pieces = list(map(int, input().split(" ")))
normal_pieces = [1, 1, 2, 2, 2, 8]
for idx in range(len(normal_pieces)):
    cur_pieces[idx] = normal_pieces[idx] - cur_pieces[idx]
print(" ".join([str(x) for x in cur_pieces]))
