import sys
input = sys.stdin.readline
n = int(input())    # n 도시 개수
m = int(input())    # m 버스 개수
lst = [[] for _ in range(n)]

INF = 21e8
dist = [[INF] * n for _ in range(n)]

for _ in range(m):
    st, ed, cost = map(int, input().split())
    dist[st-1][ed-1] = min(dist[st-1][ed-1], cost)
for i in range(n):
    for j in range(n):
        if i == j: dist[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()