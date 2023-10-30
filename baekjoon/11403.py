n = int(input())
INF = 21e8
mapp = [list(map(int, input().split())) for _ in range(n)]
dist = [[INF]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1:
            dist[i][j] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k]+dist[k][j] < dist[i][j]:
                dist[i][j] = 1

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            dist[i][j] = 0

for d in dist:
    print(*d)