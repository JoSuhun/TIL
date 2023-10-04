import heapq
import sys
input = sys.stdin.readline

n, end = map(int, input().split())

mapp = [[] for _ in range(end+1)]
for i in range(end):
    mapp[i].append((i+1, 1))
for i in range(n):
    st, ed, d = map(int, input().split())
    if st>end or ed>end:continue
    mapp[st].append((ed, d))

inf = int(21e8)
result = [inf]*(end+1)

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0,start))
    result[start] = 0

    while heap:
        now, d = heapq.heappop(heap)

        if d > result[now]: continue

        for i in mapp[now]:
            nd = d + i[1]
            if nd < result[i[0]]:
                result[i[0]] = nd
                heapq.heappush(heap, (i[0], nd))

dijkstra(0)
print(result[end])