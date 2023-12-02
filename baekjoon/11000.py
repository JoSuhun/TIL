import heapq
n = int(input())
q = [list(map(int, input().split())) for _ in range(n)]
q.sort()

cnt = []
heapq.heappush(cnt, q[0][1])
for i in range(1, n):
    if q[i][0] >= cnt[0]:
        heapq.heappop(cnt)
        heapq.heappush(cnt, q[i][1])
    else:
        heapq.heappush(cnt, q[i][1])

print(len(cnt))