import heapq
v, e = map(int, input().split())    # v 정점 // e 간선
nodes = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    nodes.append((a, b, cost))