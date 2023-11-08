import sys

n, m = map(int, sys.stdin.readline().split(" "))

site_pw_map = {}
for _ in range(n):
    site, pw = map(
        str,
        sys.stdin.readline().replace("\n", "").split(" "),
    )
    site_pw_map[site] = pw

for _ in range(m):
    site = sys.stdin.readline().replace("\n", "")
    print(site_pw_map[site])
