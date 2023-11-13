n, m = map(int, input().split())
mapp = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    mapp[start].append((end, cost))
for m in mapp:
    print(m)