n, m = map(int, input().split(" "))

not_listen: set = set()
not_watch: set = set()

for _ in range(n):
    not_listen.add(input())

for _ in range(m):
    not_watch.add(input())

not_listen_watch = list(not_listen & not_watch)
not_listen_watch.sort()

print(len(not_listen_watch))
for name in not_listen_watch:
    print(name)
