# dijkstra

import heapq

n, m = map(int, input().split())
arr =[[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

start, end = map(int, input().split())

inf = int(21e8)
result = [inf] * n

def dijkstra(start):
    heap = []   # 우선순위 큐 이용 시 사용될 리스트 - 인자값
    heapq.heappush(heap, (0, 0))    # 시작점을 경유지로 등록 (비용, 경유지)
    result[start] = 0   # 시작점이자 경유지는 비용 0

    while heap:
        cost, k = heapq.heappop(heap)

        if cost > result[k]: continue

        for i in arr[k]:
            ncost = cost+i[1]
            if ncost < result[i[0]]:
                result[i[0]] = ncost
                heapq.heappush(heap, (cost, i[0]))
dijkstra(start)
print(*result)