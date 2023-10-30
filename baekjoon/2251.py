import sys
input = sys.stdin.readline  # n 도시 수 // m 버스 노선 수
n, m = map(int, input().split())
nodes = []
INF = 21e8
dist = [INF]*n
for _ in range(m):
    s, e, time = map(int, input().split())
    nodes.append((s-1, e-1, time))

dist[0] = 0

for _ in range(n):
    for node in nodes:
        s, e, time = node
        if dist[s] != INF:
            dist[e] = min(dist[e], dist[s]+time)

cycle = 0
for node in nodes:
    s, e, time = node
    if dist[s] != INF and dist[e] > dist[s]+time: cycle = 1

if cycle: print(-1)
else:
    for i in range(1, n):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])