import heapq

n, k = map(int, input().split())

MIN = 21e8
visit = [0]*100001
def find(now):
    global MIN
    q = []
    heapq.heappush(q, (0, now))  # 이동횟수, 현재 위치
    while q:
        cnt, now = heapq.heappop(q)
        visit[now] = 1
        if cnt > MIN: continue
        if now == k:
            MIN = min(MIN, cnt)

        for next in [now+1, now-1, now*2]:
            if next < 0 or next >100000: continue
            if visit[next] ==1: continue
            if next == now*2:
                heapq.heappush(q, (cnt, next))
            else:
                heapq.heappush(q, (cnt+1, next))
    return MIN

find(n)
print(MIN)

