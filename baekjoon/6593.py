import sys
from collections import deque


def find() -> bool:
    l, r, c = map(int, sys.stdin.readline().split(" "))

    if all(x == 0 for x in [l, r, c]):
        return False

    start: tuple[int, int, int] | None = None
    end: tuple[int, int, int] | None = None

    building: list[list[list[str]]] = [[[] for _ in range(r)] for _ in range(l)]
    visited: list[list[list[int]]] = [
        [[10000 for _ in range(c)] for _ in range(r)] for _ in range(l)
    ]
    for level in range(l):
        for row in range(r):
            tmp = sys.stdin.readline()
            for col, v in enumerate(tmp):
                if v == "S":
                    start = (level, row, col)
                    visited[level][row][col] = 0
                elif v == "E":
                    end = (level, row, col)
                elif v == "\n":
                    continue

                building[level][row].append(v)

        sys.stdin.readline()

    q = deque([(start, 0)])
    while q:
        cur, count = q.popleft()
        cl, cr, cc = cur

        # 동,서,남,북,상,하
        d_pos = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]

        for dl, dr, dc in d_pos:
            nl = cl + dl
            nr = cr + dr
            nc = cc + dc

            if (
                0 <= nl < l
                and 0 <= nr < r
                and 0 <= nc < c
                and building[nl][nr][nc] in [".", "E"]
            ):
                if visited[nl][nr][nc] > count + 1:
                    visited[nl][nr][nc] = count + 1

                    if building[nl][nr][nc] != "E":
                        q.append(((nl, nr, nc), count + 1))

    result = visited[end[0]][end[1]][end[2]]
    if result == 10000:
        print("Trapped!")
    else:
        print(f"Escaped in {result} minute(s).")

    return True


if __name__ == "__main__":
    while find():
        pass
